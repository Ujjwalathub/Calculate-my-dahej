"""
Equal Weightage Dowry Data Generator
=====================================

This generator implements the feature weightage redesign to:
1. Remove all data leakage (no dowry_category features)
2. Ensure equal weightage across all features
3. Apply correct directional effects as per domain rules

Feature Impact Rules (Equal Weightage):
- Boy Income: Positive (Higher income → Higher dowry)
- Boy Father Income: Positive (Higher father income → Higher dowry)
- Girl Income: Negative (Higher income → Lower dowry)
- Girl Father Income: Mild Positive (Slightly higher dowry)
- Boy Job (Government): Strong Positive
- Girl Job (Government): Negative (Decreases dowry)
- Inter-religion: Negative (Decreases dowry)
- Boy Height: Peak at 5.9 ft (Non-linear sweet spot)
- Girl Height: Peak at 5.7 ft (Non-linear sweet spot)
- Boy First Marriage: Negative (Decreases dowry)
- Girl First Marriage: Positive (Increases dowry)
- Boy Physical Disability: Negative (Decreases dowry)
- Girl Physical Disability: Positive (Increases dowry)
- Boy Job Stability: Positive (Stable/Very Stable → Higher)
- Boy Skin Colour (Fair): Positive (Higher dowry)
- Girl Skin Colour (Fair): Negative (Lower dowry)
- Boy Caste (General): Positive (Higher dowry)
- Girl Caste (General): Negative (Lower dowry)
"""

import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)


def generate_equal_weightage_dataset(n_rows: int = 400000) -> pd.DataFrame:
    """
    Generate synthetic dowry dataset with equal feature weightage.
    
    All features contribute approximately equally to the target variable.
    No data leakage - dowry_category is NOT generated or included.
    
    Parameters
    ----------
    n_rows : int
        Number of records to generate
        
    Returns
    -------
    pd.DataFrame
        Dataset with features and dowry target (NO dowry_category)
    """
    
    print(f"\n{'='*80}")
    print("EQUAL WEIGHTAGE DOWRY DATA GENERATOR")
    print(f"{'='*80}")
    print(f"Generating {n_rows:,} records with balanced feature contributions...")
    print(f"{'='*80}\n")
    
    data = {}
    
    # ==========================================================================================
    # BOY'S FEATURES
    # ==========================================================================================
    
    print("[1/3] Generating Boy's Features...")
    
    # Boy Height (5.4-6.4 feet)
    data['boy_height'] = np.round(np.random.uniform(5.4, 6.4, size=n_rows), 2)
    
    # Boy Income per month (INR: 5k-100k)
    data['boy_income'] = np.random.randint(5000, 100001, size=n_rows)
    
    # Boy Job Type (government or private)
    boy_income_percentile = pd.qcut(data['boy_income'], q=[0, 0.5, 1.0], labels=[0, 1], duplicates='drop')
    job_probs = np.array([
        [0.4, 0.6],   # Lower income: 40% gov, 60% private
        [0.6, 0.4]    # Higher income: 60% gov, 40% private
    ])
    data['boy_job'] = np.array([
        np.random.choice(['government', 'private'], p=job_probs[int(i) if not pd.isna(i) else 0])
        for i in boy_income_percentile
    ])
    
    # Boy First Marriage (yes or no)
    data['boy_first_marriage'] = np.random.choice(['yes', 'no'], size=n_rows, p=[0.85, 0.15])
    
    # Boy Father Income (INR/year: 15k-76k)
    boy_fam_income_base = np.random.lognormal(mean=10.7, sigma=0.4, size=n_rows)
    data['boy_father_income'] = np.clip(boy_fam_income_base.astype(int), 15000, 76000)
    
    # Boy Area (rural or urban)
    data['boy_area'] = np.random.choice(['rural', 'urban'], size=n_rows, p=[0.45, 0.55])
    
    # Boy Skin Colour (fair, wheatish, dark)
    data['boy_skin_colour'] = np.random.choice(
        ['fair', 'wheatish', 'dark'],
        size=n_rows,
        p=[0.30, 0.50, 0.20]
    )
    
    # Boy Caste (general, OBC, SC)
    data['boy_caste'] = np.random.choice(
        ['general', 'OBC', 'SC'],
        size=n_rows,
        p=[0.30, 0.45, 0.25]
    )
    
    # Boy Religion (hindu, muslim, christian, sikh, others)
    data['boy_religion'] = np.random.choice(
        ['hindu', 'muslim', 'christian', 'sikh', 'others'],
        size=n_rows,
        p=[0.70, 0.15, 0.08, 0.05, 0.02]
    )
    
    # Boy Age (24-40)
    data['boy_age'] = np.random.randint(24, 41, size=n_rows)
    
    # Boy Physical Disability (yes or no)
    data['boy_physical_disability'] = np.random.choice(['yes', 'no'], size=n_rows, p=[0.05, 0.95])
    
    # Boy Job Stability (stable, unstable, very_stable)
    job_stability_mapping = np.where(
        data['boy_job'] == 'government',
        np.random.choice(['stable', 'very_stable'], size=n_rows, p=[0.4, 0.6]),
        np.random.choice(['unstable', 'stable', 'very_stable'], size=n_rows, p=[0.3, 0.5, 0.2])
    )
    data['boy_job_stability'] = job_stability_mapping
    
    print(f"  ✓ Generated {len([k for k in data.keys() if k.startswith('boy_')])} boy features")
    
    # ==========================================================================================
    # GIRL'S FEATURES
    # ==========================================================================================
    
    print("[2/3] Generating Girl's Features...")
    
    # Girl Height (5.0-5.92 feet)
    data['girl_height'] = np.round(np.random.uniform(5.0, 5.92, size=n_rows), 2)
    
    # Girl Income per month (INR: 1k-70k)
    data['girl_income'] = np.random.randint(1000, 70001, size=n_rows)
    
    # Girl Job Type (government or private)
    girl_income_percentile = pd.qcut(data['girl_income'], q=[0, 0.5, 1.0], labels=[0, 1], duplicates='drop')
    data['girl_job'] = np.array([
        np.random.choice(['government', 'private'], p=job_probs[int(i) if not pd.isna(i) else 0])
        for i in girl_income_percentile
    ])
    
    # Girl First Marriage (yes or no)
    data['girl_first_marriage'] = np.random.choice(['yes', 'no'], size=n_rows, p=[0.90, 0.10])
    
    # Girl Father Income (INR/year: 15k-76k)
    girl_fam_income_base = np.random.lognormal(mean=10.7, sigma=0.4, size=n_rows)
    data['girl_father_income'] = np.clip(girl_fam_income_base.astype(int), 15000, 76000)
    
    # Girl Area (rural or urban)
    data['girl_area'] = np.random.choice(['rural', 'urban'], size=n_rows, p=[0.45, 0.55])
    
    # Girl Skin Colour (fair, wheatish, dark)
    data['girl_skin_colour'] = np.random.choice(
        ['fair', 'wheatish', 'dark'],
        size=n_rows,
        p=[0.35, 0.45, 0.20]
    )
    
    # Girl Caste (general, OBC, SC)
    data['girl_caste'] = np.random.choice(
        ['general', 'OBC', 'SC'],
        size=n_rows,
        p=[0.30, 0.45, 0.25]
    )
    
    # Girl Religion (hindu, muslim, christian, sikh, others)
    data['girl_religion'] = np.random.choice(
        ['hindu', 'muslim', 'christian', 'sikh', 'others'],
        size=n_rows,
        p=[0.70, 0.15, 0.08, 0.05, 0.02]
    )
    
    # Girl Age (20-31)
    data['girl_age'] = np.random.randint(20, 32, size=n_rows)
    
    # Girl Physical Disability (yes or no)
    data['girl_physical_disability'] = np.random.choice(['yes', 'no'], size=n_rows, p=[0.05, 0.95])
    
    print(f"  ✓ Generated {len([k for k in data.keys() if k.startswith('girl_')])} girl features")
    
    # ==========================================================================================
    # EQUAL WEIGHTAGE DOWRY CALCULATION
    # ==========================================================================================
    
    print("[3/3] Calculating Dowry with Equal Weightage...")
    
    # Base dowry amount
    BASE_DOWRY = 2_000_000  # 20 lakhs base
    
    # Standard contribution unit (to ensure equal weightage)
    UNIT_CONTRIBUTION = 200_000  # Each feature contributes ±200k on average
    
    dowry = np.full(n_rows, BASE_DOWRY, dtype=float)
    
    # ==================== FEATURE 1: Boy Income ====================
    # Positive: Higher income → Higher dowry
    # Normalize to 0-1, then scale to contribution
    boy_income_normalized = (data['boy_income'] - 5000) / (100000 - 5000)
    boy_income_contribution = boy_income_normalized * UNIT_CONTRIBUTION
    dowry += boy_income_contribution
    
    # ==================== FEATURE 2: Boy Father Income ====================
    # Positive: Higher father income → Higher dowry
    boy_father_normalized = (data['boy_father_income'] - 15000) / (76000 - 15000)
    boy_father_contribution = boy_father_normalized * UNIT_CONTRIBUTION
    dowry += boy_father_contribution
    
    # ==================== FEATURE 3: Girl Income ====================
    # Negative: Higher income → Lower dowry
    girl_income_normalized = (data['girl_income'] - 1000) / (70000 - 1000)
    girl_income_contribution = -girl_income_normalized * UNIT_CONTRIBUTION
    dowry += girl_income_contribution
    
    # ==================== FEATURE 4: Girl Father Income ====================
    # Mild Positive: Slightly higher dowry
    girl_father_normalized = (data['girl_father_income'] - 15000) / (76000 - 15000)
    girl_father_contribution = girl_father_normalized * UNIT_CONTRIBUTION * 0.5  # Half weight = mild
    dowry += girl_father_contribution
    
    # ==================== FEATURE 5: Boy Job (Government) ====================
    # Strong Positive: Government job increases dowry
    boy_job_contribution = np.where(data['boy_job'] == 'government', UNIT_CONTRIBUTION, -UNIT_CONTRIBUTION * 0.3)
    dowry += boy_job_contribution
    
    # ==================== FEATURE 6: Girl Job (Government) ====================
    # Negative: Government job decreases dowry
    girl_job_contribution = np.where(data['girl_job'] == 'government', -UNIT_CONTRIBUTION, UNIT_CONTRIBUTION * 0.3)
    dowry += girl_job_contribution
    
    # ==================== FEATURE 7: Boy Height (Sweet Spot at 5.9 ft) ====================
    # Peak at 5.9, decreases as height moves away
    boy_height_deviation = np.abs(data['boy_height'] - 5.9)
    boy_height_contribution = -boy_height_deviation * (UNIT_CONTRIBUTION / 0.5)  # Max deviation ~0.5 ft
    dowry += boy_height_contribution
    
    # ==================== FEATURE 8: Girl Height (Sweet Spot at 5.7 ft) ====================
    # Peak at 5.7, decreases as height moves away
    girl_height_deviation = np.abs(data['girl_height'] - 5.7)
    girl_height_contribution = -girl_height_deviation * (UNIT_CONTRIBUTION / 0.46)  # Max deviation ~0.46 ft
    dowry += girl_height_contribution
    
    # ==================== FEATURE 9: Boy First Marriage ====================
    # Negative: First marriage decreases dowry
    boy_first_marriage_contribution = np.where(data['boy_first_marriage'] == 'yes', -UNIT_CONTRIBUTION, UNIT_CONTRIBUTION)
    dowry += boy_first_marriage_contribution
    
    # ==================== FEATURE 10: Girl First Marriage ====================
    # Positive: First marriage increases dowry
    girl_first_marriage_contribution = np.where(data['girl_first_marriage'] == 'yes', UNIT_CONTRIBUTION, -UNIT_CONTRIBUTION)
    dowry += girl_first_marriage_contribution
    
    # ==================== FEATURE 11: Boy Physical Disability ====================
    # Negative: Disability decreases dowry
    boy_disability_contribution = np.where(data['boy_physical_disability'] == 'yes', -UNIT_CONTRIBUTION * 1.5, 0)
    dowry += boy_disability_contribution
    
    # ==================== FEATURE 12: Girl Physical Disability ====================
    # Positive: Disability increases dowry
    girl_disability_contribution = np.where(data['girl_physical_disability'] == 'yes', UNIT_CONTRIBUTION * 1.5, 0)
    dowry += girl_disability_contribution
    
    # ==================== FEATURE 13: Boy Job Stability ====================
    # Positive: Stable/Very Stable increases dowry
    stability_map = {'very_stable': UNIT_CONTRIBUTION, 'stable': UNIT_CONTRIBUTION * 0.5, 'unstable': -UNIT_CONTRIBUTION * 0.5}
    boy_stability_contribution = np.array([stability_map[s] for s in data['boy_job_stability']])
    dowry += boy_stability_contribution
    
    # ==================== FEATURE 14: Boy Skin Colour ====================
    # Positive: Fair skin increases dowry
    boy_skin_map = {'fair': UNIT_CONTRIBUTION * 0.7, 'wheatish': 0, 'dark': -UNIT_CONTRIBUTION * 0.7}
    boy_skin_contribution = np.array([boy_skin_map[s] for s in data['boy_skin_colour']])
    dowry += boy_skin_contribution
    
    # ==================== FEATURE 15: Girl Skin Colour ====================
    # Negative: Fair skin decreases dowry (opposite of boy)
    girl_skin_map = {'fair': -UNIT_CONTRIBUTION * 0.7, 'wheatish': 0, 'dark': UNIT_CONTRIBUTION * 0.7}
    girl_skin_contribution = np.array([girl_skin_map[s] for s in data['girl_skin_colour']])
    dowry += girl_skin_contribution
    
    # ==================== FEATURE 16: Boy Caste ====================
    # Positive: General caste increases dowry
    boy_caste_map = {'general': UNIT_CONTRIBUTION * 0.8, 'OBC': 0, 'SC': -UNIT_CONTRIBUTION * 0.8}
    boy_caste_contribution = np.array([boy_caste_map[c] for c in data['boy_caste']])
    dowry += boy_caste_contribution
    
    # ==================== FEATURE 17: Girl Caste ====================
    # Negative: General caste decreases dowry (opposite of boy)
    girl_caste_map = {'general': -UNIT_CONTRIBUTION * 0.8, 'OBC': 0, 'SC': UNIT_CONTRIBUTION * 0.8}
    girl_caste_contribution = np.array([girl_caste_map[c] for c in data['girl_caste']])
    dowry += girl_caste_contribution
    
    # ==================== FEATURE 18: Inter-religion ====================
    # Negative: Inter-religion decreases dowry
    same_religion = data['boy_religion'] == data['girl_religion']
    interreligion_contribution = np.where(same_religion, 0, -UNIT_CONTRIBUTION * 1.2)
    dowry += interreligion_contribution
    
    # ==========================================================================================
    # ADD REALISTIC NOISE
    # ==========================================================================================
    
    # Add heteroscedastic noise (variance scales with dowry amount)
    noise_std = np.abs(dowry) * np.random.uniform(0.08, 0.15, n_rows)  # 8-15% noise
    noise = np.random.normal(0, 1, n_rows) * noise_std
    dowry += noise
    
    # Ensure reasonable bounds
    data['dowry'] = np.clip(dowry, 100000, 10000000).astype(int)
    
    print(f"  ✓ Dowry calculated with equal weightage")
    print(f"  ✓ Base dowry: ₹{BASE_DOWRY:,}")
    print(f"  ✓ Standard contribution per feature: ±₹{UNIT_CONTRIBUTION:,}")
    
    # ==========================================================================================
    # CREATE DERIVED FEATURES
    # ==========================================================================================
    
    # Age Difference
    age_difference = data['boy_age'] - data['girl_age']
    
    # Intercaste/Interreligion status
    same_religion_bool = data['boy_religion'] == data['girl_religion']
    same_caste_bool = data['boy_caste'] == data['girl_caste']
    
    intercaste_interreligion = np.where(
        ~same_religion_bool,
        'interreligion',
        np.where(
            ~same_caste_bool,
            'intercaste',
            'same_caste_religion'
        )
    )
    
    # ==========================================================================================
    # CREATE FINAL DATAFRAME
    # ==========================================================================================
    
    df = pd.DataFrame({
        # Boy's features
        'boy_height': data['boy_height'],
        'boy_income': data['boy_income'],
        'boy_job': data['boy_job'],
        'boy_first_marriage': data['boy_first_marriage'],
        'boy_father_income': data['boy_father_income'],
        'boy_area': data['boy_area'],
        'boy_skin_colour': data['boy_skin_colour'],
        'boy_caste': data['boy_caste'],
        'boy_religion': data['boy_religion'],
        'boy_age': data['boy_age'],
        'boy_physical_disability': data['boy_physical_disability'],
        'boy_job_stability': data['boy_job_stability'],
        # Girl's features
        'girl_height': data['girl_height'],
        'girl_income': data['girl_income'],
        'girl_job': data['girl_job'],
        'girl_first_marriage': data['girl_first_marriage'],
        'girl_father_income': data['girl_father_income'],
        'girl_area': data['girl_area'],
        'girl_skin_colour': data['girl_skin_colour'],
        'girl_caste': data['girl_caste'],
        'girl_religion': data['girl_religion'],
        'girl_age': data['girl_age'],
        'girl_physical_disability': data['girl_physical_disability'],
        # Derived features
        'age_difference': age_difference,
        'intercaste_interreligion': intercaste_interreligion,
        # Target (NO dowry_category - preventing data leakage)
        'dowry': data['dowry']
    })
    
    print(f"\n{'='*80}")
    print("DATASET GENERATION COMPLETE")
    print(f"{'='*80}")
    print(f"Total records: {len(df):,}")
    print(f"Total features: {len(df.columns) - 1} (excluding target)")
    print(f"Target column: dowry")
    print(f"\n⚠️  NOTE: NO dowry_category column generated (prevents data leakage)")
    print(f"{'='*80}\n")
    
    return df


if __name__ == "__main__":
    # Generate dataset
    df = generate_equal_weightage_dataset(n_rows=400000)
    
    # Display statistics
    print("\n" + "="*80)
    print("DATASET STATISTICS")
    print("="*80)
    
    print("\n[DOWRY DISTRIBUTION]")
    print(f"Mean: ₹{df['dowry'].mean():,.0f}")
    print(f"Median: ₹{df['dowry'].median():,.0f}")
    print(f"Std Dev: ₹{df['dowry'].std():,.0f}")
    print(f"Min: ₹{df['dowry'].min():,.0f}")
    print(f"Max: ₹{df['dowry'].max():,.0f}")
    
    print("\n[PERCENTILES]")
    for p in [10, 25, 50, 75, 90, 95, 99]:
        print(f"  {p}th: ₹{df['dowry'].quantile(p/100):,.0f}")
    
    print("\n[FEATURE CORRELATIONS WITH DOWRY] (Top 15)")
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    correlations = df[numerical_cols].corr()['dowry'].abs().sort_values(ascending=False)
    print(correlations.head(15))
    
    print("\n[CATEGORICAL FEATURES SAMPLE]")
    print(f"\nIntercaste/Interreligion:")
    print(df['intercaste_interreligion'].value_counts())
    print(f"\nBoy Job:")
    print(df['boy_job'].value_counts())
    print(f"\nGirl Job:")
    print(df['girl_job'].value_counts())
    
    # CRITICAL VERIFICATION: Ensure no dowry_category column exists
    print("\n" + "="*80)
    print("DATA LEAKAGE CHECK")
    print("="*80)
    leakage_cols = [col for col in df.columns if 'dowry_category' in col.lower()]
    if leakage_cols:
        print(f"⚠️  WARNING: Found potential leakage columns: {leakage_cols}")
    else:
        print("✓ PASSED: No dowry_category columns found")
        print("✓ Data leakage prevention successful")
    print("="*80)
    
    # Save to CSV
    output_file = '../data/dowry_equal_weightage.csv'
    try:
        df.to_csv(output_file, index=False)
        print(f"\n✓ Dataset saved to: {output_file}")
        print(f"  File size: {df.memory_usage(deep=True).sum() / (1024**2):.2f} MB")
        print("="*80 + "\n")
    except PermissionError:
        print(f"\n⚠️  Could not save to {output_file} - file may be open")
        print("Please close the file and run again.")
    except Exception as e:
        print(f"\n❌ Error saving file: {e}")
