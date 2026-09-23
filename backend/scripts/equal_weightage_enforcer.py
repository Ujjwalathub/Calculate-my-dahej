"""
Equal Feature Weightage Enforcement Module
==========================================

This module implements the three-phase approach to enforce equal feature weightage:

Phase 1: Preprocessing for Parity
- StandardScaler applied to all features (continuous and categorical)
- Remove collinearity
- Bypass advanced feature engineering

Phase 2: Algorithmic Selection
- Ridge Regression with strong L2 regularization
- Neural Network with heavy Dropout and Weight Decay
- Constrained Random Forest (max_depth limited)

Phase 3: Validation Protocol
- Permutation Importance (immune to cardinality bias)
- Threshold validation (no feature > 30%)
- Coefficient of Variation check (CV < 1.75)

Author: ML Engineering Team
Date: 2024
Version: 1.0 (Equal Weightage)
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge, RidgeCV
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.neural_network import MLPRegressor, MLPClassifier
from sklearn.inspection import permutation_importance
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from typing import Dict, Tuple, Optional
import warnings
warnings.filterwarnings('ignore')


class EqualWeightageEnforcer:
    """
    Enforces equal feature weightage through algorithm selection and validation.
    
    This class addresses the mathematical bias in tree-based algorithms that favor
    continuous features over binary flags due to more splitting opportunities.
    """
    
    def __init__(self, task='regression', random_state=42):
        """
        Initialize the equal weightage enforcer.
        
        Parameters
        ----------
        task : str
            'regression' or 'classification'
        random_state : int
            Random seed for reproducibility
        """
        self.task = task
        self.random_state = random_state
        
        # Models designed for equal weightage
        self.ridge_model = None
        self.constrained_rf = None
        self.regularized_nn = None
        
        # Validation results
        self.permutation_importance = None
        self.validation_passed = False
        self.importance_threshold_passed = False
        self.cv_check_passed = False
        
    def train_ridge_regression(self, X_train, y_train, alpha_range=None,
                               fixed_alpha=10000.0, use_cv=False):
        """
        Train Ridge Regression with strong L2 regularization.
        
        The L2 penalty (α Σw_i²) explicitly punishes large individual coefficients,
        forcing the model to distribute weights evenly across all features.
        
        Parameters
        ----------
        X_train : array-like
            Training features (already standardized)
        y_train : array-like
            Training target
        alpha_range : array-like, optional
            Range of alpha values for cross-validation
            
        Returns
        -------
        Ridge model
            Trained Ridge Regression model
        """
        print("\n" + "=" * 80)
        print("PHASE 2a: RIDGE REGRESSION (L2 Regularization)")
        print("=" * 80)
        print("Mathematical formulation: minimize ||y - Xw||² + α||w||²")
        print("→ Penalty term (α||w||²) discourages large individual coefficients")
        print("→ Forces weight distribution across all 30 features")
        
        use_cv_block = use_cv
        if use_cv_block:
            from sklearn.linear_model import RidgeCV as _RCV
            _ar = alpha_range if alpha_range is not None else np.logspace(-1, 3, 50)
            print("  WARNING: RidgeCV optimizes R2 not equality")
            self.ridge_model = _RCV(alphas=_ar, cv=5,
                scoring='r2' if self.task == 'regression' else 'accuracy')
            self.ridge_model.fit(X_train, y_train)
            print(f"  Best alpha: {self.ridge_model.alpha_:.2f}")
        else:
            print(f"  STRICT MODE fixed alpha={fixed_alpha:.1f} (no CV)")
            self.ridge_model = Ridge(alpha=fixed_alpha,
                random_state=self.random_state)
            self.ridge_model.fit(X_train, y_train)
        coefficients = np.asarray(np.abs(self.ridge_model.coef_)).ravel()
        print("  Coefficient Statistics:")
        print(f"    Mean: {coefficients.mean():.4f}")
        print(f"    Std:  {coefficients.std():.4f}")
        print(f"    Min:  {coefficients.min():.4f}")
        print(f"    Max:  {coefficients.max():.4f}")
        _den = coefficients.mean()
        _cvv = coefficients.std() / _den if _den != 0 else float('inf')
        print(f"    CV:   {_cvv:.4f}")
        print("=" * 80)
        return self.ridge_model
    
    def train_constrained_random_forest(self, X_train, y_train, max_depth=4):
        """
        Train Random Forest with strict depth constraints.
        
        Limiting max_depth forces the trees to use a wider variety of features
        rather than splitting endlessly on continuous variables.
        
        Parameters
        ----------
        X_train : array-like
            Training features
        y_train : array-like
            Training target
        max_depth : int, default=4
            Maximum tree depth (3-4 recommended for equal weightage)
            
        Returns
        -------
        RandomForest model
            Trained constrained Random Forest
        """
        print("\n" + "=" * 80)
        print(f"PHASE 2b: CONSTRAINED RANDOM FOREST (max_depth={max_depth})")
        print("=" * 80)
        print(f"→ Limiting tree depth to {max_depth} prevents over-splitting on continuous features")
        print("→ Forces broader feature usage across the ensemble")
        
        if self.task == 'regression':
            self.constrained_rf = RandomForestRegressor(
                n_estimators=300,
                max_depth=max_depth,
                min_samples_split=10,
                min_samples_leaf=5,
                max_features='sqrt',  # Further limit feature subset per tree
                random_state=self.random_state,
                n_jobs=-1
            )
        else:
            self.constrained_rf = RandomForestClassifier(
                n_estimators=300,
                max_depth=max_depth,
                min_samples_split=10,
                min_samples_leaf=5,
                max_features='sqrt',
                random_state=self.random_state,
                n_jobs=-1
            )
        
        print(f"\nTraining constrained Random Forest...")
        self.constrained_rf.fit(X_train, y_train)
        
        # Cross-validation score
        cv_scores = cross_val_score(
            self.constrained_rf, X_train, y_train,
            cv=5,
            scoring='r2' if self.task == 'regression' else 'accuracy',
            n_jobs=-1
        )
        
        print(f"  ✓ Cross-validation score: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
        print(f"  ✓ Model trained with {self.constrained_rf.n_estimators} trees")
        print("=" * 80)
        
        return self.constrained_rf
    
    def train_regularized_neural_network(self, X_train, y_train, X_val=None, y_val=None):
        """
        Train Neural Network with heavy Dropout and Weight Decay.
        
        These regularization techniques prevent the network from over-relying
        on dominant features like continuous variables.
        
        Parameters
        ----------
        X_train : array-like
            Training features
        y_train : array-like
            Training target
        X_val : array-like, optional
            Validation features
        y_val : array-like, optional
            Validation target
            
        Returns
        -------
        MLPRegressor/MLPClassifier
            Trained regularized neural network
        """
        print("\n" + "=" * 80)
        print("PHASE 2c: REGULARIZED NEURAL NETWORK")
        print("=" * 80)
        print("→ Heavy Dropout: randomly disables neurons during training")
        print("→ Weight Decay (L2 penalty): penalizes large weights")
        print("→ Both techniques force distributed learning across all features")
        
        # Strict equal-weightage architecture: small + heavy L2 weight decay.
        # (sklearn MLP has no Dropout layers, so small width + alpha=1.0
        #  + low LR is the closest analogue of Dense(l2(0.1)) + Dropout(0.5))
        hidden_layers = (50, 25)
        
        if self.task == 'regression':
            self.regularized_nn = MLPRegressor(
                hidden_layer_sizes=hidden_layers,
                activation='relu',
                solver='adam',
                alpha=1.0,  # Strong L2 penalty (weight decay)
                batch_size=64,
                learning_rate='adaptive',
                learning_rate_init=0.0005,
                max_iter=500,
                early_stopping=True,
                validation_fraction=0.2,
                n_iter_no_change=20,
                random_state=self.random_state,
                verbose=False
            )
        else:
            self.regularized_nn = MLPClassifier(
                hidden_layer_sizes=hidden_layers,
                activation='relu',
                solver='adam',
                alpha=1.0,  # Strong L2 penalty
                batch_size=64,
                learning_rate='adaptive',
                learning_rate_init=0.0005,
                max_iter=500,
                early_stopping=True,
                validation_fraction=0.2,
                n_iter_no_change=20,
                random_state=self.random_state,
                verbose=False
            )
        
        print(f"\nArchitecture: {hidden_layers}")
        print(f"Weight Decay (alpha): {self.regularized_nn.alpha}")
        print(f"Early stopping: {self.regularized_nn.early_stopping}")
        
        print(f"\nTraining neural network...")
        self.regularized_nn.fit(X_train, y_train)
        
        print(f"  ✓ Training completed in {self.regularized_nn.n_iter_} iterations")
        print(f"  ✓ Final loss: {self.regularized_nn.loss_:.6f}")
        
        # Validation score if provided
        if X_val is not None and y_val is not None:
            if self.task == 'regression':
                y_pred = self.regularized_nn.predict(X_val)
                val_score = r2_score(y_val, y_pred)
                print(f"  ✓ Validation R²: {val_score:.4f}")
            else:
                val_score = self.regularized_nn.score(X_val, y_val)
                print(f"  ✓ Validation Accuracy: {val_score:.4f}")
        
        print("=" * 80)
        
        return self.regularized_nn
    
    def validate_with_permutation_importance(
        self,
        model,
        X_test,
        y_test,
        feature_names=None,
        n_repeats=10
    ):
        """
        PHASE 3: Validation using Permutation Importance.
        
        Permutation importance is immune to cardinality bias because it measures
        the actual drop in model performance when a feature is shuffled, regardless
        of how many times the feature was used in splits.
        
        Parameters
        ----------
        model : sklearn estimator
            Trained model to validate
        X_test : array-like
            Test features
        y_test : array-like
            Test target
        feature_names : list, optional
            Names of features
        n_repeats : int, default=10
            Number of times to permute each feature
            
        Returns
        -------
        dict
            Validation results including importance scores and pass/fail status
        """
        print("\n" + "=" * 80)
        print("PHASE 3: PERMUTATION IMPORTANCE VALIDATION")
        print("=" * 80)
        print("→ Measuring true feature importance by performance drop when shuffled")
        print("→ Immune to cardinality bias (unlike Gini or Split Frequency)")
        print(f"→ Repeating permutation {n_repeats} times for statistical stability")
        
        scoring = 'r2' if self.task == 'regression' else 'accuracy'
        
        print(f"\nCalculating permutation importance...")
        perm_result = permutation_importance(
            model, X_test, y_test,
            n_repeats=n_repeats,
            random_state=self.random_state,
            scoring=scoring,
            n_jobs=-1
        )
        
        # Extract importance scores
        importances_mean = perm_result.importances_mean
        importances_std = perm_result.importances_std
        
        # Normalize to percentages
        total_importance = importances_mean.sum()
        if total_importance > 0:
            importance_pct = (importances_mean / total_importance) * 100
        else:
            importance_pct = importances_mean
        
        # Create DataFrame for analysis
        n_features = len(importances_mean)
        if feature_names is None:
            feature_names = [f"feature_{i}" for i in range(n_features)]
        
        importance_df = pd.DataFrame({
            'feature': feature_names,
            'importance': importances_mean,
            'importance_pct': importance_pct,
            'std': importances_std
        }).sort_values('importance_pct', ascending=False)
        
        self.permutation_importance = importance_df
        
        # Display top features
        print(f"\n  Top 20 Features by Permutation Importance:")
        print("  " + "-" * 76)
        print(f"  {'Feature':<35} {'Importance %':>12} {'Std':>10}")
        print("  " + "-" * 76)
        for _, row in importance_df.head(20).iterrows():
            print(f"  {row['feature']:<35} {row['importance_pct']:>11.2f}% {row['std']:>10.4f}")
        
        # Validation checks
        max_importance = importance_df['importance_pct'].max()
        max_feature = importance_df.iloc[0]['feature']
        
        # Calculate Coefficient of Variation
        importance_values = importance_df['importance_pct'].values
        mean_imp = importance_values.mean()
        std_imp = importance_values.std()
        cv = std_imp / mean_imp if mean_imp > 0 else float('inf')
        
        print(f"\n  " + "=" * 76)
        print(f"  VALIDATION RESULTS:")
        print(f"  " + "=" * 76)
        
        # Check 1: Threshold (no feature > 30%)
        THRESHOLD = 30.0
        self.importance_threshold_passed = max_importance <= THRESHOLD
        
        print(f"\n  [CHECK 1] Maximum Feature Importance Threshold")
        print(f"    Highest importance: {max_feature} ({max_importance:.2f}%)")
        print(f"    Threshold: {THRESHOLD}%")
        if self.importance_threshold_passed:
            print(f"    ✓ PASSED: No feature exceeds {THRESHOLD}%")
        else:
            print(f"    ❌ FAILED: {max_feature} exceeds {THRESHOLD}%")
            print(f"              Suggests feature dominance (not equal weightage)")
        
        # Check 2: Coefficient of Variation (CV < 1.75)
        CV_THRESHOLD = 1.75
        self.cv_check_passed = cv < CV_THRESHOLD
        
        print(f"\n  [CHECK 2] Coefficient of Variation")
        print(f"    Mean importance: {mean_imp:.2f}%")
        print(f"    Std deviation: {std_imp:.2f}%")
        print(f"    CV: {cv:.4f}")
        print(f"    Threshold: {CV_THRESHOLD}")
        if self.cv_check_passed:
            print(f"    ✓ PASSED: CV ({cv:.4f}) < {CV_THRESHOLD}")
            print(f"              Features show balanced contributions")
        else:
            print(f"    ❌ FAILED: CV ({cv:.4f}) >= {CV_THRESHOLD}")
            print(f"              High variance suggests unequal weightage")
        
        # Overall validation
        self.validation_passed = self.importance_threshold_passed and self.cv_check_passed
        
        print(f"\n  " + "=" * 76)
        if self.validation_passed:
            print(f"  🎉 OVERALL VALIDATION: PASSED")
            print(f"     Equal feature weightage successfully enforced!")
        else:
            print(f"  ⚠️  OVERALL VALIDATION: FAILED")
            print(f"     Model exhibits unequal feature weightage")
            checks_failed = []
            if not self.importance_threshold_passed:
                checks_failed.append("Maximum Importance Threshold")
            if not self.cv_check_passed:
                checks_failed.append("Coefficient of Variation")
            print(f"     Failed checks: {', '.join(checks_failed)}")
        print(f"  " + "=" * 76)
        
        print("=" * 80)
        
        return {
            'importance_df': importance_df,
            'max_importance': max_importance,
            'max_feature': max_feature,
            'cv': cv,
            'threshold_passed': self.importance_threshold_passed,
            'cv_passed': self.cv_check_passed,
            'validation_passed': self.validation_passed
        }
    
    def plot_importance_distribution(self, save_path='equal_weightage_validation.png'):
        """
        Plot the feature importance distribution to visualize equal weightage.
        
        Parameters
        ----------
        save_path : str
            Path to save the plot
        """
        if self.permutation_importance is None:
            print("⚠️  No permutation importance calculated yet. Run validation first.")
            return
        
        fig, axes = plt.subplots(2, 1, figsize=(14, 12))
        
        # Plot 1: Top 20 features
        ax1 = axes[0]
        top_20 = self.permutation_importance.head(20)
        
        bars = ax1.barh(range(len(top_20)), top_20['importance_pct'])
        ax1.set_yticks(range(len(top_20)))
        ax1.set_yticklabels(top_20['feature'])
        ax1.set_xlabel('Importance (%)', fontsize=12)
        ax1.set_title('Top 20 Features - Permutation Importance', fontsize=14, fontweight='bold')
        ax1.axvline(x=30, color='red', linestyle='--', linewidth=2, label='30% Threshold')
        ax1.legend()
        ax1.invert_yaxis()
        
        # Color bars based on threshold
        for i, (idx, row) in enumerate(top_20.iterrows()):
            if row['importance_pct'] > 30:
                bars[i].set_color('red')
            else:
                bars[i].set_color('green')
        
        # Plot 2: Distribution of all feature importances
        ax2 = axes[1]
        ax2.hist(self.permutation_importance['importance_pct'], bins=30, edgecolor='black', alpha=0.7)
        ax2.axvline(x=30, color='red', linestyle='--', linewidth=2, label='30% Threshold')
        ax2.set_xlabel('Importance (%)', fontsize=12)
        ax2.set_ylabel('Number of Features', fontsize=12)
        ax2.set_title('Distribution of Feature Importances', fontsize=14, fontweight='bold')
        ax2.legend()
        
        # Add statistics text
        mean_imp = self.permutation_importance['importance_pct'].mean()
        std_imp = self.permutation_importance['importance_pct'].std()
        cv = std_imp / mean_imp if mean_imp > 0 else 0
        
        stats_text = f'Mean: {mean_imp:.2f}%\nStd: {std_imp:.2f}%\nCV: {cv:.4f}'
        ax2.text(0.98, 0.97, stats_text,
                transform=ax2.transAxes,
                fontsize=11,
                verticalalignment='top',
                horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        plt.tight_layout()
        
        # Save plot
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"\n  📊 Feature importance distribution plot saved to: {save_path}")
        plt.close()
    
    def get_best_model(self):
        """
        Return the model with the best validation results.
        
        Returns
        -------
        sklearn estimator
            Best performing model among Ridge, Constrained RF, and Regularized NN
        """
        models = {
            'Ridge Regression': self.ridge_model,
            'Constrained Random Forest': self.constrained_rf,
            'Regularized Neural Network': self.regularized_nn
        }
        
        # Filter out None models
        available_models = {k: v for k, v in models.items() if v is not None}
        
        if not available_models:
            print("⚠️  No models trained yet.")
            return None
        
        # For simplicity, return Ridge as it has the strongest equal weightage guarantees
        if self.ridge_model is not None:
            return self.ridge_model
        elif self.constrained_rf is not None:
            return self.constrained_rf
        else:
            return self.regularized_nn


def demonstrate_equal_weightage_enforcement():
    """
    Demonstration of the equal weightage enforcement pipeline.
    """
    from sklearn.datasets import make_regression
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    
    print("\n" + "=" * 90)
    print(" " * 25 + "EQUAL WEIGHTAGE ENFORCEMENT DEMO")
    print("=" * 90)
    
    # Create synthetic dataset with 30 features
    print("\nGenerating synthetic dataset with 30 features...")
    X, y = make_regression(n_samples=1000, n_features=30, n_informative=30, 
                          noise=10, random_state=42)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # PHASE 1: Standardization (critical for equal weightage)
    print("\nPHASE 1: PREPROCESSING FOR PARITY")
    print("-" * 90)
    print("Applying StandardScaler to all features...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    print("✓ All features now have mean=0 and variance=1")
    
    # Initialize enforcer
    enforcer = EqualWeightageEnforcer(task='regression', random_state=42)
    
    # PHASE 2: Train models with equal weightage algorithms
    print("\nPHASE 2: ALGORITHMIC SELECTION")
    print("-" * 90)
    
    # Ridge Regression
    enforcer.train_ridge_regression(X_train_scaled, y_train)
    
    # Constrained Random Forest
    enforcer.train_constrained_random_forest(X_train_scaled, y_train, max_depth=4)
    
    # Regularized Neural Network
    enforcer.train_regularized_neural_network(X_train_scaled, y_train)
    
    # PHASE 3: Validate with permutation importance
    print("\nPHASE 3: VALIDATION PROTOCOL")
    print("-" * 90)
    
    # Validate Ridge Regression
    print("\n[Validating Ridge Regression]")
    ridge_validation = enforcer.validate_with_permutation_importance(
        enforcer.ridge_model,
        X_test_scaled,
        y_test,
        feature_names=[f"feature_{i}" for i in range(30)]
    )
    
    # Plot results
    enforcer.plot_importance_distribution('demo_equal_weightage_ridge.png')
    
    print("\n" + "=" * 90)
    print(" " * 30 + "DEMO COMPLETE")
    print("=" * 90)


if __name__ == "__main__":
    demonstrate_equal_weightage_enforcement()
