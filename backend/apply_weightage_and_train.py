"""
Apply Weightage and Train Models
=================================

This script:
1. Applies weightage rules to the dowry.csv dataset
2. Trains the machine learning models with the weighted data
3. Saves the trained models and performance reports

Usage:
    python apply_weightage_and_train.py
"""

import sys
from pathlib import Path

# Fix for Windows UnicodeEncodeError (cp1252) when printing emojis
# This MUST execute before any print() statements.
if (sys.stdout.encoding or '').lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
if (getattr(sys.stderr, 'encoding', None) or '').lower() not in ('', 'utf-8'):
    try:
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Add scripts directory to path
scripts_dir = Path(__file__).parent / 'scripts'
sys.path.insert(0, str(scripts_dir))

from apply_weightage import replace_original_dowry
from model import run_complete_pipeline


def main():
    """Main execution function."""
    
    print("\n" + "=" * 90)
    print(" " * 25 + "DOWRY PREDICTION MODEL TRAINING")
    print("=" * 90)
    
    # Step 1: Apply weightage to dataset
    print("\n" + "=" * 90)
    print("STEP 1: APPLYING WEIGHTAGE RULES TO DATASET")
    print("=" * 90)
    
    input_csv = './data/dowry.csv'
    output_csv = './data/dowry_dataset.csv'
    
    try:
        print(f"\nProcessing {input_csv}...")
        replace_original_dowry(input_csv, output_csv)
        print(f"\n✅ Weightage applied successfully!")
        print(f"   Output saved to: {output_csv}")
    except Exception as e:
        print(f"\n❌ ERROR in weightage application: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    # Step 2: Train models
    print("\n" + "=" * 90)
    print("STEP 2: TRAINING MACHINE LEARNING MODELS")
    print("=" * 90)
    
    config = {
        'csv_path': output_csv,
        'task': 'regression',  # Predicting continuous dowry amount
        'enable_advanced_features': True,
        'apply_resampling': None,  # No resampling for regression
        'tune_hyperparameters': True,  # Enable hyperparameter tuning
        'train_neural_network': True,  # Include neural network
        'test_size': 0.2,
        'random_state': 42,
        'output_dir': './output'
    }
    
    print("\nTraining Configuration:")
    for key, value in config.items():
        print(f"  {key:25s}: {value}")
    print("=" * 90)
    
    try:
        # Run the complete pipeline
        ensemble_trainer, preprocessor, report = run_complete_pipeline(**config)
        
        print("\n" + "=" * 90)
        print(" " * 30 + "TRAINING COMPLETE!")
        print("=" * 90)
        
        # Display model performance
        print("\n📊 Model Performance Summary:")
        print("-" * 90)
        
        for model_name, scores in ensemble_trainer.test_scores.items():
            print(f"\n{model_name}:")
            print(f"  R² Score: {scores['R2']:.4f}")
            print(f"  MAE:      ₹{scores['MAE']:,.0f}")
            print(f"  RMSE:     ₹{scores['RMSE']:,.0f}")
            if 'MAPE' in scores:
                print(f"  MAPE:     {scores['MAPE']:.2f}%")
        
        print("\n" + "=" * 90)
        print("\n✅ Models saved successfully!")
        print(f"   Location: {config['output_dir']}/")
        print("\n📁 Generated files:")
        print(f"   • trained_models.pkl - Trained model ensemble")
        print(f"   • preprocessor.pkl - Data preprocessing pipeline")
        print(f"   • performance_report.json - Detailed performance metrics")
        print(f"   • feature_importances.csv - Feature importance analysis")
        if config['train_neural_network']:
            print(f"   • neural_network_loss_curve.png - Training visualization")
        print("=" * 90 + "\n")
        
        # Display feature importance (top 10)
        try:
            import pandas as pd
            fi_path = Path(config['output_dir']) / 'feature_importances.csv'
            if fi_path.exists():
                fi_df = pd.read_csv(fi_path)
                print("\n📈 Top 10 Most Important Features:")
                print("-" * 90)
                # Check which column name is used (Feature or feature)
                feature_col = 'Feature' if 'Feature' in fi_df.columns else 'feature'
                importance_col = 'Importance' if 'Importance' in fi_df.columns else 'importance'
                for idx, row in fi_df.head(10).iterrows():
                    print(f"  {idx+1:2d}. {row[feature_col]:40s} - {row[importance_col]:.4f} ({row.get('Percentage', row.get('percentage', 0)):.2f}%)")
                print("=" * 90 + "\n")
        except Exception as e:
            print(f"\n⚠️  Could not display feature importance: {str(e)}")
        
        return True
        
    except FileNotFoundError as e:
        print(f"\n❌ ERROR: Dataset file not found!")
        print(f"   Expected location: {config['csv_path']}")
        print(f"   Please ensure the dataset exists at this location.")
        sys.exit(1)
        
    except Exception as e:
        print(f"\n❌ ERROR in model training: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
