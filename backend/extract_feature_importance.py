"""
Extract and display feature importances from trained models.
"""

import sys
from pathlib import Path

# Add scripts directory to path so we can unpickle objects from model.py
scripts_dir = Path(__file__).parent / 'scripts'
sys.path.insert(0, str(scripts_dir))

import joblib
import numpy as np
import pandas as pd

def extract_feature_importances():
    """Extract feature importances from trained models."""
    
    print("=" * 100)
    print("FEATURE IMPORTANCE ANALYSIS - DOWRY PREDICTION MODEL")
    print("=" * 100)
    
    # Load trained models
    models_path = Path('models/trained_models.pkl')
    preprocessor_path = Path('models/preprocessor.pkl')
    
    if not models_path.exists():
        print(f"❌ Error: {models_path} not found!")
        return
    
    if not preprocessor_path.exists():
        print(f"❌ Error: {preprocessor_path} not found!")
        return
    
    # Load the objects
    print("\n📂 Loading models and preprocessor...")
    models_data = joblib.load(models_path)
    preprocessor = joblib.load(preprocessor_path)
    
    # Inspect structure
    print(f"   Model data keys: {list(models_data.keys())}")
    
    # Get the actual models
    xgb_model = models_data.get('xgb_model')
    lgb_model = models_data.get('lgb_model')
    
    print("   ✓ Models loaded successfully")
    
    # Get feature names from preprocessor
    print("\n📋 Extracting feature names...")
    
    # Numerical features (keep original names)
    num_features = preprocessor.numerical_features.copy()
    
    # Categorical features (after one-hot encoding)
    cat_features = []
    if hasattr(preprocessor, 'preprocessor') and hasattr(preprocessor.preprocessor, 'named_transformers_'):
        cat_transformer = preprocessor.preprocessor.named_transformers_['cat']
        if hasattr(cat_transformer, 'named_steps') and 'encoder' in cat_transformer.named_steps:
            encoder = cat_transformer.named_steps['encoder']
            cat_features = encoder.get_feature_names_out(preprocessor.categorical_features).tolist()
    
    all_feature_names = num_features + cat_features
    
    print(f"   • Numerical features: {len(num_features)}")
    print(f"   • Categorical features (after encoding): {len(cat_features)}")
    print(f"   • Total features: {len(all_feature_names)}")
    
    # Extract XGBoost importances
    if xgb_model is not None and hasattr(xgb_model, 'feature_importances_'):
        print("\n" + "=" * 100)
        print("🎯 XGBoost MODEL - FEATURE IMPORTANCES")
        print("=" * 100)
        
        xgb_importances = xgb_model.feature_importances_
        
        # Create dataframe
        importance_df = pd.DataFrame({
            'Feature': all_feature_names[:len(xgb_importances)],
            'Importance': xgb_importances,
            'Percentage': (xgb_importances / xgb_importances.sum()) * 100
        })
        
        # Sort by importance
        importance_df = importance_df.sort_values('Importance', ascending=False)
        
        # Display top features
        print("\n📊 TOP 30 MOST IMPORTANT FEATURES:\n")
        print(f"{'Rank':<6} {'Feature':<50} {'Importance':<12} {'Percentage':<10}")
        print("-" * 100)
        
        for idx, row in importance_df.head(30).iterrows():
            rank = importance_df.index.get_loc(idx) + 1
            print(f"{rank:<6} {row['Feature']:<50} {row['Importance']:<12.6f} {row['Percentage']:>8.2f}%")
        
        # Summary statistics
        print("\n" + "=" * 100)
        print("📈 SUMMARY STATISTICS")
        print("=" * 100)
        print(f"Total features: {len(importance_df)}")
        print(f"Top 10 features contribute: {importance_df.head(10)['Percentage'].sum():.2f}% of total importance")
        print(f"Top 20 features contribute: {importance_df.head(20)['Percentage'].sum():.2f}% of total importance")
        print(f"Top 30 features contribute: {importance_df.head(30)['Percentage'].sum():.2f}% of total importance")
        
        # Feature categories
        print("\n" + "=" * 100)
        print("📂 FEATURE CATEGORIES (Top 30)")
        print("=" * 100)
        
        top_30 = importance_df.head(30)
        
        print("\n🔢 Numerical Features:")
        for idx, row in top_30[top_30['Feature'].isin(num_features)].iterrows():
            rank = importance_df.index.get_loc(idx) + 1
            print(f"   #{rank:<3} {row['Feature']:<45} {row['Percentage']:>6.2f}%")
        
        print("\n🏷️  Categorical Features (Encoded):")
        for idx, row in top_30[~top_30['Feature'].isin(num_features)].iterrows():
            rank = importance_df.index.get_loc(idx) + 1
            print(f"   #{rank:<3} {row['Feature']:<45} {row['Percentage']:>6.2f}%")
        
        # Save to CSV
        csv_path = 'models/feature_importances.csv'
        importance_df.to_csv(csv_path, index=False)
        print(f"\n💾 Full feature importance report saved to: {csv_path}")
    
    else:
        print("\n❌ Could not extract feature importances from XGBoost model")
        importance_df = None
    
    # Extract LightGBM importances
    if lgb_model is not None and hasattr(lgb_model, 'feature_importances_'):
        print("\n" + "=" * 100)
        print("🎯 LightGBM MODEL - FEATURE IMPORTANCES")
        print("=" * 100)
        
        lgb_importances = lgb_model.feature_importances_
        
        # Create dataframe
        lgb_importance_df = pd.DataFrame({
            'Feature': all_feature_names[:len(lgb_importances)],
            'Importance': lgb_importances,
            'Percentage': (lgb_importances / lgb_importances.sum()) * 100
        })
        
        # Sort by importance
        lgb_importance_df = lgb_importance_df.sort_values('Importance', ascending=False)
        
        # Display top features
        print("\n📊 TOP 30 MOST IMPORTANT FEATURES:\n")
        print(f"{'Rank':<6} {'Feature':<50} {'Importance':<12} {'Percentage':<10}")
        print("-" * 100)
        
        for idx, row in lgb_importance_df.head(30).iterrows():
            rank = lgb_importance_df.index.get_loc(idx) + 1
            print(f"{rank:<6} {row['Feature']:<50} {row['Importance']:<12.0f} {row['Percentage']:>8.2f}%")
        
        # Save to CSV
        csv_path = 'models/feature_importances_lightgbm.csv'
        lgb_importance_df.to_csv(csv_path, index=False)
        print(f"\n💾 LightGBM feature importance report saved to: {csv_path}")
        
        return importance_df


if __name__ == "__main__":
    importance_df = extract_feature_importances()
    print("\n" + "=" * 100)
    print("✅ ANALYSIS COMPLETE")
    print("=" * 100 + "\n")
