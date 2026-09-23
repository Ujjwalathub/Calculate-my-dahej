# Dowry Valuation System — Equal-Weightage Production (Phase 4)

A machine learning system for dowry valuation operating under strict
**equal-weightage parity constraints**: **Ridge + Regularized NN ensemble,
R² ~0.758, MAE ~₹187,674, 37 features, 400k synthetic records.**

> Legacy unconstrained metrics (R² 0.9483, XGBoost/LightGBM, 106 features,
> 10k records) and the `dowry_category` leakage field are retired. The backend
> strips `dowry_category` and serves the parity-constrained ensemble.

## 🆕 Latest: Phase 3 Implementation (Classification Enhancement)

**Status:** ✅ Ready for Execution  
**Goal:** Improve High class F1 from 0.45 to ≥0.62

### Quick Start Phase 3

```bash
cd backend
python run_phase3_training.py
```

**See:** [PHASE3_SUMMARY.md](PHASE3_SUMMARY.md) for complete details.

---

## Phase 4: Equal-Weightage Production (Current)

- **Model:** Ridge (alpha=10000) + Regularized NN (MLP 50→25, alpha=1.0) + Voting Ensemble
- **Metrics:** R² ~0.758, MAE ~₹187,674, RMSE ~₹242,985
- **Scale:** 400,000 synthetic records (320,000 train / 80,000 test), 25 base columns → 37 features
- **Parity:** permutation max 11.75% (< 30%), CV 1.26 (< 1.75) — PASSED
- **Stability:** 5-fold CV 0.7584 ± 0.0018, train/test gap 0.0018 — HIGHLY STABLE
- **Leakage:** `dowry_category` retired and stripped at serving; legacy tree artifacts quarantined in `backend/legacy/`

```bash
cd backend
python train_model.py --equal-weightage --no-advanced-features --no-tune
```

---

## Project Structure (Phase 4)

```
Dowry/
├── backend/
│   ├── app/
│   │   ├── api/              # API endpoints
│   │   ├── core/             # Configuration
│   │   ├── models/           # Trained ML models
│   │   ├── schemas/          # Request/response schemas
│   │   └── services/         # Preprocessing & prediction
│   ├── data/                 # Dataset (400,000 synthetic equal-weightage records)
│   ├── legacy/               # Quarantined: feature_engineering.py, preprocessing_pipeline_v2.py, biased tree importances
│   ├── scripts/              # Training scripts
│   │   ├── phase2_model_training.py
│   │   └── phase3_model_training.py  # NEW
│   ├── tests/                # Test suite
│   ├── visualizations/       # Model performance plots
│   └── run_phase3_training.py  # NEW: Phase 3 runner
│
├── frontend/                 # Vue.js web interface
│
├── PHASE3_DOCUMENTATION.md   # NEW: Full Phase 3 docs
├── PHASE3_SUMMARY.md         # NEW: Quick overview
├── PHASE_COMPARISON.md       # NEW: Phase evolution
├── PHASE3_CHECKLIST.md       # NEW: Execution checklist
└── design.md                 # System design document
```

---

## Current Performance (Phase 4 Production)

### Regression — Ridge + Regularized NN Ensemble (equal weightage)
- **R² Score:** ~0.758 (train/test gap 0.0018; 5-fold CV 0.7584 ± 0.0018)
- **MAE:** ~₹187,674
- **RMSE:** ~₹242,985
- **Status:** ✅ Production (parity-constrained)

> Phase 2/3 unconstrained numbers (R² 0.918, XGBoost/LightGBM, 10k records)
> are superseded and retained in git history only.

### Classification (Phase 2 - Needs Improvement)
| Class | F1 Score | Status |
|-------|----------|--------|
| Low | 0.85 | ✅ Good |
| Medium | 0.90 | ✅ Excellent |
| **High** | **0.45** | ❌ **Poor - Phase 3 Target** |
| Very High | 0.92 | ✅ Excellent |

**Overall:** 0.89 Accuracy, 0.889 Weighted F1

---

## Phase Evolution

### Phase 1: Foundation (Baseline)
- Random Forest models
- Basic feature engineering
- R² = 0.9029, Classification Acc = 73.25%

### Phase 2: Optimization
- Promoted XGBoost as primary model
- Added 23 advanced features
- Improved regression: R² = 0.918
- Improved classification: Acc = 0.89
- **Problem discovered:** High class F1 dropped to 0.45

### Phase 3: Classification Fix (Current)
- **Critical fix:** Corrected classification target (88% Very High → balanced)
- Added 12 High-class specific features
- Advanced resampling (ADASYN, SMOTEENN, SMOTETomek)
- Stronger class weighting (High = 2.8×)
- Specialized High-vs-Rest binary classifier
- **Target:** High F1 ≥ 0.62

---

## Key Features

### Machine Learning (Phase 4 Production)
- **Models:** Ridge Regression, Regularized NN (MLP), Voting Ensemble
- **Tasks:** Regression under equal-weightage parity constraints
- **Dataset:** 400,000 synthetic records (equal weightage, no `dowry_category`)
- **Features:** 37 transformed (25 base columns; advanced interactions OFF)

### Advanced Techniques
- Ensemble voting
- Class imbalance handling (ADASYN, SMOTEENN, SMOTETomek)
- Dynamic class weighting
- Specialized binary classifiers
- Comprehensive preprocessing pipeline

### API
- FastAPI backend
- RESTful endpoints
- Real-time predictions
- Batch processing support

---

## Quick Start

### 1. Setup Environment

```bash
# Clone repository
cd Dowry

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r backend/requirements.txt
```

### 2. Run Phase 3 Training

```bash
cd backend
python run_phase3_training.py
```

**Duration:** 15-20 minutes  
**Output:** Models, metrics, confusion matrices

### 3. Start API Server

```bash
cd backend
uvicorn app.main:app --reload
```

**Access:** http://localhost:8000

### 4. Run Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## Phase 3 Documentation

### Essential Reading
1. **[PHASE3_SUMMARY.md](PHASE3_SUMMARY.md)** - Start here for overview
2. **[backend/README_PHASE3.md](backend/README_PHASE3.md)** - Quick start guide
3. **[PHASE3_CHECKLIST.md](PHASE3_CHECKLIST.md)** - Execution checklist

### Detailed Documentation
4. **[PHASE3_DOCUMENTATION.md](PHASE3_DOCUMENTATION.md)** - Complete specification
5. **[PHASE_COMPARISON.md](PHASE_COMPARISON.md)** - Phase evolution analysis

---

## Key Improvements in Phase 3

### 1. Fixed Classification Target
**Root Cause:** Incorrect target definition caused 88% Very High samples

**Solution:** Quantile-based binning
- Low: 0-33% → ~33% samples
- Medium: 33-66% → ~33% samples
- High: 66-85% → ~19% samples
- Very High: 85-100% → ~15% samples

**Impact:** Foundation for all other improvements

### 2. High-Class Specific Features (12 new)
```python
# Interaction Features
salary_edu_interaction = boy_salary × boy_edu_num
nri_high_salary = boy_salary if NRI else 0
wealth_intensity = family_income / (assets + 1)
high_zone_score = weighted_combo(salary, edu, assets)
prev_married_high_risk = girl_prev_married × (girl_age > 25)
edu_gap_penalty = max(0, girl_edu - boy_edu)

# Ratio Features
salary_to_family_ratio = boy_salary / family_income
age_premium_factor = (age_diff × boy_age) / 100
education_premium = boy_edu × is_govt_job

# Binary Threshold Features
is_high_earner = boy_salary ≥ 70th percentile
is_premium_family = family_income ≥ 75th percentile
is_advanced_education = boy_edu ≥ 6 (PG/PhD)
```

### 3. Advanced Resampling
- **ADASYN:** Adaptive synthetic sampling (focuses on hard samples)
- **SMOTEENN:** SMOTE + cleaning (removes noisy synthetics)
- **SMOTETomek:** SMOTE + Tomek links (balanced over/under sampling)

### 4. Stronger Class Weighting
- Low: 1.0× (baseline)
- Medium: 1.2× (mild boost)
- **High: 2.8×** (aggressive boost - main focus)
- Very High: 0.75× (reduce majority dominance)

### 5. Specialized High-vs-Rest Model
Binary classifier optimized exclusively for High class detection.

---

## Expected Results

### Target Metrics
| Metric | Phase 2 | Phase 3 Target | Improvement |
|--------|---------|---------------|-------------|
| High F1 | 0.45 | ≥0.62 | +38% |
| High Recall | 0.49 | ≥0.60 | +22% |
| Weighted F1 | 0.889 | ≥0.85 | Maintain |
| Accuracy | 0.89 | ≥0.80 | Maintain |

### Confidence Estimates
- **Conservative (70%):** High F1 = 0.60–0.62
- **Realistic (50%):** High F1 = 0.63–0.67
- **Optimistic (20%):** High F1 = 0.68–0.72

### Success Probability: **80-85%**

---

## API Endpoints

### Health Check
```bash
GET /health
```

### Model Info
```bash
GET /model/info
```

### Single Prediction
```bash
POST /predict
Content-Type: application/json

{
  "girl_age": 24,
  "boy_age": 28,
  "girl_education": "Graduate",
  "boy_education": "Post Graduate",
  ...
}
```

### Batch Prediction
```bash
POST /predict/batch
Content-Type: application/json

[
  {...},
  {...}
]
```

---

## Development

### Running Tests
```bash
cd backend
pytest tests/
```

### Code Structure
```python
# Preprocessing
preprocessing_pipeline_v2.py  # Phase 2 features
phase3_model_training.py      # Phase 3 features

# Model Training
phase2_model_training.py      # Phase 2 (XGBoost, LightGBM, RF)
phase3_model_training.py      # Phase 3 (+ ADASYN, SMOTEENN, SMOTETomek)

# Prediction Service
prediction_service.py          # Real-time inference
```

---

## Technologies

### Backend
- **Python 3.8+**
- **FastAPI** - API framework
- **XGBoost** - Gradient boosting (primary)
- **LightGBM** - Gradient boosting (secondary)
- **scikit-learn** - Preprocessing & Random Forest
- **imbalanced-learn** - Resampling (ADASYN, SMOTE)
- **pandas, numpy** - Data manipulation

### Frontend
- **Vue.js 3** - UI framework
- **Vite** - Build tool
- **TailwindCSS** - Styling
- **Recharts** - Visualizations

---

## Model Files

### Phase 2 (Current Production)
- `phase2_regression_models.pkl` - Regression models
- `phase2_classification_models.pkl` - Classification models

### Phase 3 (After Training)
- `phase3_classification_models.pkl` - Enhanced classification
- `phase3_results.json` - Performance metrics

---

## Troubleshooting

### Missing Dependencies
```bash
pip install imbalanced-learn xgboost lightgbm
```

### Out of Memory
Reduce batch size or model capacity in training script.

### Training Too Slow
Enable early stopping or reduce n_estimators.

---

## Future Enhancements

### If Phase 3 Succeeds (High F1 ≥ 0.62)
1. ✅ Deploy Phase 3 classification models
2. ✅ Keep Phase 2 regression (already excellent)
3. ✅ Monitor production performance
4. ✅ Collect user feedback

### If Phase 3 Falls Short
1. 🔄 Increase High weight to 3.5×
2. 🔄 Implement cost-sensitive learning
3. 🔄 Try ensemble voting
4. 🔄 Add distance-to-centroid features
5. 🔄 Collect more High-class training data

---

## Contributing

1. Review documentation
2. Run Phase 3 training
3. Analyze results
4. Propose improvements via issues

---

## License

[Your License Here]

---

## Contact

For questions about Phase 3:
- See [PHASE3_DOCUMENTATION.md](PHASE3_DOCUMENTATION.md)
- Check [PHASE3_CHECKLIST.md](PHASE3_CHECKLIST.md)
- Review implementation in `backend/scripts/phase3_model_training.py`

---

## Acknowledgments

This project demonstrates a systematic approach to fixing machine learning classification weaknesses through:
1. Root cause analysis (incorrect target definition)
2. Targeted feature engineering
3. Advanced resampling techniques
4. Strategic class weighting
5. Specialized model architectures

**Key Lesson:** Sometimes the biggest improvements come from fixing fundamental data issues, not just adding more complex models.

---

**Version:** 3.0.0 (Phase 3 Implementation Complete)  
**Status:** Ready for Training  
**Last Updated:** Phase 3 Implementation Ready
