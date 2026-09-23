"""
Phase 2 Enhanced Data Preprocessing Pipeline

This module extends the original preprocessing pipeline with Phase 2 features:
1. All original domain transformation and preprocessing
2. Advanced feature engineering (23 new features)
3. Backward compatible with Phase 1 models
4. Optimized for both regression and classification tasks
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from typing import Tuple, Optional

from feature_engineering import Phase2FeatureEngineer


class Phase2PreprocessingPipeline:
    """
    Enhanced preprocessing pipeline with Phase 2 feature engineering.
    
    Combines domain transformation, feature engineering, and scikit-learn
    preprocessing into a single cohesive pipeline.
    """
    
    # Feature mapping for domain transformation
    FEATURE_MAPPING = {
        'dowry_amount': 'acquisition_price_inr',
        'income_per_month_inr': 'monthly_recurring_revenue',
        'land_acres': 'patents_held',
        'property_value_inr': 'infrastructure_value',
        'car_cost_inr': 'fleet_value',
        'gold_value_inr': 'liquid_cash_reserves',
        'father_income_inr': 'parent_company_revenue',
        'job_type': 'business_model',
        'family_status': 'brand_reputation',
        'caste': 'tech_sector',
        'taking_intoxicants': 'pending_lawsuits',
        'height_feet': 'years_in_operation',
        'is_first_marriage': 'is_first_acquisition'
    }
    
    # Categorical value mappings
    CATEGORICAL_VALUE_MAPPINGS = {
        'business_model': {
            'government': 'B2B_Enterprise',
            'private': 'B2C_Consumer'
        },
        'brand_reputation': {
            'respected': 'Industry_Leader',
            'average': 'Established',
            'notorious': 'Controversial'
        },
        'tech_sector': {
            'general': 'AI_DeepTech',
            'OBC': 'SaaS',
            'SC': 'E_commerce'
        },
        'pending_lawsuits': {
            'yes': 'yes',
            'no': 'no'
        },
        'is_first_acquisition': {
            'yes': 'yes',
            'no': 'no'
        }
    }
    
    def __init__(self, enable_phase2_features: bool = True):
        """
        Initialize the Phase 2 preprocessing pipeline.
        
        Parameters
        ----------
        enable_phase2_features : bool, default=True
            If True, applies Phase 2 feature engineering.
            If False, uses only Phase 1 features (backward compatible).
        """
        self.enable_phase2_features = enable_phase2_features
        self.feature_engineer = Phase2FeatureEngineer() if enable_phase2_features else None
        
        # Will be set during preprocessing
        self.numerical_features = None
        self.categorical_features = None
        self.target_column = None
        self.preprocessor = None
        self.new_phase2_features = []
        
    def create_derived_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Create derived features from raw dataset that Phase 2 engineering needs.
        
        Parameters
        ----------
        df : pd.DataFrame
            Raw dataset with original columns
            
        Returns
        -------
        pd.DataFrame
            DataFrame with derived features added
        """
        print("=" * 80)
        print("CREATING DERIVED FEATURES FROM RAW DATA")
        print("=" * 80)
        
        df = df.copy()
        
        # Education numerical mapping
        education_mapping = {
            'Below 10th': 1, '10th': 2, '12th': 3, 'Diploma': 4,
            'Bachelor': 5, 'Master': 6, 'Doctorate': 7
        }
        
        df['boy_edu_num'] = df['boy_education'].map(education_mapping)
        df['girl_edu_num'] = df['girl_education'].map(education_mapping)
        df['edu_difference'] = df['boy_edu_num'] - df['girl_edu_num']
        
        # Binary features
        df['is_govt_job'] = (df['boy_job_type'] == 'Government').astype(int)
        df['girl_prev_married'] = (df['girl_previous_marriage'].astype(str) != 'Never Married').astype(int)
        
        # Asset score (count of asset ownership)
        land_map = {'None': 0, 'Small': 1, 'Medium': 2, 'Large': 3}
        df['asset_score'] = (
            (df['own_house_boy'].astype(str) == 'Yes').astype(int) +
            df['land_ownership_boy'].map(land_map).fillna(0).astype(int) +
            df['land_ownership_girl'].map(land_map).fillna(0).astype(int)
        )
        
        print(f"  ✓ Created boy_edu_num, girl_edu_num (from education mapping)")
        print(f"  ✓ Created edu_difference")
        print(f"  ✓ Created is_govt_job (from boy_job_type)")
        print(f"  ✓ Created girl_prev_married (from girl_previous_marriage)")
        print(f"  ✓ Created asset_score (house + land ownership)")
        print("=" * 80)
        
        return df
    
    def apply_domain_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply semantic domain transformation from dowry to startup acquisition.
        
        Parameters
        ----------
        df : pd.DataFrame
            Original dataset with dowry-related column names
            
        Returns
        -------
        pd.DataFrame
            Transformed dataset with business-appropriate column names
        """
        print("=" * 80)
        print("APPLYING DOMAIN TRANSFORMATION")
        print("=" * 80)
        
        df_transformed = df.copy()
        
        # Rename columns
        df_transformed = df_transformed.rename(columns=self.FEATURE_MAPPING)
        
        # Transform categorical values
        for col, mapping in self.CATEGORICAL_VALUE_MAPPINGS.items():
            if col in df_transformed.columns:
                df_transformed[col] = df_transformed[col].map(mapping)
        
        print(f"  ✓ Transformed {len(self.FEATURE_MAPPING)} features")
        print(f"  ✓ Statistical properties preserved")
        print("=" * 80)
        
        return df_transformed
    
    def apply_feature_engineering(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply Phase 2 feature engineering if enabled.
        
        Parameters
        ----------
        df : pd.DataFrame
            DataFrame after domain transformation
            
        Returns
        -------
        pd.DataFrame
            DataFrame with Phase 2 features added (if enabled)
        """
        if not self.enable_phase2_features:
            print("\nPhase 2 features disabled - using Phase 1 features only")
            return df
        
        print("\nAPPLYING PHASE 2 FEATURE ENGINEERING")
        print("=" * 80)
        
        df_engineered = self.feature_engineer.create_all_phase2_features(df)
        self.new_phase2_features = self.feature_engineer.get_new_feature_names()
        
        print(f"  ✓ Created {len(self.new_phase2_features)} new features")
        print("=" * 80)
        
        return df_engineered
    
    def identify_feature_types(self, df: pd.DataFrame, target_col: str = 'acquisition_price_inr'):
        """
        Identify and segregate numerical and categorical features.
        
        Parameters
        ----------
        df : pd.DataFrame
            Transformed dataset
        target_col : str
            Name of target variable to exclude from features
        """
        self.target_column = target_col
        
        # DATA LEAKAGE PREVENTION: Exclude target and any dowry_category columns
        leakage_cols = [col for col in df.columns if 'dowry_category' in col.lower()]
        exclude_cols = [target_col] + leakage_cols
        
        if leakage_cols:
            print(f"\n⚠️  WARNING: Excluding data leakage columns: {leakage_cols}")
        
        # All columns except target and leakage columns
        feature_columns = [col for col in df.columns if col not in exclude_cols]
        
        # Separate by data type
        self.numerical_features = df[feature_columns].select_dtypes(
            include=['int64', 'float64']
        ).columns.tolist()
        
        self.categorical_features = df[feature_columns].select_dtypes(
            include=['object', 'category']
        ).columns.tolist()
        
        print("\nFEATURE SEGMENTATION")
        print("-" * 80)
        print(f"Numerical features: {len(self.numerical_features)}")
        print(f"Categorical features: {len(self.categorical_features)}")
        
        if self.enable_phase2_features:
            print(f"Phase 2 features: {len(self.new_phase2_features)}")
        
        print(f"Target variable: {target_col}")
        print("-" * 80)
    
    def build_preprocessing_pipeline(self):
        """
        Construct the ColumnTransformer with separate pipelines for numerical
        and categorical features.
        
        Returns
        -------
        ColumnTransformer
            Complete preprocessing pipeline
        """
        print("\nBUILDING PREPROCESSING PIPELINE")
        print("-" * 80)
        
        # NUMERICAL PIPELINE
        numerical_pipeline = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])
        
        print("Numerical Pipeline:")
        print("  1. SimpleImputer(strategy='median')")
        print("  2. StandardScaler()")
        
        # CATEGORICAL PIPELINE
        categorical_pipeline = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
            ('encoder', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'))
        ])
        
        print("\nCategorical Pipeline:")
        print("  1. SimpleImputer(strategy='constant')")
        print("  2. OneHotEncoder(drop='first', handle_unknown='ignore')")
        
        # COLUMN TRANSFORMER
        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', numerical_pipeline, self.numerical_features),
                ('cat', categorical_pipeline, self.categorical_features)
            ],
            remainder='drop'
        )
        
        print(f"\nColumnTransformer created:")
        print(f"  • Numerical: {len(self.numerical_features)} features")
        print(f"  • Categorical: {len(self.categorical_features)} features")
        print("-" * 80)
        
        return self.preprocessor
    
    def get_feature_names_after_preprocessing(self):
        """
        Extract feature names after one-hot encoding.
        
        Returns
        -------
        list
            Names of all features after preprocessing
        """
        # Numerical features stay the same
        num_features = self.numerical_features.copy()
        
        # Get encoded categorical feature names
        if hasattr(self.preprocessor, 'named_transformers_'):
            cat_encoder = self.preprocessor.named_transformers_['cat']['encoder']
            cat_features = cat_encoder.get_feature_names_out(self.categorical_features).tolist()
        else:
            cat_features = []
        
        return num_features + cat_features


def load_and_preprocess_data_v2(
    csv_path: str, 
    test_size: float = 0.2, 
    random_state: int = 42,
    enable_phase2_features: bool = True,
    target_col: str = 'dowry_amount'
) -> Tuple:
    """
    Complete Phase 2 data loading and preprocessing workflow.
    
    Parameters
    ----------
    csv_path : str
        Path to the CSV dataset
    test_size : float, default=0.2
        Proportion of data for testing
    random_state : int, default=42
        Random seed for reproducibility
    enable_phase2_features : bool, default=True
        Enable Phase 2 feature engineering
    target_col : str, default='dowry_amount'
        Target column name (use 'dowry_class' for classification)
        
    Returns
    -------
    tuple
        (X_train, X_test, y_train, y_test, preprocessor_obj, df_transformed)
    """
    print("\n" + "=" * 80)
    print("PHASE 2 DATA PREPROCESSING PIPELINE")
    print("=" * 80)
    print(f"Phase 2 Features: {'ENABLED' if enable_phase2_features else 'DISABLED'}")
    print(f"Target: {target_col}")
    print("=" * 80)
    
    # 1. LOAD DATA
    print("\n[STEP 1] Loading dataset...")
    df = pd.read_csv(csv_path)
    print(f"  ✓ Loaded {len(df):,} records with {len(df.columns)} columns")
    
    # 2. CREATE DERIVED FEATURES
    print("\n[STEP 2] Creating derived features...")
    preprocessor_obj = Phase2PreprocessingPipeline(enable_phase2_features=enable_phase2_features)
    df = preprocessor_obj.create_derived_features(df)
    
    # 3. DOMAIN TRANSFORMATION
    print("\n[STEP 3] Applying domain transformation...")
    df_transformed = preprocessor_obj.apply_domain_transformation(df)
    # Resolve target_col to its post-rename name (if it was renamed by FEATURE_MAPPING)
    target_col = preprocessor_obj.FEATURE_MAPPING.get(target_col, target_col)
    
    # 4. FEATURE ENGINEERING (Phase 2)
    print("\n[STEP 4] Feature engineering...")
    df_transformed = preprocessor_obj.apply_feature_engineering(df_transformed)
    
    # 5. FEATURE IDENTIFICATION
    print("\n[STEP 5] Identifying feature types...")
    preprocessor_obj.identify_feature_types(df_transformed, target_col=target_col)
    
    # 6. BUILD PIPELINE
    print("\n[STEP 6] Building preprocessing pipeline...")
    preprocessor_obj.build_preprocessing_pipeline()
    
    # 7. TRAIN-TEST SPLIT
    print("\n[STEP 7] Splitting data...")
    
    # DATA LEAKAGE PREVENTION: Remove all dowry_category columns
    leakage_cols = [col for col in df_transformed.columns if 'dowry_category' in col.lower()]
    if leakage_cols:
        print(f"\n⚠️  WARNING: Removing data leakage columns: {leakage_cols}")
        df_transformed = df_transformed.drop(columns=leakage_cols)
        print(f"  ✓ Leakage columns removed")
    else:
        print(f"  ✓ No leakage columns detected")
    
    # Check if target exists
    if target_col not in df_transformed.columns:
        print(f"\n⚠ Warning: Target column '{target_col}' not found!")
        print(f"Available columns: {df_transformed.columns.tolist()}")
        raise ValueError(f"Target column '{target_col}' not in dataframe")
    
    X = df_transformed.drop(columns=[target_col])
    y = df_transformed[target_col]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y if target_col == 'dowry_class' else None
    )
    
    print(f"  ✓ Training set: {len(X_train):,} samples")
    print(f"  ✓ Test set: {len(X_test):,} samples")
    print(f"  ✓ Split ratio: {(1-test_size)*100:.0f}% train / {test_size*100:.0f}% test")
    
    # 7. SUMMARY
    print("\n" + "=" * 80)
    print("PREPROCESSING PIPELINE READY")
    print("=" * 80)
    print(f"Total features: {len(X.columns)}")
    
    if enable_phase2_features:
        print(f"  • Phase 1 features: {len(X.columns) - len(preprocessor_obj.new_phase2_features)}")
        print(f"  • Phase 2 features: {len(preprocessor_obj.new_phase2_features)}")
    
    print(f"Target variable: {target_col}")
    print("=" * 80 + "\n")
    
    return X_train, X_test, y_train, y_test, preprocessor_obj, df_transformed


def create_classification_target(df: pd.DataFrame, 
                                 source_col: str = 'acquisition_price_inr',
                                 bins: Optional[list] = None,
                                 labels: Optional[list] = None) -> pd.DataFrame:
    """
    Create classification target from continuous dowry/acquisition amounts.
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with continuous target
    source_col : str
        Column to bin into classes
    bins : list, optional
        Bin edges. Default: [0, 200000, 400000, 600000, inf]
    labels : list, optional
        Class labels. Default: ['Low', 'Medium', 'High', 'Very High']
        
    Returns
    -------
    pd.DataFrame
        DataFrame with 'dowry_class' column added
    """
    if bins is None:
        bins = [0, 200000, 400000, 600000, float('inf')]
    
    if labels is None:
        labels = ['Low', 'Medium', 'High', 'Very High']
    
    df = df.copy()
    df['dowry_class'] = pd.cut(df[source_col], bins=bins, labels=labels)
    
    print(f"\nCreated classification target 'dowry_class':")
    print(df['dowry_class'].value_counts().sort_index())
    print(f"\nClass distribution:")
    print(df['dowry_class'].value_counts(normalize=True).sort_index())
    
    return df


if __name__ == "__main__":
    """
    Demonstration of Phase 2 preprocessing pipeline.
    """
    print("\n" + "=" * 80)
    print("PHASE 2 PREPROCESSING PIPELINE - DEMONSTRATION")
    print("=" * 80)
    
    # Note: This assumes the dataset exists
    # Adjust the path as needed
    try:
        # Test with Phase 2 features enabled (regression)
        print("\n### TEST 1: Regression with Phase 2 Features ###")
        X_train, X_test, y_train, y_test, preprocessor, df = load_and_preprocess_data_v2(
            csv_path='../../data/dowry_dataset.csv',
            enable_phase2_features=True,
            target_col='dowry_amount'
        )
        
        print(f"\nResult shapes:")
        print(f"  X_train: {X_train.shape}")
        print(f"  X_test: {X_test.shape}")
        print(f"  y_train: {y_train.shape}")
        print(f"  y_test: {y_test.shape}")
        
        # Fit and transform
        print("\nFitting preprocessor...")
        X_train_transformed = preprocessor.preprocessor.fit_transform(X_train)
        X_test_transformed = preprocessor.preprocessor.transform(X_test)
        
        print(f"  ✓ X_train_transformed: {X_train_transformed.shape}")
        print(f"  ✓ X_test_transformed: {X_test_transformed.shape}")
        
        # Test with Phase 2 features disabled (backward compatibility)
        print("\n\n### TEST 2: Regression with Phase 1 Features Only ###")
        X_train_p1, X_test_p1, y_train_p1, y_test_p1, preprocessor_p1, df_p1 = load_and_preprocess_data_v2(
            csv_path='../../data/dowry_dataset.csv',
            enable_phase2_features=False,
            target_col='dowry_amount'
        )
        
        print(f"\nPhase 1 shapes:")
        print(f"  X_train: {X_train_p1.shape}")
        print(f"  X_test: {X_test_p1.shape}")
        
        print("\n" + "=" * 80)
        print("DEMONSTRATION COMPLETE")
        print("=" * 80)
        print("\nComparison:")
        print(f"  Phase 1 features: {X_train_p1.shape[1]}")
        print(f"  Phase 2 features: {X_train.shape[1]}")
        print(f"  New features added: {X_train.shape[1] - X_train_p1.shape[1]}")
        print("=" * 80 + "\n")
        
    except FileNotFoundError:
        print("\n⚠ Dataset not found. Skipping demonstration.")
        print("To run demonstration, ensure dataset is at:")
        print("  ../../data/dowry_dataset.csv")
        print("=" * 80 + "\n")
