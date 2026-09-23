"""
Dowry Weightage Calculator
Based on Feature Impact Rules

This script applies realistic weightages to calculate dowry amounts
based on various social, economic, and demographic factors.
"""

import pandas as pd
import numpy as np
from typing import Dict, Any


class DowryWeightageCalculator:
    """
    Calculate dowry amounts based on feature weightages and rules.
    
    Feature Impact Rules:
    - Boy Income: Positive (Higher income → Higher dowry)
    - Boy Father Income: Positive (Higher father income → Higher dowry)
    - Girl Income: Negative (Higher income → Lower dowry)
    - Girl Father Income: Mild Positive (Slightly higher dowry)
    - Boy Job (Government): Strong Positive (Sweet spot)
    - Girl Job (Government): Negative (Decreases dowry)
    - Inter-religion: Negative (Decreases dowry)
    - Boy Height: Peak at 5.9 ft (Non-linear)
    - Girl Height: Peak at 5.7 ft (Non-linear)
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
    
    def __init__(self):
        # Base dowry amount
        self.base_dowry = 3_000_000  # 30 lakhs base
        
        # Income weightages (per unit of income)
        self.boy_income_weight = 50  # Strong positive
        self.boy_father_income_weight = 40  # Strong positive
        self.girl_income_weight = -25  # Negative
        self.girl_father_income_weight = 10  # Mild positive
        
        # Job type weights
        self.job_weights = {
            'boy': {
                'government': 1_500_000,  # Strong positive (15 lakhs)
                'private': 0,
            },
            'girl': {
                'government': -800_000,  # Negative (8 lakhs reduction)
                'private': 0,
            }
        }
        
        # Job stability weights (for boy)
        self.job_stability_weights = {
            'very_stable': 800_000,
            'stable': 400_000,
            'unstable': -400_000,
        }
        
        # Marriage status weights
        self.marriage_weights = {
            'boy_first_yes': -300_000,  # First marriage decreases
            'boy_first_no': 0,
            'girl_first_yes': 500_000,  # First marriage increases
            'girl_first_no': 0,
        }
        
        # Physical disability weights
        self.disability_weights = {
            'boy_yes': -1_200_000,  # Strong negative
            'boy_no': 0,
            'girl_yes': 600_000,  # Positive (compensation)
            'girl_no': 0,
        }
        
        # Skin colour weights
        self.skin_colour_weights = {
            'boy': {
                'fair': 600_000,
                'wheatish': 0,
                'dark': -300_000,
            },
            'girl': {
                'fair': -400_000,  # Negative (opposite of boy)
                'wheatish': 0,
                'dark': 200_000,
            }
        }
        
        # Caste weights
        self.caste_weights = {
            'boy': {
                'general': 700_000,  # Positive
                'OBC': 0,
                'SC': -400_000,
            },
            'girl': {
                'general': -500_000,  # Negative (opposite)
                'OBC': 0,
                'SC': 300_000,
            }
        }
        
        # Inter-caste/religion weights
        self.intercaste_religion_weights = {
            'interreligion': -1_000_000,  # Strong negative
            'intercaste': -500_000,
            'same_caste_religion': 0,
        }
        
        # Height sweet spots
        self.boy_height_sweet_spot = 5.9
        self.girl_height_sweet_spot = 5.7
        self.height_deviation_penalty = 200_000  # Per 0.1 ft deviation
    
    def calculate_height_impact(self, height: float, gender: str) -> float:
        """
        Calculate height impact with sweet spot logic.
        Peak at 5.9 ft for boys, 5.7 ft for girls.
        Deviation from sweet spot gradually decreases dowry.
        
        Formula:
        - Boy: -abs(boy_height - 5.9) * 2,500,000
        - Girl: -abs(girl_height - 5.7) * 1,800,000
        """
        if gender == 'boy':
            return -abs(height - 5.9) * 2_500_000
        else:  # girl
            return -abs(height - 5.7) * 1_800_000
    
    def calculate_income_impact(self, row: pd.Series) -> float:
        """Calculate combined income impact."""
        boy_income_impact = row['boy_income'] * self.boy_income_weight
        boy_father_impact = row['boy_father_income'] * self.boy_father_income_weight
        girl_income_impact = row['girl_income'] * self.girl_income_weight
        girl_father_impact = row['girl_father_income'] * self.girl_father_income_weight
        
        return boy_income_impact + boy_father_impact + girl_income_impact + girl_father_impact
    
    def calculate_job_impact(self, row: pd.Series) -> float:
        """Calculate job type impact for both boy and girl."""
        boy_job_impact = self.job_weights['boy'].get(row['boy_job'], 0)
        girl_job_impact = self.job_weights['girl'].get(row['girl_job'], 0)
        
        # Add job stability for boy
        job_stability_impact = self.job_stability_weights.get(row['boy_job_stability'], 0)
        
        return boy_job_impact + girl_job_impact + job_stability_impact
    
    def calculate_marriage_impact(self, row: pd.Series) -> float:
        """Calculate marriage status impact."""
        boy_key = f"boy_first_{row['boy_first_marriage']}"
        girl_key = f"girl_first_{row['girl_first_marriage']}"
        
        boy_impact = self.marriage_weights.get(boy_key, 0)
        girl_impact = self.marriage_weights.get(girl_key, 0)
        
        return boy_impact + girl_impact
    
    def calculate_disability_impact(self, row: pd.Series) -> float:
        """Calculate physical disability impact."""
        boy_key = f"boy_{row['boy_physical_disability']}"
        girl_key = f"girl_{row['girl_physical_disability']}"
        
        boy_impact = self.disability_weights.get(boy_key, 0)
        girl_impact = self.disability_weights.get(girl_key, 0)
        
        return boy_impact + girl_impact
    
    def calculate_skin_colour_impact(self, row: pd.Series) -> float:
        """Calculate skin colour impact."""
        boy_impact = self.skin_colour_weights['boy'].get(row['boy_skin_colour'], 0)
        girl_impact = self.skin_colour_weights['girl'].get(row['girl_skin_colour'], 0)
        
        return boy_impact + girl_impact
    
    def calculate_caste_impact(self, row: pd.Series) -> float:
        """Calculate caste impact."""
        boy_impact = self.caste_weights['boy'].get(row['boy_caste'], 0)
        girl_impact = self.caste_weights['girl'].get(row['girl_caste'], 0)
        
        return boy_impact + girl_impact
    
    def calculate_intercaste_religion_impact(self, row: pd.Series) -> float:
        """Calculate inter-caste/religion impact."""
        return self.intercaste_religion_weights.get(row['intercaste_interreligion'], 0)
    
    def calculate_dowry(self, row: pd.Series) -> float:
        """
        Calculate total dowry amount based on all features.
        
        Returns:
            float: Calculated dowry amount (minimum 0)
        """
        dowry = self.base_dowry
        
        # Add all impacts
        dowry += self.calculate_income_impact(row)
        dowry += self.calculate_job_impact(row)
        dowry += self.calculate_height_impact(row['boy_height'], 'boy')
        dowry += self.calculate_height_impact(row['girl_height'], 'girl')
        dowry += self.calculate_marriage_impact(row)
        dowry += self.calculate_disability_impact(row)
        dowry += self.calculate_skin_colour_impact(row)
        dowry += self.calculate_caste_impact(row)
        dowry += self.calculate_intercaste_religion_impact(row)
        
        # Add some random variation (±5%)
        variation = np.random.uniform(-0.05, 0.05)
        dowry *= (1 + variation)
        
        # Ensure minimum dowry is 0
        return max(0, dowry)
    
    def get_feature_breakdown(self, row: pd.Series) -> Dict[str, float]:
        """
        Get detailed breakdown of all feature impacts.
        Useful for understanding and debugging.
        """
        return {
            'base_dowry': self.base_dowry,
            'income_impact': self.calculate_income_impact(row),
            'job_impact': self.calculate_job_impact(row),
            'boy_height_impact': self.calculate_height_impact(row['boy_height'], 'boy'),
            'girl_height_impact': self.calculate_height_impact(row['girl_height'], 'girl'),
            'marriage_impact': self.calculate_marriage_impact(row),
            'disability_impact': self.calculate_disability_impact(row),
            'skin_colour_impact': self.calculate_skin_colour_impact(row),
            'caste_impact': self.calculate_caste_impact(row),
            'intercaste_religion_impact': self.calculate_intercaste_religion_impact(row),
        }


def apply_weightage_to_dataset(input_csv: str, output_csv: str, show_breakdown: bool = False):
    """
    Apply weightage rules to dataset and generate new dowry amounts.
    
    Args:
        input_csv: Path to input CSV file
        output_csv: Path to output CSV file
        show_breakdown: If True, print feature breakdown for first few rows
    """
    # Load data
    print(f"Loading data from {input_csv}...")
    df = pd.read_csv(input_csv)
    print(f"Loaded {len(df)} records")
    
    # Initialize calculator
    calculator = DowryWeightageCalculator()
    
    # Calculate new dowry amounts
    print("Calculating dowry amounts with weightage rules...")
    df['dowry_calculated'] = df.apply(calculator.calculate_dowry, axis=1)
    
    # Round to nearest integer
    df['dowry_calculated'] = df['dowry_calculated'].round().astype(int)
    
    # Show breakdown for first few rows if requested
    if show_breakdown:
        print("\n" + "="*80)
        print("FEATURE IMPACT BREAKDOWN (First 3 rows)")
        print("="*80)
        for idx in range(min(3, len(df))):
            row = df.iloc[idx]
            breakdown = calculator.get_feature_breakdown(row)
            print(f"\nRow {idx + 1}:")
            print("-" * 80)
            for feature, impact in breakdown.items():
                print(f"  {feature:30s}: {impact:>15,.0f}")
            print(f"  {'TOTAL CALCULATED':30s}: {row['dowry_calculated']:>15,.0f}")
            print(f"  {'ORIGINAL DOWRY':30s}: {row['dowry']:>15,.0f}")
    
    # Statistics
    print("\n" + "="*80)
    print("STATISTICS")
    print("="*80)
    print(f"Original dowry - Mean: ₹{df['dowry'].mean():,.0f}, Std: ₹{df['dowry'].std():,.0f}")
    print(f"Calculated dowry - Mean: ₹{df['dowry_calculated'].mean():,.0f}, Std: ₹{df['dowry_calculated'].std():,.0f}")
    print(f"Min calculated: ₹{df['dowry_calculated'].min():,.0f}")
    print(f"Max calculated: ₹{df['dowry_calculated'].max():,.0f}")
    
    # Save with new column
    print(f"\nSaving to {output_csv}...")
    df.to_csv(output_csv, index=False)
    print("✓ Complete!")
    
    return df


def replace_original_dowry(input_csv: str, output_csv: str):
    """
    Replace original dowry column with calculated values.
    
    Args:
        input_csv: Path to input CSV file
        output_csv: Path to output CSV file with replaced dowry
    """
    print(f"Loading data from {input_csv}...")
    df = pd.read_csv(input_csv)
    
    # Initialize calculator
    calculator = DowryWeightageCalculator()
    
    # Calculate and replace
    print("Replacing dowry amounts with calculated values...")
    df['dowry'] = df.apply(calculator.calculate_dowry, axis=1)
    df['dowry'] = df['dowry'].round().astype(int)
    
    # Save
    print(f"Saving to {output_csv}...")
    df.to_csv(output_csv, index=False)
    print("✓ Dowry column replaced successfully!")
    
    return df


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Apply weightage rules to dowry dataset')
    parser.add_argument('--input', type=str, default='../data/dowry.csv',
                        help='Input CSV file path')
    parser.add_argument('--output', type=str, default='../data/dowry_weighted.csv',
                        help='Output CSV file path')
    parser.add_argument('--replace', action='store_true',
                        help='Replace original dowry column instead of adding new column')
    parser.add_argument('--breakdown', action='store_true',
                        help='Show feature breakdown for first few rows')
    
    args = parser.parse_args()
    
    if args.replace:
        replace_original_dowry(args.input, args.output)
    else:
        apply_weightage_to_dataset(args.input, args.output, args.breakdown)
