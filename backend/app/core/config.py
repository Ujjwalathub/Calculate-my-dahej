"""
Configuration Management

Handles environment variables and application settings.
"""

from pydantic_settings import BaseSettings
from typing import List
from pathlib import Path
import os


# Resolve the absolute path to the backend/ directory
# __file__ is in backend/app/core/config.py -> parent=core, parent.parent=app, parent.parent.parent=backend/
BASE_DIR = Path(__file__).resolve().parent.parent.parent


def _abs_path(value: str, *parts: str) -> str:
    """Resolve a path setting to absolute, honouring env overrides (Phase 5)."""
    if value and os.path.isabs(value):
        return value
    if value:
        return str((BASE_DIR / value).resolve())
    return str(BASE_DIR.joinpath(*parts))


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # API Configuration
    API_TITLE: str = "Startup Acquisition Valuation API"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = """
    Equal-weightage ML API for predicting dowry valuation (INR).
    
    **Features:**
    - Ridge + Regularized NN Ensemble (equal weightage)
    - R² ~ 0.758, MAE ~ ₹187k, 37 features, 400k records
    - Real-time predictions
    - Batch processing support
    """
    
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    
    # Environment
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    # CORS - explicit frontend dev-server origins only (no wildcard default).
    # The API echoes back ONLY a matching origin, which is what fixes
    # browser CORS errors in dev. Covers Vite (5173) and TanStack Start
    # (3000/3001) on localhost AND 127.0.0.1. Extend via ALLOWED_ORIGINS
    # env var; set ALLOW_ALL_ORIGINS=true only to temporarily bypass.
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3001",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]
    ALLOW_ALL_ORIGINS: bool = False
    
    # Model Configuration
    MODEL_PATH: str = str(BASE_DIR / "models" / "trained_models.pkl")
    PREPROCESSOR_PATH: str = str(BASE_DIR / "models" / "preprocessor.pkl")
    CONFIDENCE_THRESHOLD: float = 0.9
    
    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = str(BASE_DIR / "logs" / "api.log")
    
    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = 100
    
    # Prediction Bounds (based on training data)
    MIN_ACQUISITION_PRICE: int = 50000
    MAX_ACQUISITION_PRICE: int = 80000000
    
    def model_post_init(self, __context) -> None:
        object.__setattr__(self, "MODEL_PATH", _abs_path(self.MODEL_PATH, "models", "trained_models.pkl"))
        object.__setattr__(self, "PREPROCESSOR_PATH", _abs_path(self.PREPROCESSOR_PATH, "models", "preprocessor.pkl"))
        object.__setattr__(self, "LOG_FILE", _abs_path(self.LOG_FILE, "logs", "api.log"))

    model_config = {"env_file": ".env", "case_sensitive": True}


# Create global settings instance
settings = Settings()


def get_settings() -> Settings:
    """
    Dependency injection for settings.
    
    Returns
    -------
    Settings
        Application settings instance
    """
    return settings
