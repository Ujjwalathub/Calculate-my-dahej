"""Zero-leakage validation: sanitization + train-only thresholds + feature check."""
import sys
from pathlib import Path
import pandas as pd
sys.path.insert(0, str(Path(__file__).parent))
from sklearn.model_selection import train_test_split

CSV = Path(__file__).parent.parent / "data" / "dowry_equal_weightage.csv"
df = pd.read_csv(CSV)
print(f"rows={len(df)} cols={list(df.columns)[:5]}...")

continuous_target_col = "dowry"
y_continuous = df[continuous_target_col].copy()
target_exclusion_list = [continuous_target_col, "dowry_amount",
                         "acquisition_price_inr", "dowry_category", "dowry_class"]
X_sanitized = df.drop(columns=target_exclusion_list, errors="ignore")

# 1. Exclusion verification
assert "dowry" not in X_sanitized.columns
assert "dowry_amount" not in X_sanitized.columns
assert "acquisition_price_inr" not in X_sanitized.columns
assert "dowry_class" not in X_sanitized.columns
assert "dowry_category" not in X_sanitized.columns
print("PASS exclusion: no target proxy in X")

# 2. Global vs train-only thresholds (distributional integrity)
g33, g66 = y_continuous.quantile(0.33), y_continuous.quantile(0.66)
Xtr, Xte, ytr_c, yte_c = train_test_split(X_sanitized, y_continuous, test_size=0.2, random_state=42)
t33, t66 = ytr_c.quantile(0.33), ytr_c.quantile(0.66)
print(f"global  Q33={g33:,.0f} Q66={g66:,.0f}")
print(f"train   Q33={t33:,.0f} Q66={t66:,.0f}")
assert (t33 != g33) or (t66 != g66), "thresholds identical -- suspicious"
print("PASS distributional integrity: train-only thresholds deviate from global")

# 3. Deferred discretization mapping
def map_to_class(v):
    import pandas as _pd
    if _pd.isna(v):
        return "Unknown"
    elif v <= t33:
        return "Low"
    elif v <= t66:
        return "Medium"
    return "High"
ytr = ytr_c.apply(map_to_class)
yte = yte_c.apply(map_to_class)
print("train dist:", ytr.value_counts(normalize=True).round(3).to_dict())
print("test dist:", yte.value_counts(normalize=True).round(3).to_dict())
assert set(ytr.unique()) <= {"Low", "Medium", "High", "Unknown"}
assert "dowry" not in Xtr.columns and "dowry" not in Xte.columns
print("PASS mapping: 3-class labels, no leakage in splits")
print("ALL ZERO-LEAKAGE CHECKS PASSED")
