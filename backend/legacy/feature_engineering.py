"""
Phase 2 Feature Engineering Module

This module implements advanced feature engineering including:
1. High-value interaction features (salary × education, NRI interactions, etc.)
2. Non-linear transformations (log transforms, binning)
3. Composite scores (social preference, economic strength)

These features are designed to:
- Improve regression R² from 0.90 to ≥0.915
- Boost "High" class F1 score from ~0.53 to ≥0.62
- Better capture complex relationships in the data
"""

import pandas as pd
import numpy as np
from typing import Tuple


class Phase2FeatureEngineer:
    """
    Advanced feature engineering for Phase 2 model improvements.
    
    Creates interaction features, composite scores, and non-linear transformations
    to enhance model predictive power.
    """
    
    def __init__(self):
        """Initialize the feature engineer."""
        self.new_feature_names = []
        
    def create_salary_education_interactions(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Create salary × education interaction features.
        
        Captures the premium of educated high earners - a critical signal
        for both regression accuracy and classification boundaries.
        
        Parameters
        ----------
        df : pd.DataFrame
            DataFrame with boy_salary and boy_edu_num columns
            
        Returns
        -------
        pd.DataFrame
            DataFrame with new interaction features added
        """
        df = df.copy()
        
        # Boy salary × education (main interaction)
        df['boy_salary_x_edu'] = df['boy_salary'] * df['boy_edu_num']
        
        # Girl salary × education
        df['girl_salary_x_edu'] = df['girl_salary'] * df['girl_edu_num']
        
        # Education gap × boy salary (mismatch penalty/bonus)
        df['edu_gap_x_salary'] = df['edu_difference'] * df['boy_salary']
        
        self.new_feature_names.extend([
            'boy_salary_x_edu', 
            'girl_salary_x_edu',
            'edu_gap_x_salary'
        ])
        
        return df
    
    def create_nri_interactions(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Create NRI (working abroad) interaction features.
        
        NRI status significantly impacts dowry amounts, especially when
        combined with high salary or government jobs.
        
        Parameters
        ----------
        df : pd.DataFrame
            DataFrame with working_abroad, is_govt_job, boy_salary columns
            
        Returns
        -------
        pd.DataFrame
            DataFrame with NRI interaction features added
        """
        df = df.copy()
        
        # NRI × Government job (rare but high-value combination)
        df['nri_x_govt'] = (
            (df['working_abroad'] == 'Yes').astype(int) * 
            df['is_govt_job']
        )
        
        # NRI × Salary (salary matters more when working abroad)
        df['nri_x_salary'] = np.where(
            df['working_abroad'] == 'Yes',
            df['boy_salary'],
            0
        )
        
        # High education NRI (elite signal)
        df['high_edu_nri'] = (
            (df['boy_edu_num'] >= 6) & 
            (df['working_abroad'] == 'Yes')
        ).astype(int)
        
        self.new_feature_names.extend([
            'nri_x_govt',
            'nri_x_salary',
            'high_edu_nri'
        ])
        
        return df
    
    def create_wealth_interactions(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Create wealth-related interaction features.
        
        Combines asset ownership with income to create a comprehensive
        wealth signal.
        
        Parameters
        ----------
        df : pd.DataFrame
            DataFrame with asset_score and family_income_boy columns
            
        Returns
        -------
        pd.DataFrame
            DataFrame with wealth interaction features added
        """
        df = df.copy()
        
        # Asset score × Family income (combined wealth signal)
        df['asset_x_income'] = df['asset_score'] * df['family_income_boy']
        
        # Total wealth score (composite)
        df['total_wealth_score'] = (
            df['boy_salary'] * 0.3 +
            df['family_income_boy'] * 0.3 +
            df['asset_score'] * 100000 * 0.4  # Scale asset score
        )
        
        self.new_feature_names.extend([
            'asset_x_income',
            'total_wealth_score'
        ])
        
        return df
    
    def create_demographic_interactions(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Create demographic interaction features.
        
        Captures effects of age gaps, previous marriages, and other
        demographic factors.
        
        Parameters
        ----------
        df : pd.DataFrame
            DataFrame with demographic columns
            
        Returns
        -------
        pd.DataFrame
            DataFrame with demographic interaction features added
        """
        df = df.copy()
        
        # Previous marriage × age (older previously married individuals)
        df['prev_married_x_age'] = df['girl_prev_married'] * df['girl_age']
        
        # Age gap × boy salary (larger gaps may require higher dowry)
        df['age_gap_x_salary'] = df['age_difference'] * df['boy_salary']
        
        # Physical disability penalty
        df['disability_penalty'] = (
            df['physical_disability_girl'] == 'Yes'
        ).astype(int) * df['boy_salary'] * 0.5
        
        self.new_feature_names.extend([
            'prev_married_x_age',
            'age_gap_x_salary',
            'disability_penalty'
        ])
        
        return df
    
    def create_log_transformations(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply log transformations to handle skewed distributions.
        
        Log transforms help models handle non-linear relationships and
        reduce the impact of extreme outliers.
        
        Parameters
        ----------
        df : pd.DataFrame
            DataFrame with salary and income columns
            
        Returns
        -------
        pd.DataFrame
            DataFrame with log-transformed features added
        """
        df = df.copy()
        
        # Log transform key financial features
        df['log_boy_salary'] = np.log1p(df['boy_salary'])
        df['log_girl_salary'] = np.log1p(df['girl_salary'])
        df['log_family_income_boy'] = np.log1p(df['family_income_boy'])
        df['log_family_income_girl'] = np.log1p(df['family_income_girl'])
        
        self.new_feature_names.extend([
            'log_boy_salary',
            'log_girl_salary',
            'log_family_income_boy',
            'log_family_income_girl'
        ])
        
        return df
    
    def create_binned_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Create binned categorical versions of continuous features.
        
        Binning can help capture non-linear effects and threshold behaviors.
        
        Parameters
        ----------
        df : pd.DataFrame
            DataFrame with continuous features to bin
            
        Returns
        -------
        pd.DataFrame
            DataFrame with binned features added
        """
        df = df.copy()
        
        # Salary bins
        df['boy_salary_bin'] = pd.cut(
            df['boy_salary'],
            bins=[0, 30000, 60000, 100000, float('inf')],
            labels=['Low', 'Medium', 'High', 'Very_High']
        )
        
        df['girl_salary_bin'] = pd.cut(
            df['girl_salary'],
            bins=[0, 20000, 40000, 60000, float('inf')],
            labels=['Low', 'Medium', 'High', 'Very_High']
        )
        
        # Family income bins
        df['family_income_boy_bin'] = pd.cut(
            df['family_income_boy'],
            bins=[0, 50000, 100000, 200000, float('inf')],
            labels=['Low', 'Medium', 'High', 'Very_High']
        )
        
        # Age gap categories
        df['age_gap_category'] = pd.cut(
            df['age_difference'],
            bins=[0, 3, 7, float('inf')],
            labels=['Small', 'Medium', 'Large']
        )
        
        self.new_feature_names.extend([
            'boy_salary_bin',
            'girl_salary_bin',
            'family_income_boy_bin',
            'age_gap_category'
        ])
        
        return df
    
    def create_social_preference_score(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Create composite social preference score.
        
        Captures non-economic factors that influence dowry amounts
        (skin tone, previous marriage status, disability status).
        
        Parameters
        ----------
        df : pd.DataFrame
            DataFrame with social feature columns
            
        Returns
        -------
        pd.DataFrame
            DataFrame with social preference score added
        """
        df = df.copy()
        
        # Social preference score (higher = more desirable socially)
        df['social_preference_score'] = (
            (df['girl_skin_tone'] == 'Fair').astype(int) * 2 +
            (df['girl_skin_tone'] == 'Wheatish').astype(int) * 1 +
            (df['physical_disability_girl'] == 'No').astype(int) * 1 +
            (df['girl_prev_married'] == 0).astype(int) * 2
        )
        
        # Boy's desirability score
        df['boy_desirability_score'] = (
            (df['boy_skin_tone'] == 'Fair').astype(int) * 1 +
            df['is_govt_job'] * 2 +
            (df['working_abroad'] == 'Yes').astype(int) * 2 +
            (df['boy_edu_num'] / 10) * 1  # Normalized education
        )
        
        self.new_feature_names.extend([
            'social_preference_score',
            'boy_desirability_score'
        ])
        
        return df
    
    def create_economic_strength_score(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Create composite economic strength score.
        
        Weighted combination of education, job type, NRI status, and assets
        to capture overall economic position.
        
        Parameters
        ----------
        df : pd.DataFrame
            DataFrame with economic feature columns
            
        Returns
        -------
        pd.DataFrame
            DataFrame with economic strength score added
        """
        df = df.copy()
        
        # Economic strength score (normalized 0-100)
        df['economic_strength'] = (
            (df['boy_edu_num'] / 10) * 30 +  # Education (0-30)
            df['is_govt_job'] * 25 +  # Government job bonus (0 or 25)
            (df['working_abroad'] == 'Yes').astype(int) * 25 +  # NRI bonus (0 or 25)
            (df['asset_score'] / 5) * 20  # Assets (0-20, assuming max 5 assets)
        )
        
        # Girl's economic independence score
        df['girl_economic_independence'] = (
            (df['girl_salary'] / 100000) * 50 +  # Normalize salary
            (df['girl_edu_num'] / 10) * 30 +  # Education
            (df['girl_prev_married'] == 0).astype(int) * 20  # First marriage
        )
        
        self.new_feature_names.extend([
            'economic_strength',
            'girl_economic_independence'
        ])
        
        return df
    
    def create_all_phase2_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply all Phase 2 feature engineering in sequence.
        
        Parameters
        ----------
        df : pd.DataFrame
            Input DataFrame with base features
            
        Returns
        -------
        pd.DataFrame
            DataFrame with all Phase 2 features added
        """
        print("=" * 80)
        print("PHASE 2 FEATURE ENGINEERING")
        print("=" * 80)
        print(f"Starting features: {len(df.columns)}")
        
        # Reset new features list
        self.new_feature_names = []
        
        # Apply all feature engineering steps
        df = self.create_salary_education_interactions(df)
        print(f"  ✓ Salary × Education interactions: {3} features")
        
        df = self.create_nri_interactions(df)
        print(f"  ✓ NRI interactions: {3} features")
        
        df = self.create_wealth_interactions(df)
        print(f"  ✓ Wealth interactions: {2} features")
        
        df = self.create_demographic_interactions(df)
        print(f"  ✓ Demographic interactions: {3} features")
        
        df = self.create_log_transformations(df)
        print(f"  ✓ Log transformations: {4} features")
        
        df = self.create_binned_features(df)
        print(f"  ✓ Binned features: {4} features")
        
        df = self.create_social_preference_score(df)
        print(f"  ✓ Social preference scores: {2} features")
        
        df = self.create_economic_strength_score(df)
        print(f"  ✓ Economic strength scores: {2} features")
        
        print(f"\nTotal new features created: {len(self.new_feature_names)}")
        print(f"Final feature count: {len(df.columns)}")
        print("=" * 80)
        
        return df
    
    def get_new_feature_names(self) -> list:
        """
        Get list of all newly created feature names.
        
        Returns
        -------
        list
            Names of all Phase 2 features
        """
        return self.new_feature_names


def apply_phase2_feature_engineering(df: pd.DataFrame) -> Tuple[pd.DataFrame, list]:
    """
    Convenience function to apply all Phase 2 feature engineering.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame with base features
        
    Returns
    -------
    tuple
        (transformed_df, new_feature_names)
    """
    engineer = Phase2FeatureEngineer()
    df_transformed = engineer.create_all_phase2_features(df)
    new_features = engineer.get_new_feature_names()
    
    return df_transformed, new_features


if __name__ == "__main__":
    """
    Demonstration of Phase 2 feature engineering.
    """
    print("\n" + "=" * 80)
    print("PHASE 2 FEATURE ENGINEERING - DEMONSTRATION")
    print("=" * 80)
    
    # Create sample data
    sample_data = pd.DataFrame({
        'boy_salary': [50000, 80000, 120000],
        'girl_salary': [30000, 40000, 60000],
        'boy_edu_num': [6, 8, 9],
        'girl_edu_num': [5, 7, 8],
        'edu_difference': [1, 1, 1],
        'family_income_boy': [100000, 150000, 200000],
        'family_income_girl': [80000, 100000, 120000],
        'working_abroad': ['No', 'Yes', 'Yes'],
        'is_govt_job': [0, 1, 1],
        'asset_score': [2, 3, 4],
        'girl_prev_married': [0, 0, 1],
        'girl_age': [25, 27, 30],
        'age_difference': [3, 5, 8],
        'physical_disability_girl': ['No', 'No', 'Yes'],
        'girl_skin_tone': ['Fair', 'Wheatish', 'Dark'],
        'boy_skin_tone': ['Fair', 'Fair', 'Wheatish']
    })
    
    print("\nOriginal features:")
    print(sample_data.columns.tolist())
    
    # Apply feature engineering
    df_engineered, new_features = apply_phase2_feature_engineering(sample_data)
    
    print("\n\nNew features created:")
    for i, feat in enumerate(new_features, 1):
        print(f"{i:2d}. {feat}")
    
    print("\n\nSample of engineered features (first row):")
    print("-" * 80)
    for feat in new_features[:10]:  # Show first 10 new features
        if feat in df_engineered.columns:
            print(f"{feat:30s}: {df_engineered[feat].iloc[0]}")
    
    print("\n" + "=" * 80)
    print("DEMONSTRATION COMPLETE")
    print("=" * 80)
    print("\nThese features will significantly improve:")
    print("  • Regression R² (target: ≥0.915)")
    print("  • Classification accuracy (target: ≥0.76)")
    print("  • 'High' class F1 score (target: ≥0.62)")
    print("=" * 80 + "\n")
