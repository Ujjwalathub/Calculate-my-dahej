"""
Model Training Script
=====================

Execute this script to train the machine learning models.

Usage:
    python train_model.py [--task regression|classification] [--no-tune] [--no-nn]

Examples:
    python train_model.py                    # Train regression with all features
    python train_model.py --task classification  # Train classification models
    python train_model.py --no-tune          # Skip hyperparameter tuning (faster)
    python train_model.py --no-nn            # Skip neural network training
"""

import sys
import argparse
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
from model import run_complete_pipeline


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Train machine learning models for startup acquisition valuation'
    )
    
    parser.add_argument(
        '--task',
        type=str,
        choices=['regression', 'classification'],
        default='regression',
        help='Task type: regression or classification (default: regression)'
    )
    
    parser.add_argument(
        '--no-advanced-features',
        action='store_true',
        help='Disable advanced feature engineering'
    )
    
    parser.add_argument(
        '--equal-weightage',
        action='store_true',
        help='Enforce equal feature weightage using Ridge Regression and constrained trees'
    )
    
    parser.add_argument(
        '--resampling',
        type=str,
        choices=['smote', 'adasyn', 'smoteenn', 'smotetomek'],
        default=None,
        help='Resampling method for imbalanced classification'
    )
    
    parser.add_argument(
        '--no-tune',
        action='store_true',
        help='Skip hyperparameter tuning (uses default parameters, faster)'
    )
    
    parser.add_argument(
        '--no-nn',
        action='store_true',
        help='Skip neural network training'
    )
    
    parser.add_argument(
        '--test-size',
        type=float,
        default=0.2,
        help='Test set proportion (default: 0.2)'
    )
    
    parser.add_argument(
        '--random-state',
        type=int,
        default=42,
        help='Random seed for reproducibility (default: 42)'
    )
    
    parser.add_argument(
        '--output-dir',
        type=str,
        default='./models',
        help='Directory to save trained models (default: ./models)'
    )
    
    return parser.parse_args()


def main():
    """Main execution function."""
    args = parse_arguments()
    
    # Configuration - UPDATED to use equal weightage dataset
    config = {
        'csv_path': './data/dowry_equal_weightage.csv',  # Using new dataset without leakage
        'task': args.task,
        'enable_advanced_features': not args.no_advanced_features,
        'apply_resampling': args.resampling,
        'tune_hyperparameters': not args.no_tune,
        'train_neural_network': not args.no_nn,
        'test_size': args.test_size,
        'random_state': args.random_state,
        'output_dir': args.output_dir,
        'equal_weightage_mode': args.equal_weightage  # NEW: Enforce equal weightage
    }
    
    print("\n" + "=" * 90)
    print(" " * 30 + "MODEL TRAINING")
    print("=" * 90)
    print("\nConfiguration:")
    for key, value in config.items():
        print(f"  {key:25s}: {value}")
    print("=" * 90)
    
    try:
        # Run the complete pipeline
        ensemble_trainer, preprocessor, report = run_complete_pipeline(**config)
        
        print("\n" + "=" * 90)
        print(" " * 30 + "TRAINING COMPLETE!")
        print("=" * 90)
        
        # Display best model results
        print("\n📊 Model Performance Summary:")
        print("-" * 90)
        
        if config['task'] == 'regression':
            for model_name, scores in ensemble_trainer.test_scores.items():
                print(f"\n{model_name}:")
                print(f"  R² Score: {scores['R2']:.4f}")
                print(f"  MAE:      ₹{scores['MAE']:,.0f}")
                print(f"  RMSE:     ₹{scores['RMSE']:,.0f}")
        else:
            for model_name, scores in ensemble_trainer.test_scores.items():
                print(f"\n{model_name}:")
                print(f"  Accuracy:    {scores['accuracy']:.4f}")
                print(f"  Weighted F1: {scores['weighted_f1']:.4f}")
        
        print("\n" + "=" * 90)
        print("\n✅ Models saved successfully!")
        print(f"   Location: {config['output_dir']}/")
        print("\n📁 Generated files:")
        print(f"   • trained_models.pkl")
        print(f"   • preprocessor.pkl")
        print(f"   • performance_report.json")
        if config['train_neural_network']:
            print(f"   • neural_network_loss_curve.png")
        print("=" * 90 + "\n")
        
    except FileNotFoundError as e:
        print(f"\n❌ ERROR: Dataset file not found!")
        print(f"   Expected location: {config['csv_path']}")
        print(f"   Please ensure the dataset exists at this location.")
        sys.exit(1)
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
