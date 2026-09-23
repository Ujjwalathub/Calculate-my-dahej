import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
sys.path.append(str(Path(__file__).parent / 'scripts'))
import joblib
import pandas as pd

p = joblib.load('models/preprocessor.pkl')
m = joblib.load('models/trained_models.pkl')

df = pd.read_csv('data/dowry_dataset.csv').head(3)
df_derived = p.create_derived_features(df)
df_trans = p.apply_domain_transformation(df_derived)
df_adv = p.create_advanced_features(df_trans)
X_proc = p.preprocessor.transform(df_adv)

actuals = df['dowry_amount'].values
pred_nn = m['neural_net'].predict(X_proc)
pred_ens = m['ensemble_model'].predict(X_proc)

print("="*60)
for i in range(len(actuals)):
    print(f"Row {i+1}: Actual=Rs.{actuals[i]:,} | Neural Net=Rs.{int(pred_nn[i]):,} | Ensemble=Rs.{int(pred_ens[i]):,}")
print("="*60)
