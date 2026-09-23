"""
Validate Weightage Rules
Verify that the feature impacts follow the specified rules
"""

import pandas as pd
import numpy as np
from apply_weightage import DowryWeightageCalculator


def validate_feature_rules(csv_path: str):
    """
    Validate that calculated dowries follow the feature impact rules.
    """
    print("="*80)
    print("VALIDATING FEATURE IMPACT RULES")
    print("="*80)
    
    # Load data
    df = pd.read_csv(csv_path)
    calculator = DowryWeightageCalculator()
    
    # Calculate dowry for all rows
    df['dowry_calc'] = df.apply(calculator.calculate_dowry, axis=1)
    
    validation_results = []
    
    # 1. Boy Income - Positive correlation
    print("\n1. Boy Income (Positive):")
    corr = df['boy_income'].corr(df['dowry_calc'])
    print(f"   Correlation: {corr:.4f}")
    validation_results.append(("Boy Income Positive", corr > 0))
    
    # 2. Boy Father Income - Positive correlation
    print("\n2. Boy Father Income (Positive):")
    corr = df['boy_father_income'].corr(df['dowry_calc'])
    print(f"   Correlation: {corr:.4f}")
    validation_results.append(("Boy Father Income Positive", corr > 0))
    
    # 3. Girl Income - Negative correlation
    print("\n3. Girl Income (Negative):")
    corr = df['girl_income'].corr(df['dowry_calc'])
    print(f"   Correlation: {corr:.4f}")
    validation_results.append(("Girl Income Negative", corr < 0))
    
    # 4. Girl Father Income - Mild Positive
    print("\n4. Girl Father Income (Mild Positive):")
    corr = df['girl_father_income'].corr(df['dowry_calc'])
    print(f"   Correlation: {corr:.4f}")
    validation_results.append(("Girl Father Income Mild Positive", corr > 0))
    
    # 5. Boy Job - Government vs Private
    print("\n5. Boy Job (Government > Private):")
    gov_mean = df[df['boy_job'] == 'government']['dowry_calc'].mean()
    pvt_mean = df[df['boy_job'] == 'private']['dowry_calc'].mean()
    print(f"   Government: ₹{gov_mean:,.0f}")
    print(f"   Private: ₹{pvt_mean:,.0f}")
    print(f"   Difference: ₹{gov_mean - pvt_mean:,.0f}")
    validation_results.append(("Boy Govt Job Higher", gov_mean > pvt_mean))
    
    # 6. Girl Job - Government vs Private (opposite)
    print("\n6. Girl Job (Government < Private for dowry):")
    df_girl_govt = df[df['girl_job'] == 'government']['dowry_calc'].mean()
    df_girl_pvt = df[df['girl_job'] == 'private']['dowry_calc'].mean()
    print(f"   Girl Government: ₹{df_girl_govt:,.0f}")
    print(f"   Girl Private: ₹{df_girl_pvt:,.0f}")
    print(f"   Difference: ₹{df_girl_pvt - df_girl_govt:,.0f}")
    validation_results.append(("Girl Govt Job Lower", df_girl_govt < df_girl_pvt))
    
    # 7. Inter-religion impact
    print("\n7. Inter-religion (Negative Impact):")
    same_religion = df[df['intercaste_interreligion'] == 'same_caste_religion']['dowry_calc'].mean()
    inter_religion = df[df['intercaste_interreligion'] == 'interreligion']['dowry_calc'].mean()
    print(f"   Same Religion: ₹{same_religion:,.0f}")
    print(f"   Inter-religion: ₹{inter_religion:,.0f}")
    print(f"   Difference: ₹{same_religion - inter_religion:,.0f}")
    validation_results.append(("Inter-religion Negative", inter_religion < same_religion))
    
    # 8. Boy Height - Peak at 5.9
    print("\n8. Boy Height (Peak at 5.9 ft):")
    height_groups = df.groupby(pd.cut(df['boy_height'], bins=[5.0, 5.5, 5.8, 6.0, 6.2, 7.0]))['dowry_calc'].mean()
    print("   Height ranges and average dowry:")
    for height_range, avg_dowry in height_groups.items():
        print(f"   {height_range}: ₹{avg_dowry:,.0f}")
    
    # 9. Girl Height - Peak at 5.7
    print("\n9. Girl Height (Peak at 5.7 ft):")
    height_groups = df.groupby(pd.cut(df['girl_height'], bins=[4.5, 5.3, 5.6, 5.8, 6.0, 6.5]))['dowry_calc'].mean()
    print("   Height ranges and average dowry:")
    for height_range, avg_dowry in height_groups.items():
        print(f"   {height_range}: ₹{avg_dowry:,.0f}")
    
    # 10. Boy First Marriage
    print("\n10. Boy First Marriage (Negative):")
    boy_first_yes = df[df['boy_first_marriage'] == 'yes']['dowry_calc'].mean()
    boy_first_no = df[df['boy_first_marriage'] == 'no']['dowry_calc'].mean()
    print(f"    First Marriage: ₹{boy_first_yes:,.0f}")
    print(f"    Not First: ₹{boy_first_no:,.0f}")
    print(f"    Difference: ₹{boy_first_no - boy_first_yes:,.0f}")
    validation_results.append(("Boy First Marriage Negative", boy_first_yes < boy_first_no))
    
    # 11. Girl First Marriage
    print("\n11. Girl First Marriage (Positive):")
    girl_first_yes = df[df['girl_first_marriage'] == 'yes']['dowry_calc'].mean()
    girl_first_no = df[df['girl_first_marriage'] == 'no']['dowry_calc'].mean()
    print(f"    First Marriage: ₹{girl_first_yes:,.0f}")
    print(f"    Not First: ₹{girl_first_no:,.0f}")
    print(f"    Difference: ₹{girl_first_yes - girl_first_no:,.0f}")
    validation_results.append(("Girl First Marriage Positive", girl_first_yes > girl_first_no))
    
    # 12. Boy Physical Disability
    print("\n12. Boy Physical Disability (Negative):")
    boy_disabled = df[df['boy_physical_disability'] == 'yes']['dowry_calc'].mean()
    boy_not_disabled = df[df['boy_physical_disability'] == 'no']['dowry_calc'].mean()
    print(f"    With Disability: ₹{boy_disabled:,.0f}")
    print(f"    No Disability: ₹{boy_not_disabled:,.0f}")
    print(f"    Difference: ₹{boy_not_disabled - boy_disabled:,.0f}")
    validation_results.append(("Boy Disability Negative", boy_disabled < boy_not_disabled))
    
    # 13. Girl Physical Disability (if data exists)
    if (df['girl_physical_disability'] == 'yes').any():
        print("\n13. Girl Physical Disability (Positive):")
        girl_disabled = df[df['girl_physical_disability'] == 'yes']['dowry_calc'].mean()
        girl_not_disabled = df[df['girl_physical_disability'] == 'no']['dowry_calc'].mean()
        print(f"    With Disability: ₹{girl_disabled:,.0f}")
        print(f"    No Disability: ₹{girl_not_disabled:,.0f}")
        print(f"    Difference: ₹{girl_disabled - girl_not_disabled:,.0f}")
        validation_results.append(("Girl Disability Positive", girl_disabled > girl_not_disabled))
    
    # 14. Boy Job Stability
    print("\n14. Boy Job Stability (Positive):")
    for stability in ['very_stable', 'stable', 'unstable']:
        avg = df[df['boy_job_stability'] == stability]['dowry_calc'].mean()
        print(f"    {stability.capitalize()}: ₹{avg:,.0f}")
    
    # 15. Boy Skin Colour
    print("\n15. Boy Skin Colour (Fair > Wheatish > Dark):")
    for colour in ['fair', 'wheatish', 'dark']:
        avg = df[df['boy_skin_colour'] == colour]['dowry_calc'].mean()
        print(f"    {colour.capitalize()}: ₹{avg:,.0f}")
    
    # 16. Girl Skin Colour (opposite)
    print("\n16. Girl Skin Colour (Fair < Wheatish < Dark):")
    for colour in ['fair', 'wheatish', 'dark']:
        avg = df[df['girl_skin_colour'] == colour]['dowry_calc'].mean()
        print(f"    {colour.capitalize()}: ₹{avg:,.0f}")
    
    # 17. Boy Caste
    print("\n17. Boy Caste (General > OBC > SC):")
    for caste in ['general', 'OBC', 'SC']:
        if (df['boy_caste'] == caste).any():
            avg = df[df['boy_caste'] == caste]['dowry_calc'].mean()
            print(f"    {caste}: ₹{avg:,.0f}")
    
    # 18. Girl Caste (opposite)
    print("\n18. Girl Caste (General < OBC < SC):")
    for caste in ['general', 'OBC', 'SC']:
        if (df['girl_caste'] == caste).any():
            avg = df[df['girl_caste'] == caste]['dowry_calc'].mean()
            print(f"    {caste}: ₹{avg:,.0f}")
    
    # Summary
    print("\n" + "="*80)
    print("VALIDATION SUMMARY")
    print("="*80)
    passed = sum(1 for _, result in validation_results if result)
    total = len(validation_results)
    print(f"Tests Passed: {passed}/{total}")
    print()
    for rule, result in validation_results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"  {status}: {rule}")
    print("="*80)


if __name__ == "__main__":
    import sys
    
    csv_path = sys.argv[1] if len(sys.argv) > 1 else '../data/dowry.csv'
    validate_feature_rules(csv_path)
