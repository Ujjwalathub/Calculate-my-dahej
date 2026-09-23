"""
Dowry Prediction Dataset – Synthetic Data Generator
Version: 1.0
Generates a realistic, correlated dataset for ML training (classification + regression).
Output: dowry_dataset.csv
"""

import numpy as np
import pandas as pd
from numpy.random import default_rng

# ── Configuration ──────────────────────────────────────────────────────────────
N_ROWS   = 10_000
SEED     = 42
OUT_FILE = "dowry_dataset.csv"
# ──────────────────────────────────────────────────────────────────────────────

rng = default_rng(SEED)

# ── Helper ─────────────────────────────────────────────────────────────────────
def weighted_choice(choices, weights, size):
    weights = np.array(weights, dtype=float)
    weights /= weights.sum()
    return rng.choice(choices, size=size, p=weights)

EDUCATION_LEVELS = [
    "Illiterate", "Primary", "Middle", "Secondary",
    "Higher Secondary", "Graduate", "Post Graduate", "Doctorate",
]
EDU_IDX = {e: i for i, e in enumerate(EDUCATION_LEVELS)}

# ── 1. Ages ────────────────────────────────────────────────────────────────────
girl_age = np.clip(rng.normal(23, 3, N_ROWS).astype(int), 16, 32)

# age_difference distribution: 70% → 2–6, 20% → 0–1 or 7–9, 10% → 10–15
diff_bucket = rng.choice([0, 1, 2], size=N_ROWS, p=[0.70, 0.20, 0.10])
age_diff = np.where(
    diff_bucket == 0, rng.integers(2, 7, N_ROWS),
    np.where(
        diff_bucket == 1,
        rng.choice(list(range(0, 2)) + list(range(7, 10)), size=N_ROWS),
        rng.integers(10, 16, N_ROWS),
    ),
)
boy_age = np.clip(girl_age + age_diff, 20, 38)
age_difference = boy_age - girl_age

# ── 2. Education ───────────────────────────────────────────────────────────────
edu_weights = [2, 4, 6, 12, 18, 30, 22, 6]  # population-realistic
girl_education = weighted_choice(EDUCATION_LEVELS, edu_weights, N_ROWS)

# Boy education ≥ girl education in ~75 % of cases
boy_edu_indices = []
for ge in girl_education:
    gi = EDU_IDX[ge]
    # weights are higher for indices >= gi
    w = np.array([max(0.2, edu_weights[i] * (2 if i >= gi else 0.4))
                  for i in range(len(EDUCATION_LEVELS))], dtype=float)
    w /= w.sum()
    boy_edu_indices.append(rng.choice(len(EDUCATION_LEVELS), p=w))
boy_education = np.array(EDUCATION_LEVELS)[boy_edu_indices]

# ── 3. Job types (needed before salary) ───────────────────────────────────────
BOY_JOB_TYPES  = ["Private", "Government", "Business", "Farmer", "Unemployed"]
GIRL_JOB_TYPES = ["Private", "Government", "Business", "Housewife", "Student"]

# Boy job correlates with education
def boy_job_weights(edu):
    idx = EDU_IDX[edu]
    # Government / Private more likely with higher education
    if idx >= 6:   # PG / Doctorate
        return [25, 35, 20, 5, 5]
    elif idx == 5: # Graduate
        return [30, 25, 20, 10, 5]
    elif idx == 4: # Higher Secondary
        return [30, 15, 15, 20, 10]
    elif idx <= 2: # Illiterate–Middle
        return [10, 5, 15, 50, 10]
    else:
        return [25, 15, 15, 30, 8]

boy_job_type = np.array([
    weighted_choice(BOY_JOB_TYPES, boy_job_weights(e), 1)[0]
    for e in boy_education
])

def girl_job_weights(edu):
    idx = EDU_IDX[edu]
    if idx >= 5:
        return [30, 20, 15, 20, 5]
    elif idx == 4:
        return [20, 10, 10, 40, 10]
    elif idx <= 2:
        return [5, 2, 5, 80, 3]
    else:
        return [15, 8, 8, 55, 10]

girl_job_type = np.array([
    weighted_choice(GIRL_JOB_TYPES, girl_job_weights(e), 1)[0]
    for e in girl_education
])

# ── 4. Salaries ────────────────────────────────────────────────────────────────
JOB_SALARY_RANGE = {
    "Government": (25_000, 1_50_000),
    "Private":    (12_000, 1_20_000),
    "Business":   (20_000, 2_50_000),
    "Farmer":     ( 8_000,  40_000),
    "Unemployed": (      0,       0),
    "Housewife":  (      0,       0),
    "Student":    (      0,  10_000),
}

def salary_for(job_col):
    salaries = []
    for jt in job_col:
        lo, hi = JOB_SALARY_RANGE[jt]
        if hi == 0:
            salaries.append(0)
        else:
            salaries.append(int(rng.integers(lo, hi + 1)))
    return np.array(salaries)

girl_salary = salary_for(girl_job_type)
boy_salary  = salary_for(boy_job_type)

# ── 5. Family Income ───────────────────────────────────────────────────────────
# Annual; must exceed individual monthly salary * 12 in most cases
family_income_girl = np.clip(
    (girl_salary * 12 * rng.uniform(1.5, 4.0, N_ROWS)).astype(int),
    1_00_000, 25_00_000,
)
family_income_boy = np.clip(
    (boy_salary * 12 * rng.uniform(1.5, 4.0, N_ROWS)).astype(int),
    1_50_000, 40_00_000,
)

# ── 6. Location ────────────────────────────────────────────────────────────────
AREAS = ["Village", "Town", "City"]
girl_area = weighted_choice(AREAS, [35, 35, 30], N_ROWS)
boy_area  = weighted_choice(AREAS, [30, 35, 35], N_ROWS)

def rural_urban_from_areas(ga, ba):
    if ga == "Village" and ba == "Village":
        return rng.choice(["Rural", "Semi-Urban"], p=[0.85, 0.15])
    elif ga == "City" or ba == "City":
        return rng.choice(["Urban", "Semi-Urban"], p=[0.75, 0.25])
    else:
        return rng.choice(["Rural", "Semi-Urban", "Urban"], p=[0.25, 0.50, 0.25])

rural_urban = np.array([rural_urban_from_areas(g, b) for g, b in zip(girl_area, boy_area)])

# ── 7. Marital History ─────────────────────────────────────────────────────────
MARITAL = ["Never Married", "Divorced", "Widowed"]
girl_previous_marriage = weighted_choice(MARITAL, [90, 7, 3], N_ROWS)
boy_previous_marriage  = weighted_choice(MARITAL, [90, 7, 3], N_ROWS)

# ── 8. Caste / Religion / Inter-marriage ──────────────────────────────────────
CASTES    = ["General", "OBC", "SC", "ST", "Other"]
RELIGIONS = ["Hindu", "Muslim", "Christian", "Sikh", "Other"]
INTER     = ["Same Caste Same Religion", "Intercaste", "Interreligion", "Both"]

caste    = weighted_choice(CASTES,    [40, 30, 15, 10, 5], N_ROWS)
religion = weighted_choice(RELIGIONS, [75, 14,  6,  3, 2], N_ROWS)
intercaste_interreligion = weighted_choice(INTER, [82, 10, 5, 3], N_ROWS)

# ── 9. Physical Attributes ─────────────────────────────────────────────────────
SKIN_TONES = ["Fair", "Wheatish", "Medium", "Dark"]
girl_skin_tone = weighted_choice(SKIN_TONES, [25, 35, 25, 15], N_ROWS)
boy_skin_tone  = weighted_choice(SKIN_TONES, [20, 30, 30, 20], N_ROWS)

girl_height = np.clip(rng.normal(155, 5, N_ROWS).astype(int), 145, 175)
boy_height  = np.clip(rng.normal(170, 6, N_ROWS).astype(int), 155, 190)

physical_disability_girl = weighted_choice(["Yes", "No"], [3, 97], N_ROWS)
physical_disability_boy  = weighted_choice(["Yes", "No"], [3, 97], N_ROWS)

# ── 10. Job Stability & Working Abroad ────────────────────────────────────────
def job_stability(job_type):
    mapping = {
        "Government": weighted_choice(["Permanent", "Contract"], [90, 10], 1)[0],
        "Private":    weighted_choice(["Permanent", "Contract", "Unstable"], [50, 35, 15], 1)[0],
        "Business":   weighted_choice(["Business", "Unstable"], [75, 25], 1)[0],
        "Farmer":     weighted_choice(["Permanent", "Unstable"], [60, 40], 1)[0],
        "Unemployed": "Unemployed",
    }
    return mapping[job_type]

job_stability_boy = np.array([job_stability(j) for j in boy_job_type])

# NRI more likely for higher-educated private/business workers
working_abroad_prob = np.where(
    (boy_job_type == "Government") | (boy_job_type == "Farmer") | (boy_job_type == "Unemployed"),
    0.02,
    np.where(np.vectorize(lambda e: EDU_IDX[e])(boy_education) >= 5, 0.15, 0.05),
)
working_abroad = np.where(rng.random(N_ROWS) < working_abroad_prob, "Yes", "No")

# ── 11. Asset Ownership ───────────────────────────────────────────────────────
own_house_boy = weighted_choice(["Yes", "No"], [60, 40], N_ROWS)

LAND_VALS = ["None", "Small", "Medium", "Large"]
land_ownership_boy  = weighted_choice(LAND_VALS, [35, 30, 25, 10], N_ROWS)
land_ownership_girl = weighted_choice(LAND_VALS, [40, 30, 20, 10], N_ROWS)

# ── 12. Target Variable: dowry_score (continuous, 0–1) ────────────────────────
def compute_dowry_score():
    score = np.zeros(N_ROWS)

    # Boy education (+ve)
    score += np.vectorize(lambda e: EDU_IDX[e])(boy_education) / 7 * 0.18

    # Boy salary (+ve, normalised)
    score += np.clip(boy_salary / 2_50_000, 0, 1) * 0.15

    # Boy job type
    job_bonus = {"Government": 0.12, "Business": 0.08, "Private": 0.05,
                 "Farmer": 0.02, "Unemployed": -0.05}
    score += np.array([job_bonus[j] for j in boy_job_type])

    # Working abroad
    score += (working_abroad == "Yes") * 0.12

    # Family income boy (normalised)
    score += np.clip(family_income_boy / 40_00_000, 0, 1) * 0.10

    # Girl previously married → higher dowry pressure
    score += (girl_previous_marriage == "Divorced") * 0.08
    score += (girl_previous_marriage == "Widowed")  * 0.06

    # Own house
    score += (own_house_boy == "Yes") * 0.05

    # Land
    land_map = {"None": 0, "Small": 0.02, "Medium": 0.05, "Large": 0.10}
    score += np.array([land_map[l] for l in land_ownership_boy])

    # Girl disability → higher dowry pressure
    score += (physical_disability_girl == "Yes") * 0.06

    # Skin tone bias (Fair → lower dowry from girl's family perspective)
    skin_map = {"Fair": -0.03, "Wheatish": 0.0, "Medium": 0.02, "Dark": 0.05}
    score += np.array([skin_map[s] for s in girl_skin_tone])

    # Intercaste / interreligion
    inter_map = {
        "Same Caste Same Religion": 0.02,
        "Intercaste": -0.02,
        "Interreligion": -0.03,
        "Both": -0.04,
    }
    score += np.array([inter_map[i] for i in intercaste_interreligion])

    # Rural area → moderate effect
    score += (rural_urban == "Rural") * 0.03

    # Add controlled noise
    score += rng.normal(0, 0.04, N_ROWS)

    return np.clip(score, 0, 1)

dowry_score = compute_dowry_score()

# ── 13. Derive dowry_amount and dowry_category ─────────────────────────────────
# Map score → INR amount (50,000 – 25,00,000)
dowry_amount = (50_000 + dowry_score * (25_00_000 - 50_000)).astype(int)

# Quantile-based category so class distribution is controlled
q33, q66, q85 = np.percentile(dowry_amount, [33, 66, 85])

def categorise(amt):
    if amt <= q33:   return "Low"
    elif amt <= q66: return "Medium"
    elif amt <= q85: return "High"
    else:            return "Very High"

dowry_category = np.array([categorise(a) for a in dowry_amount])

# ── 14. Introduce < 2 % Missing Values ────────────────────────────────────────
NULLABLE_COLS = [
    "girl_skin_tone", "boy_skin_tone", "land_ownership_girl",
    "land_ownership_boy", "girl_salary", "family_income_girl",
]

df = pd.DataFrame({
    "girl_age":                  girl_age,
    "boy_age":                   boy_age,
    "age_difference":            age_difference,
    "girl_education":            girl_education,
    "boy_education":             boy_education,
    "girl_salary":               girl_salary,
    "boy_salary":                boy_salary,
    "rural_urban":               rural_urban,
    "family_income_girl":        family_income_girl,
    "family_income_boy":         family_income_boy,
    "girl_previous_marriage":    girl_previous_marriage,
    "boy_previous_marriage":     boy_previous_marriage,
    "caste":                     caste,
    "religion":                  religion,
    "intercaste_interreligion":  intercaste_interreligion,
    "girl_skin_tone":            girl_skin_tone,
    "boy_skin_tone":             boy_skin_tone,
    "girl_height":               girl_height,
    "boy_height":                boy_height,
    "physical_disability_girl":  physical_disability_girl,
    "physical_disability_boy":   physical_disability_boy,
    "job_stability_boy":         job_stability_boy,
    "working_abroad":            working_abroad,
    "girl_job_type":             girl_job_type,
    "boy_job_type":              boy_job_type,
    "own_house_boy":             own_house_boy,
    "land_ownership_boy":        land_ownership_boy,
    "land_ownership_girl":       land_ownership_girl,
    "girl_area":                 girl_area,
    "boy_area":                  boy_area,
    "dowry_amount":              dowry_amount,
    "dowry_category":            dowry_category,
})

for col in NULLABLE_COLS:
    mask = rng.random(N_ROWS) < 0.015   # ~1.5 % nulls
    df.loc[mask, col] = np.nan

# ── 15. Save ───────────────────────────────────────────────────────────────────
df.to_csv(OUT_FILE, index=False)
print(f"✓ Saved {len(df):,} rows × {len(df.columns)} columns → {OUT_FILE}")

# ── 16. Quick Validation Summary ──────────────────────────────────────────────
print("\n── Category Distribution ──")
print(df["dowry_category"].value_counts())

print("\n── Null Count (nullable cols only) ──")
print(df[NULLABLE_COLS].isnull().sum())

print("\n── Numeric Ranges ──")
print(df[["girl_age","boy_age","age_difference","girl_salary",
          "boy_salary","dowry_amount"]].describe().round(1))
