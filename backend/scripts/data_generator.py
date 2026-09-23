import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of rows
n = 400000

def generate_dowry_dataset(n_rows):
    data = {}
    
    # ==========================================================================================
    # BOY'S FEATURES (Separate columns)
    # ==========================================================================================
    
    # 1. Boy Height (in feet) - Range: 5.4-6.4 feet
    data['boy_height'] = np.round(np.random.uniform(5.4, 6.4, size=n_rows), 2)
    
    # 2. Boy Income per month (INR) - Range: 5k-100k
    data['boy_income'] = np.random.randint(5000, 100001, size=n_rows)
    
    # 3. Boy Job Type (government or private)
    # Higher income boys more likely to have government jobs
    boy_income_percentile = pd.qcut(data['boy_income'], q=[0, 0.5, 1.0], labels=[0, 1], duplicates='drop')
    job_probs = np.array([
        [0.4, 0.6],   # Lower income: 40% gov, 60% private
        [0.6, 0.4]    # Higher income: 60% gov, 40% private
    ])
    data['boy_job'] = np.array([
        np.random.choice(['government', 'private'], p=job_probs[int(i) if not pd.isna(i) else 0])
        for i in boy_income_percentile
    ])
    
    # 4. Is it boy's first marriage (yes or no)
    data['boy_first_marriage'] = np.random.choice(['yes', 'no'], size=n_rows, p=[0.85, 0.15])
    
    # 5. Boy Father/Family Income (INR/year) - min 15k, max 76k
    boy_fam_income_base = np.random.lognormal(mean=10.7, sigma=0.4, size=n_rows)
    data['boy_father_income'] = boy_fam_income_base.astype(int)
    data['boy_father_income'] = np.clip(data['boy_father_income'], 15000, 76000)
    
    # 6. Boy Area (rural or urban)
    data['boy_area'] = np.random.choice(['rural', 'urban'], size=n_rows, p=[0.45, 0.55])
    
    # 7. Boy Skin Colour (fair, wheatish, dark)
    data['boy_skin_colour'] = np.random.choice(
        ['fair', 'wheatish', 'dark'],
        size=n_rows,
        p=[0.30, 0.50, 0.20]
    )
    
    # 8. Boy Caste
    data['boy_caste'] = np.random.choice(
        ['general', 'OBC', 'SC'],
        size=n_rows,
        p=[0.30, 0.45, 0.25]
    )
    
    # 8b. Boy Religion (hindu, muslim, christian, sikh, others)
    data['boy_religion'] = np.random.choice(
        ['hindu', 'muslim', 'christian', 'sikh', 'others'],
        size=n_rows,
        p=[0.70, 0.15, 0.08, 0.05, 0.02]
    )
    
    # 9. Boy Age - Range: 24-40
    data['boy_age'] = np.random.randint(24, 41, size=n_rows)
    
    # 10. Boy Physical Disability (yes or no) - low probability
    data['boy_physical_disability'] = np.random.choice(['yes', 'no'], size=n_rows, p=[0.05, 0.95])
    
    # 17. Boy Job Stability (stable, unstable, very_stable)
    # Government jobs are mostly stable/very_stable, private jobs have more variation
    job_stability_mapping = np.where(
        data['boy_job'] == 'government',
        np.random.choice(['stable', 'very_stable'], size=n_rows, p=[0.4, 0.6]),
        np.random.choice(['unstable', 'stable', 'very_stable'], size=n_rows, p=[0.3, 0.5, 0.2])
    )
    data['boy_job_stability'] = job_stability_mapping
    
    # ==========================================================================================
    # GIRL'S FEATURES (Separate columns)
    # ==========================================================================================
    
    # 1. Girl Height (in feet) - Range: 5.0-5.11 feet (5.92)
    data['girl_height'] = np.round(np.random.uniform(5.0, 5.92, size=n_rows), 2)
    
    # 2. Girl Income per month (INR) - Range: 1k-70k (many girls may not work or earn less)
    data['girl_income'] = np.random.randint(1000, 70001, size=n_rows)
    
    # 3. Girl Job Type (government or private)
    girl_income_percentile = pd.qcut(data['girl_income'], q=[0, 0.5, 1.0], labels=[0, 1], duplicates='drop')
    data['girl_job'] = np.array([
        np.random.choice(['government', 'private'], p=job_probs[int(i) if not pd.isna(i) else 0])
        for i in girl_income_percentile
    ])
    
    # 4. Is it girl's first marriage (yes or no)
    data['girl_first_marriage'] = np.random.choice(['yes', 'no'], size=n_rows, p=[0.90, 0.10])
    
    # 5. Girl Father/Family Income (INR/year) - min 15k, max 76k
    girl_fam_income_base = np.random.lognormal(mean=10.7, sigma=0.4, size=n_rows)
    data['girl_father_income'] = girl_fam_income_base.astype(int)
    data['girl_father_income'] = np.clip(data['girl_father_income'], 15000, 76000)
    
    # 6. Girl Area (rural or urban)
    data['girl_area'] = np.random.choice(['rural', 'urban'], size=n_rows, p=[0.45, 0.55])
    
    # 7. Girl Skin Colour (fair, wheatish, dark)
    # Fair skin has higher probability for girls in traditional contexts
    data['girl_skin_colour'] = np.random.choice(
        ['fair', 'wheatish', 'dark'],
        size=n_rows,
        p=[0.35, 0.45, 0.20]
    )
    
    # 8. Girl Caste
    data['girl_caste'] = np.random.choice(
        ['general', 'OBC', 'SC'],
        size=n_rows,
        p=[0.30, 0.45, 0.25]
    )
    
    # 8b. Girl Religion (hindu, muslim, christian, sikh, others)
    data['girl_religion'] = np.random.choice(
        ['hindu', 'muslim', 'christian', 'sikh', 'others'],
        size=n_rows,
        p=[0.70, 0.15, 0.08, 0.05, 0.02]
    )
    
    # 9. Girl Age - Range: 20-31
    data['girl_age'] = np.random.randint(20, 32, size=n_rows)
    
    # 10. Girl Physical Disability (yes or no) - low probability
    data['girl_physical_disability'] = np.random.choice(['yes', 'no'], size=n_rows, p=[0.05, 0.95])
    
    # ==========================================================================================
    # HIDDEN LATENT VARIABLES (These will influence the target but NOT be saved in final CSV)
    # ==========================================================================================
    
    # Hidden variable 1: Negotiation skill (0 to 1) - affects final bargaining
    negotiation_skill = np.random.beta(a=2, b=5, size=n_rows)  # Skewed towards lower skills
    
    # Hidden variable 2: Desperation index (0 to 1) - urgency to get married
    desperation_index = np.random.beta(a=3, b=2, size=n_rows)  # Skewed towards higher desperation
    
    # Hidden variable 3: Local cultural norms (-1 to 1) - regional variation
    local_cultural_norms = np.random.normal(0, 0.3, size=n_rows)
    local_cultural_norms = np.clip(local_cultural_norms, -1, 1)
    
    # Hidden variable 4: Boy's family bargaining power
    boy_family_bargaining_power = (
        (data['boy_father_income'] / 76000) * 1.0  # Based only on father income now
    )
    
    # Hidden variable 5: Girl's family bargaining power
    girl_family_bargaining_power = (
        (data['girl_father_income'] / 76000) * 1.0  # Based only on father income now
    )
    
    # ==========================================================================================
    # NON-LINEAR, INTERACTIVE DOWRY CALCULATION WITH HETEROSCEDASTIC NOISE
    # ==========================================================================================
    
    # Calculate boy's wealth index (normalized 0-1 scale) - based on income and father income
    boy_wealth_index = (
        (data['boy_income'] - 5000) / (100000 - 5000) * 0.6 +
        (data['boy_father_income'] - 15000) / (76000 - 15000) * 0.4
    )
    boy_wealth_index = np.clip(boy_wealth_index, 0, 1)
    
    # Calculate girl's wealth index (normalized 0-1 scale) - based on income and father income
    girl_wealth_index = (
        (data['girl_income'] - 1000) / (70000 - 1000) * 0.6 +
        (data['girl_father_income'] - 15000) / (76000 - 15000) * 0.4
    )
    girl_wealth_index = np.clip(girl_wealth_index, 0, 1)
    
    # BASE CALCULATION - Higher dowry when boy's family is wealthier, lower when girl's is wealthier
    base_from_wealth = 500000 * np.exp(boy_wealth_index * 3) * np.exp(-girl_wealth_index * 1.5)
    
    # ============= BOY'S FEATURES CONTRIBUTION (INCREASES DOWRY) =============
    
    # BOY FEATURE 1: Income (HIGHEST IMPACT) - Non-linear with diminishing returns
    boy_income_contribution = data['boy_income'] ** 1.3 * 0.8
    
    # BOY FEATURE 2: Job Type (2nd HIGHEST) - Government job premium
    boy_job_base_premium = np.where(data['boy_job'] == 'government', 1200000, 300000)
    boy_job_interaction_factor = 1 + (0.5 - boy_wealth_index) * 1.5
    boy_job_interaction_factor = np.clip(boy_job_interaction_factor, 0.3, 2.0)
    boy_job_contribution = boy_job_base_premium * boy_job_interaction_factor
    
    # BOY FEATURE 3: First Marriage (3rd HIGHEST)
    boy_first_marriage_base = np.where(data['boy_first_marriage'] == 'yes', 1000000, -300000)
    boy_first_marriage_contribution = boy_first_marriage_base * (1 + desperation_index * 0.5)
    
    # BOY FEATURE 4: Caste (4th HIGHEST)
    boy_caste_base = np.where(data['boy_caste'] == 'general', 700000,
                              np.where(data['boy_caste'] == 'OBC', 350000, 100000))
    boy_caste_contribution = boy_caste_base * (1 + local_cultural_norms * 0.8)
    
    # BOY FEATURE 5: Family income - interaction with bargaining power
    boy_family_contribution = data['boy_father_income'] * 1.2 * (1 + boy_family_bargaining_power)
    
    # BOY FEATURE 6: Height premium (taller = higher dowry)
    boy_height_premium = ((data['boy_height'] - 5.4) ** 2) * 300000
    
    # BOY FEATURE 7: Age effect (older boys slightly less desirable)
    boy_age_penalty = (data['boy_age'] - 24) * -20000
    
    # BOY FEATURE 8: Area (urban boys command higher dowry)
    boy_area_contribution = np.where(data['boy_area'] == 'urban', 200000, 0)
    
    # BOY FEATURE 9: Skin colour (fair = higher dowry in traditional context)
    boy_skin_contribution = np.where(data['boy_skin_colour'] == 'fair', 150000,
                                     np.where(data['boy_skin_colour'] == 'wheatish', 50000, -50000))
    
    # BOY FEATURE 10: Physical Disability (significant penalty)
    boy_disability_penalty = np.where(data['boy_physical_disability'] == 'yes', -800000, 0)
    
    # BOY FEATURE 11: Job Stability (stable job increases dowry)
    boy_job_stability_contribution = np.where(data['boy_job_stability'] == 'very_stable', 400000,
                                              np.where(data['boy_job_stability'] == 'stable', 200000, -100000))
    
    # ============= GIRL'S FEATURES CONTRIBUTION (DECREASES DOWRY) =============
    
    # GIRL FEATURE 1: Income (working girl may reduce dowry slightly)
    girl_income_contribution = -(data['girl_income'] ** 1.1 * 0.3)
    
    # GIRL FEATURE 2: Girl's job type
    girl_job_contribution = np.where(data['girl_job'] == 'government', -300000, -100000)
    
    # GIRL FEATURE 3: First Marriage (second marriage reduces dowry significantly)
    girl_first_marriage_contribution = np.where(data['girl_first_marriage'] == 'yes', 0, -500000)
    
    # GIRL FEATURE 4: Religion and Caste matching/compatibility
    # PRIORITY: Religion > Caste
    # Interreligion marriage = highest dowry penalty/increase (depends on families)
    # Intercaste (same religion, different caste) = moderate impact
    # Same caste and religion = bonus (reduces dowry)
    
    # Religion match status
    same_religion = data['boy_religion'] == data['girl_religion']
    same_caste = data['boy_caste'] == data['girl_caste']
    
    # Calculate religion and caste compatibility impact
    # Interreligion: Major penalty/increase (varies by family tolerance)
    # Intercaste but same religion: Moderate penalty
    # Same religion and caste: Bonus (reduces dowry)
    religion_caste_compatibility = np.where(
        ~same_religion,  # Different religions - HIGHEST IMPACT
        np.random.randint(500000, 1500000, n_rows),  # Interreligion increases dowry significantly
        np.where(
            ~same_caste,  # Same religion but different caste - MODERATE IMPACT
            np.random.randint(100000, 400000, n_rows),  # Intercaste increases dowry moderately
            -200000  # Same religion and caste - BONUS (reduces dowry)
        )
    )
    
    # GIRL FEATURE 5: Girl's family income (wealthy girl's family pays less)
    girl_family_contribution = -data['girl_father_income'] * 0.5 * girl_family_bargaining_power
    
    # GIRL FEATURE 6: Height (shorter girls traditionally preferred)
    girl_height_contribution = -((data['girl_height'] - 5.0) ** 2) * 100000
    
    # GIRL FEATURE 7: Age (older girls face higher dowry pressure)
    girl_age_penalty = (data['girl_age'] - 20) * 80000
    
    # GIRL FEATURE 8: Area (urban girl may have lower dowry expectations)
    girl_area_contribution = np.where(data['girl_area'] == 'urban', -150000, 0)
    
    # GIRL FEATURE 9: Skin colour (fair girl reduces dowry, dark increases it)
    girl_skin_contribution = np.where(data['girl_skin_colour'] == 'fair', -300000,
                                      np.where(data['girl_skin_colour'] == 'wheatish', -100000, 200000))
    
    # GIRL FEATURE 10: Physical Disability (increases dowry significantly)
    girl_disability_penalty = np.where(data['girl_physical_disability'] == 'yes', 1000000, 0)
    
    # Negotiation skill effect (hidden variable)
    negotiation_effect = negotiation_skill * -500000  # Better negotiation = lower dowry
    
    # ==========================================================================================
    # AGGREGATE WITH HETEROSCEDASTIC NOISE
    # ==========================================================================================
    
    # Sum all contributions
    dowry_base = (
        base_from_wealth +
        # Boy's contributions (increase dowry)
        boy_income_contribution +
        boy_job_contribution +
        boy_first_marriage_contribution +
        boy_caste_contribution +
        boy_family_contribution +
        boy_height_premium +
        boy_age_penalty +
        boy_area_contribution +
        boy_skin_contribution +
        boy_disability_penalty +
        boy_job_stability_contribution +
        # Girl's contributions (decrease dowry)
        girl_income_contribution +
        girl_job_contribution +
        girl_first_marriage_contribution +
        religion_caste_compatibility +
        girl_family_contribution +
        girl_height_contribution +
        girl_age_penalty +
        girl_area_contribution +
        girl_skin_contribution +
        girl_disability_penalty +
        # Hidden variables
        negotiation_effect
    )
    
    # HETEROSCEDASTIC NOISE: Variance scales with the magnitude of dowry
    # Low dowry = low variance, High dowry = high variance
    noise_std = np.abs(dowry_base) * np.random.uniform(0.15, 0.35, n_rows)  # 15-35% relative noise
    heteroscedastic_noise = np.random.normal(0, 1, n_rows) * noise_std
    
    # Add proportional multiplicative noise (70% to 130% of base)
    multiplicative_noise = np.random.uniform(0.85, 1.15, n_rows)
    
    # Final calculation
    data['dowry'] = (dowry_base + heteroscedastic_noise) * multiplicative_noise
    data['dowry'] = data['dowry'].astype(int)
    
    # Ensure reasonable bounds
    data['dowry'] = np.clip(data['dowry'], 50000, 80000000)
    
    # ==========================================================================================
    # CREATE FINAL DATAFRAME (WITHOUT HIDDEN VARIABLES)
    # ==========================================================================================
    
    # Create DataFrame with all boy and girl features
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
    })
    
    # ==========================================================================================
    # DERIVED COLUMNS (Created after merging boy and girl data)
    # ==========================================================================================
    
    # 1. Age Difference (boy_age - girl_age)
    df['age_difference'] = df['boy_age'] - df['girl_age']
    
    # 2. Intercaste/Interreligion status
    # Priority: Religion > Caste
    # If different religion -> 'interreligion'
    # If same religion but different caste -> 'intercaste'
    # If same religion and same caste -> 'same_caste_religion'
    
    df['intercaste_interreligion'] = np.where(
        df['boy_religion'] != df['girl_religion'],
        'interreligion',
        np.where(
            df['boy_caste'] != df['girl_caste'],
            'intercaste',
            'same_caste_religion'
        )
    )
    
    # Add target variable at the end
    df['dowry'] = data['dowry']
    
    return df

# Generate dataset
print("Generating realistic synthetic dataset with 400,000 rows...")
print("Incorporating separate boy and girl features, non-linear interactions,")
print("hidden variables, and heteroscedastic noise...")
df = generate_dowry_dataset(n)

# Display first few rows
print("\nFirst 10 rows:")
print(df.head(10))

print("\nDataset Info:")
print(df.info())

print("\nDescriptive Statistics (Numerical columns):")
print(df.describe())

print("\nValue Counts for Boy's Categorical columns:")
for col in ['boy_job', 'boy_first_marriage', 'boy_area', 'boy_skin_colour', 
            'boy_caste', 'boy_religion', 'boy_physical_disability', 'boy_job_stability']:
    print(f"\n{col}:")
    print(df[col].value_counts())

print("\nValue Counts for Girl's Categorical columns:")
for col in ['girl_job', 'girl_first_marriage', 'girl_area', 'girl_skin_colour', 
            'girl_caste', 'girl_religion', 'girl_physical_disability']:
    print(f"\n{col}:")
    print(df[col].value_counts())

print("\nValue Counts for Derived Categorical columns:")
for col in ['intercaste_interreligion']:
    print(f"\n{col}:")
    print(df[col].value_counts())

# Save to CSV
output_file = 'dowry_prediction_dataset.csv'
try:
    df.to_csv(output_file, index=False)
    print(f"\nDataset saved to: {output_file}")
    print(f"File size: {df.memory_usage(deep=True).sum() / (1024**2):.2f} MB")
except PermissionError:
    print(f"\n⚠️ Could not save to {output_file} - file may be open in another program.")
    print("Please close the file and run the script again.")

# Show correlation between features and dowry
print("\nCorrelation with dowry (Top 20):")
numerical_cols = [col for col in df.columns if df[col].dtype in ['int64', 'float64']]
correlations = df[numerical_cols].corr()['dowry'].sort_values(ascending=False)
print(correlations.head(20))

# Additional statistics
print("\n" + "="*80)
print("DOWRY AMOUNT DISTRIBUTION:")
print("="*80)
print(f"Mean: ₹{df['dowry'].mean():,.0f}")
print(f"Median: ₹{df['dowry'].median():,.0f}")
print(f"Std Dev: ₹{df['dowry'].std():,.0f}")
print(f"Coefficient of Variation: {(df['dowry'].std() / df['dowry'].mean()):.2%}")
print(f"\nRange: ₹{df['dowry'].min():,.0f} to ₹{df['dowry'].max():,.0f}")
print(f"\nPercentiles:")
for p in [10, 25, 50, 75, 90, 95, 99]:
    print(f"  {p}th: ₹{df['dowry'].quantile(p/100):,.0f}")

# Boy vs Girl feature comparisons
print("\n" + "="*80)
print("BOY vs GIRL FEATURE COMPARISONS:")
print("="*80)

print(f"\nAGE:")
print(f"  Boy - Range: {df['boy_age'].min()}-{df['boy_age'].max()}, Mean: {df['boy_age'].mean():.1f}")
print(f"  Girl - Range: {df['girl_age'].min()}-{df['girl_age'].max()}, Mean: {df['girl_age'].mean():.1f}")

print(f"\nINCOME:")
print(f"  Boy - Range: ₹{df['boy_income'].min():,} - ₹{df['boy_income'].max():,}, Mean: ₹{df['boy_income'].mean():,.0f}")
print(f"  Girl - Range: ₹{df['girl_income'].min():,} - ₹{df['girl_income'].max():,}, Mean: ₹{df['girl_income'].mean():,.0f}")

print(f"\nHEIGHT:")
print(f"  Boy - Range: {df['boy_height'].min():.2f} - {df['boy_height'].max():.2f} feet, Mean: {df['boy_height'].mean():.2f}")
print(f"  Girl - Range: {df['girl_height'].min():.2f} - {df['girl_height'].max():.2f} feet, Mean: {df['girl_height'].mean():.2f}")

print(f"\nFATHER/FAMILY INCOME:")
print(f"  Boy's family - Mean: ₹{df['boy_father_income'].mean():,.0f}, Median: ₹{df['boy_father_income'].median():,.0f}")
print(f"  Girl's family - Mean: ₹{df['girl_father_income'].mean():,.0f}, Median: ₹{df['girl_father_income'].median():,.0f}")

print(f"\nAGE DIFFERENCE (boy_age - girl_age):")
print(f"  Mean: {df['age_difference'].mean():.2f} years")
print(f"  Median: {df['age_difference'].median():.1f} years")
print(f"  Range: {df['age_difference'].min()} to {df['age_difference'].max()} years")
print(f"  Std Dev: {df['age_difference'].std():.2f} years")

print("\n" + "="*80)
print("Total features: 25 (12 boy + 11 girl + 2 derived + 1 target)")
print("  - Boy features: 12")
print("  - Girl features: 11")
print("  - Derived features: 2 (age_difference, intercaste_interreligion)")
print("  - Target: 1 (dowry)")
print("="*80)
