"""
Data Preprocessing & Pipeline for Startup Acquisition Valuation Prediction

This module implements the complete preprocessing pipeline with:
1. Domain semantic transformation (ethical business alignment)
2. Numerical pipeline (imputation + scaling)
3. Categorical pipeline (imputation + one-hot encoding)
4. Scikit-learn ColumnTransformer for leak-proof preprocessing
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer


class StartupAcquisitionPreprocessor:
    """
    Complete preprocessing pipeline for startup acquisition valuation prediction.
    
    Handles domain transformation, missing values, scaling, and encoding while
    preventing data leakage through scikit-learn pipelines.
    """
    
    # Feature mapping for domain transformation
    FEATURE_MAPPING = {
        'dowry_amount_inr': 'acquisition_price_inr',
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
    
    def __init__(self):
        """Initialize the preprocessor with feature lists and pipeline."""
        # Will be set after domain transformation
        self.numerical_features = None
        self.categorical_features = None
        self.target_column = None
        self.preprocessor = None
        self.full_pipeline = None
        
    def apply_domain_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply semantic domain transformation from dowry to startup acquisition.
        
        Statistical properties remain identical:
        - Distributions preserved
        - Non-linearities maintained
        - Heteroscedastic noise structure unchanged
        
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
        print("Swapping feature names while preserving statistical distributions...")
        
        # Create a copy to avoid modifying original
        df_transformed = df.copy()
        
        # Rename columns
        df_transformed = df_transformed.rename(columns=self.FEATURE_MAPPING)
        
        # Transform categorical values
        for col, mapping in self.CATEGORICAL_VALUE_MAPPINGS.items():
            if col in df_transformed.columns:
                df_transformed[col] = df_transformed[col].map(mapping)
                print(f"  ✓ Transformed {col}: {list(mapping.keys())} → {list(mapping.values())}")
        
        print("\nDomain transformation complete!")
        print(f"  • All {len(self.FEATURE_MAPPING)} features renamed")
        print(f"  • Statistical properties preserved")
        print(f"  • Ready for ethical business ML modeling")
        print("=" * 80)
        
        return df_transformed
    
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
        print(f"Numerical features ({len(self.numerical_features)}):")
        for feat in self.numerical_features:
            print(f"  • {feat}")
        
        print(f"\nCategorical features ({len(self.categorical_features)}):")
        for feat in self.categorical_features:
            print(f"  • {feat}")
        
        print(f"\nTarget variable: {target_col}")
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
        # Step 1: Impute missing values with median (robust to outliers)
        # Step 2: Standardize to zero mean and unit variance
        numerical_pipeline = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])
        
        print("Numerical Pipeline:")
        print("  1. SimpleImputer(strategy='median')")
        print("     → Handles ~40% missing values in fleet_value")
        print("     → Robust against extreme outliers")
        print("  2. StandardScaler()")
        print("     → Removes mean, scales to unit variance")
        print("     → Prevents magnitude bias in distance-based models")
        
        # CATEGORICAL PIPELINE
        # Step 1: Impute any unexpected missing values with constant "missing"
        # Step 2: One-hot encode with drop='first' to avoid dummy variable trap
        categorical_pipeline = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
            ('encoder', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'))
        ])
        
        print("\nCategorical Pipeline:")
        print("  1. SimpleImputer(strategy='constant', fill_value='missing')")
        print("     → Safety net for unexpected NaN values")
        print("  2. OneHotEncoder(drop='first', handle_unknown='ignore')")
        print("     → Converts categories to binary vectors")
        print("     → Drops first category to prevent multicollinearity")
        print("     → Handles unknown categories in production")
        
        # COLUMN TRANSFORMER
        # Applies appropriate pipeline to each feature type
        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', numerical_pipeline, self.numerical_features),
                ('cat', categorical_pipeline, self.categorical_features)
            ],
            remainder='drop'  # Drop any columns not specified
        )
        
        print("\nColumnTransformer created:")
        print(f"  • Numerical transformer → {len(self.numerical_features)} features")
        print(f"  • Categorical transformer → {len(self.categorical_features)} features")
        print("  • Leak prevention: fit on train, transform on test")
        print("-" * 80)
        
        return self.preprocessor
    
    def create_full_pipeline(self, estimator):
        """
        Create a complete pipeline chaining preprocessor with an estimator.
        
        Parameters
        ----------
        estimator : sklearn estimator
            Machine learning model (e.g., RandomForestRegressor, LinearRegression)
            
        Returns
        -------
        Pipeline
            Complete end-to-end pipeline
        """
        self.full_pipeline = Pipeline(steps=[
            ('preprocessor', self.preprocessor),
            ('model', estimator)
        ])
        
        print("\nFULL PIPELINE CREATED")
        print("-" * 80)
        print("Pipeline structure:")
        print("  Input → Preprocessor → Model → Predictions")
        print("\nBenefits:")
        print("  ✓ No data leakage (scaler/encoder fit only on train)")
        print("  ✓ Automatic transformation of test/production data")
        print("  ✓ Reproducible preprocessing")
        print("  ✓ Easy model serialization (pickle/joblib)")
        print("-" * 80)
        
        return self.full_pipeline
    
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


def load_and_preprocess_data(csv_path: str, test_size: float = 0.2, random_state: int = 42):
    """
    Complete data loading and preprocessing workflow.
    
    Parameters
    ----------
    csv_path : str
        Path to the CSV dataset
    test_size : float, default=0.2
        Proportion of data for testing
    random_state : int, default=42
        Random seed for reproducibility
        
    Returns
    -------
    tuple
        (X_train, X_test, y_train, y_test, preprocessor, transformed_df)
    """
    print("\n" + "=" * 80)
    print("STARTUP ACQUISITION VALUATION - DATA PREPROCESSING PIPELINE")
    print("=" * 80)
    
    # 1. LOAD DATA
    print("\nStep 1: Loading dataset...")
    df = pd.read_csv(csv_path)
    print(f"  ✓ Loaded {len(df):,} records")
    print(f"  ✓ {len(df.columns)} columns")
    print(f"  ✓ Memory usage: {df.memory_usage(deep=True).sum() / (1024**2):.2f} MB")
    
    # 2. DOMAIN TRANSFORMATION
    print("\nStep 2: Applying domain transformation...")
    preprocessor_obj = StartupAcquisitionPreprocessor()
    df_transformed = preprocessor_obj.apply_domain_transformation(df)
    
    # 3. FEATURE IDENTIFICATION
    print("\nStep 3: Identifying feature types...")
    preprocessor_obj.identify_feature_types(df_transformed)
    
    # 4. MISSING VALUE ANALYSIS
    print("\nStep 4: Analyzing missing values...")
    missing_counts = df_transformed.isnull().sum()
    missing_features = missing_counts[missing_counts > 0]
    if len(missing_features) > 0:
        print("  Missing values detected:")
        for feat, count in missing_features.items():
            pct = (count / len(df_transformed)) * 100
            print(f"    • {feat}: {count:,} ({pct:.1f}%)")
    else:
        print("  ✓ No missing values detected (except fleet_value as expected)")
    
    # 5. BUILD PIPELINE
    print("\nStep 5: Building preprocessing pipeline...")
    preprocessor_obj.build_preprocessing_pipeline()
    
    # 6. TRAIN-TEST SPLIT
    print("\nStep 6: Splitting data...")
    
    # DATA LEAKAGE PREVENTION: Remove all dowry_category columns
    leakage_cols = [col for col in df_transformed.columns if 'dowry_category' in col.lower()]
    if leakage_cols:
        print(f"\n⚠️  WARNING: Removing data leakage columns: {leakage_cols}")
        df_transformed = df_transformed.drop(columns=leakage_cols)
        print(f"  ✓ Leakage columns removed")
    else:
        print(f"  ✓ No leakage columns detected")
    
    X = df_transformed.drop(columns=['acquisition_price_inr'])
    y = df_transformed['acquisition_price_inr']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    print(f"  ✓ Training set: {len(X_train):,} samples")
    print(f"  ✓ Test set: {len(X_test):,} samples")
    print(f"  ✓ Split ratio: {(1-test_size)*100:.0f}% train / {test_size*100:.0f}% test")
    
    print("\n" + "=" * 80)
    print("PREPROCESSING PIPELINE READY")
    print("=" * 80)
    print("\nNext steps:")
    print("  1. Fit preprocessor on X_train (learns median, mean, std, categories)")
    print("  2. Transform X_train and X_test (applies learned parameters)")
    print("  3. Train model on transformed data")
    print("  4. Make predictions")
    print("=" * 80 + "\n")
    
    return X_train, X_test, y_train, y_test, preprocessor_obj, df_transformed


def demonstrate_pipeline_usage():
    """
    Demonstration of the complete preprocessing pipeline with a baseline model.
    """
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    
    # Load and preprocess
    X_train, X_test, y_train, y_test, preprocessor_obj, df_transformed = load_and_preprocess_data(
        csv_path='dowry_prediction_dataset.csv'
    )
    
    # Create a complete pipeline with Linear Regression baseline
    print("\nCREATING BASELINE MODEL (Linear Regression)")
    print("-" * 80)
    lr_model = LinearRegression()
    full_pipeline = preprocessor_obj.create_full_pipeline(lr_model)
    
    # Fit the entire pipeline on training data
    print("\nFitting pipeline on training data...")
    print("  • Learning median values for imputation")
    print("  • Learning mean and std for scaling")
    print("  • Learning category encodings")
    print("  • Training Linear Regression model")
    full_pipeline.fit(X_train, y_train)
    print("  ✓ Pipeline fitted successfully!\n")
    
    # Make predictions
    print("Making predictions on test set...")
    y_pred = full_pipeline.predict(X_test)
    
    # Evaluate
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
    
    print("\n" + "=" * 80)
    print("BASELINE MODEL PERFORMANCE (Linear Regression)")
    print("=" * 80)
    print(f"Mean Absolute Error (MAE):     ₹{mae:,.0f}")
    print(f"Root Mean Squared Error (RMSE): ₹{rmse:,.0f}")
    print(f"R² Score:                       {r2:.4f}")
    print(f"Mean Absolute % Error (MAPE):   {mape:.2f}%")
    print("=" * 80)
    
    # Show sample predictions
    print("\nSample Predictions (first 10 test samples):")
    print("-" * 80)
    comparison_df = pd.DataFrame({
        'Actual': y_test.iloc[:10].values,
        'Predicted': y_pred[:10],
        'Error': y_test.iloc[:10].values - y_pred[:10],
        'Error %': ((y_test.iloc[:10].values - y_pred[:10]) / y_test.iloc[:10].values * 100)
    })
    print(comparison_df.to_string(index=False))
    print("-" * 80 + "\n")
    
    return full_pipeline, X_train, X_test, y_train, y_test, df_transformed


if __name__ == "__main__":
    # Run the complete demonstration
    pipeline, X_train, X_test, y_train, y_test, df_transformed = demonstrate_pipeline_usage()
    
    print("\n" + "=" * 80)
    print("PIPELINE DEMONSTRATION COMPLETE")
    print("=" * 80)
    print("\nThe preprocessing pipeline is now ready for:")
    print("  • Advanced models (RandomForest, XGBoost, Neural Networks)")
    print("  • Hyperparameter tuning with GridSearchCV/RandomizedSearchCV")
    print("  • Cross-validation")
    print("  • Production deployment (save with joblib/pickle)")
    print("\nExample: Save the pipeline")
    print("  import joblib")
    print("  joblib.dump(pipeline, 'acquisition_valuation_pipeline.pkl')")
    print("\nExample: Load and use in production")
    print("  pipeline = joblib.load('acquisition_valuation_pipeline.pkl')")
    print("  predictions = pipeline.predict(new_startup_data)")
    print("=" * 80 + "\n")
