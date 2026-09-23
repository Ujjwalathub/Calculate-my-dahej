# Dowry Valuation Backend — Equal-Weightage Production

ML REST API predicting dowry valuation (INR) under strict equal-weightage
parity constraints: **Ridge + Regularized NN ensemble, R² ~0.758,
MAE ~₹187,674, 37 features, 400k synthetic records.**

> No `dowry_category` leakage: the serving layer strips that field and maps
> every payload to the 25 live base columns (→ 37 transformed).

## 📊 Model Performance

- **Production Model**: Ridge + Regularized NN Voting Ensemble (equal weightage)
- **R² Score**: ~0.758 (parity-constrained; train/test gap 0.0018, CV 0.7584 ± 0.0018)
- **MAE**: ~₹187,674
- **RMSE**: ~₹242,985
- **Training Samples**: 320,000 (400,000 total, 80/20 split)
- **Features**: 37 transformed (25 base columns, no derived interactions)

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Train Models (First Time Only)

```bash
python train_model.py --equal-weightage --no-advanced-features --no-tune
```

This will:
- Load `data/dowry_equal_weightage.csv` (400k records, no `dowry_category`)
- Standardize 25 base columns → 37 transformed (advanced features OFF)
- Train Ridge (alpha=10000) + Regularized NN + Voting Ensemble
- Save trained models to `./models/` (incl. `stability_analysis` + equal-weightage validation)

Training takes approximately 10-20 minutes (400k rows + 5-fold stability CV).

### 3. Start API Server

```bash
python run.py
```

Server will start at: `http://localhost:8000`

## 📚 API Documentation

Once the server is running, visit:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔧 API Endpoints

### Health Check
```http
GET /health
```

### Model Information
```http
GET /model/info
```

### Single Prediction
```http
POST /predict
Content-Type: application/json

{
  "monthly_recurring_revenue": 150000,
  "patents_held": 12,
  "infrastructure_value": 5000000,
  "fleet_value": 2000000,
  "liquid_cash_reserves": 800000,
  "parent_company_revenue": 120000,
  "business_model": "B2B_Enterprise",
  "brand_reputation": "Industry_Leader",
  "tech_sector": "AI_DeepTech",
  "pending_lawsuits": "no",
  "years_in_operation": 5.8,
  "is_first_acquisition": "yes"
}
```

### Batch Prediction
```http
POST /predict/batch
Content-Type: application/json

{
  "startups": [
    { /* startup data */ },
    { /* startup data */ }
  ]
}
```

## 📁 Project Structure

```
backend/
├── app/
│   ├── api/
│   │   ├── endpoints.py          # API routes
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py             # Configuration
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── request.py            # Request models
│   │   ├── response.py           # Response models
│   │   └── __init__.py
│   ├── services/
│   │   ├── prediction_service.py # ML prediction logic
│   │   └── __init__.py
│   ├── main.py                   # FastAPI app
│   └── __init__.py
├── data/
│   └── dowry_dataset.csv         # Training data
├── models/
│   ├── trained_models.pkl        # Trained ML models
│   ├── preprocessor.pkl          # Preprocessing pipeline
│   ├── performance_report.json   # Model metrics
│   └── neural_network_loss_curve.png
├── scripts/
│   ├── model.py                  # Unified ML pipeline
│   ├── 01_data_generator.py      # Dataset generation
│   └── generate_dowry_dataset.py # Alternative generator
├── tests/
│   ├── test_api.py               # API tests
│   └── __init__.py
├── .env.example                  # Environment template
├── .gitignore
├── README.md                     # This file
├── requirements.txt              # Python dependencies
├── run.py                        # Start server
└── train_model.py                # Train models CLI
```

## 🎯 Training Options

```bash
# Train with all features (default)
python train_model.py

# Train classification models
python train_model.py --task classification

# Skip hyperparameter tuning (faster, uses defaults)
python train_model.py --no-tune

# Skip neural network training
python train_model.py --no-nn

# Use resampling for imbalanced data
python train_model.py --task classification --resampling smote

# Custom test split
python train_model.py --test-size 0.3

# Save to custom directory
python train_model.py --output-dir ./custom_models
```

## 🧠 ML Pipeline Features

### Preprocessing
- Domain transformation (ethical business context)
- Missing value imputation (median for numerical, mode for categorical)
- Standard scaling for numerical features
- One-hot encoding for categorical features

### Feature Engineering (parity lockdown: OFF in production)
- Advanced interactions (Salary × Education, NRI, wealth composites) are
  **disabled** under equal weightage — production uses 25 base columns only.
- Standardization: strict scaler (mean=0, var=1) incl. one-hots for parity.

### Models Trained (equal weightage)
1. **Ridge Regression** - L2 alpha=10000, forces distributed weights ⭐ **Best**
2. **Regularized NN (MLP 50→25)** - weight decay alpha=1.0 + early stopping
3. **Voting Ensemble** - averages Ridge + Regularized NN

### Validation
- **Permutation importance**: max feature 11.75% (< 30% threshold), CV 1.26 (< 1.75)
- **Stability**: 5-fold CV 0.7584 ± 0.0018, train/test gap 0.0018 (HIGHLY STABLE)

### Optimization Techniques
- **Hyperparameter Tuning**: RandomizedSearchCV with 5-fold CV
- **Gradient Descent**: Adam optimizer for neural network
- **Regularization**: L2 penalty (alpha=0.0001)
- **Early Stopping**: Prevents overfitting
- **Resampling**: SMOTE, ADASYN, SMOTEENN, SMOTETomek for imbalanced data

## 🔒 Environment Variables

Create a `.env` file (copy from `.env.example`):

```bash
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
ENVIRONMENT=development
DEBUG=True

# Model Paths
MODEL_PATH=models/trained_models.pkl
PREPROCESSOR_PATH=models/preprocessor.pkl

# Logging
LOG_LEVEL=INFO
```

## 📊 Model Details

### Regularized NN Architecture (equal weightage)
```
Input Layer (37 parity-weighted features)
    ↓
Hidden Layer 1 (50 neurons, ReLU, weight decay alpha=1.0)
    ↓
Hidden Layer 2 (25 neurons, ReLU, weight decay alpha=1.0)
    ↓
Output Layer (1 neuron, Linear activation)
```

### Legacy hyperparameter reference (retired — kept for audit history)
> Production runs `--no-tune` with fixed Ridge alpha=10000 and NN alpha=1.0.
> The XGBoost/LightGBM values below are NOT used in production.

**Legacy XGBoost parameters (retired)**:
- n_estimators: 300
- learning_rate: 0.05
- max_depth: 5
- subsample: 0.9

**Legacy LightGBM parameters (retired)**:
- n_estimators: 300
- learning_rate: 0.05
- num_leaves: 63
- max_depth: 5

## 🧪 Testing

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=app --cov-report=html

# Test API manually
python test_api_manually.py
```

## 🐛 Troubleshooting

### Model Not Found Error
```bash
# Retrain the models
python train_model.py
```

### Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### Port Already in Use
```bash
# Change port in .env file
API_PORT=8001
```

### CORS Issues
- Ensure frontend origin is allowed in `app/core/config.py`
- Check CORS middleware configuration in `app/main.py`

## 📝 Development

### Adding New Features
1. Update `scripts/model.py` - Add feature engineering logic
2. Retrain models: `python train_model.py`
3. Update API schemas if needed

### Modifying API
1. Update schemas in `app/schemas/`
2. Update endpoints in `app/api/endpoints.py`
3. Test changes: `pytest tests/`

## 📈 Performance Metrics

| Model | R² Score | MAE (₹) | RMSE (₹) | MAPE |
|-------|----------|---------|----------|------|
| Ridge (Equal Weightage) | **0.7582** | **187,556** | **242,917** | 10.06% |
| Voting Ensemble (Ridge + NN) | 0.7581 | 187,675 | 242,985 | 10.08% |
| Regularized NN | 0.7559 | 188,586 | 244,045 | 10.14% |

## 🤝 Contributing

1. Create feature branch
2. Make changes
3. Run tests: `pytest tests/`
4. Submit pull request

## 📄 License

This project is licensed under the MIT License.

## 📧 Support

For issues or questions, please open an issue on GitHub.

---

**Built with FastAPI, scikit-learn, Ridge + Regularized NN (equal weightage)**
