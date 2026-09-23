"""
Response Schemas

Pydantic models for API responses.
"""

from pydantic import BaseModel, Field
from typing import List, Any, Optional
from datetime import datetime


class PredictionRange(BaseModel):
    """Prediction range with confidence intervals."""
    
    lower_bound: int = Field(..., description="Lower bound of prediction (MAE-based)")
    upper_bound: int = Field(..., description="Upper bound of prediction (MAE-based)")


class PredictionData(BaseModel):
    """Single prediction result data."""
    
    predicted_acquisition_price_inr: int = Field(
        ..., 
        description="Predicted acquisition price in INR"
    )
    predicted_dowry_amount_inr: Optional[int] = Field(
        None,
        description="Predicted dowry valuation in INR"
    )
    confidence_score: float = Field(
        ..., 
        ge=0.0, 
        le=1.0,
        description="Model confidence (R² score)"
    )
    prediction_range: PredictionRange = Field(
        ...,
        description="Prediction range based on model MAE"
    )


class PredictionResponse(BaseModel):
    """Standard response for single prediction."""
    
    success: bool = Field(..., description="Whether the request was successful")
    data: Optional[PredictionData] = Field(None, description="Prediction result")
    message: str = Field(..., description="Response message")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Response timestamp")
    
    class Config:
        json_schema_extra = {
            "example": {
                "success": True,
                "data": {
                    "predicted_acquisition_price_inr": 750000,
                    "confidence_score": 0.7581,
                    "prediction_range": {
                        "lower_bound": 689810,
                        "upper_bound": 810190
                    }
                },
                "message": "Prediction successful",
                "timestamp": "2026-09-14T20:58:00.000Z"
            }
        }


class BatchPredictionData(BaseModel):
    """Batch prediction result data."""
    
    predictions: List[PredictionData] = Field(
        ...,
        description="List of predictions for each startup"
    )
    total_count: int = Field(..., description="Total number of predictions")
    average_acquisition_price: int = Field(
        ...,
        description="Average predicted acquisition price"
    )


class BatchPredictionResponse(BaseModel):
    """Response for batch predictions."""
    
    success: bool = Field(..., description="Whether the request was successful")
    data: Optional[BatchPredictionData] = Field(None, description="Batch prediction results")
    message: str = Field(..., description="Response message")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Response timestamp")


class HealthResponse(BaseModel):
    """Health check response."""
    
    status: str = Field(..., description="Service status")
    model_loaded: bool = Field(..., description="Whether ML model is loaded")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Check timestamp")
    version: str = Field(..., description="API version")


class ModelInfo(BaseModel):
    """Model information response."""
    
    model_type: str = Field(..., description="Type of ML model")
    components: List[str] = Field(..., description="Model components")
    r2_score: float = Field(..., description="Model R² score on test set")
    mae: int = Field(..., description="Mean Absolute Error on test set")
    rmse: int = Field(..., description="Root Mean Squared Error on test set")
    training_samples: int = Field(..., description="Number of training samples")
    features: int = Field(..., description="Number of features")
    
    class Config:
        json_schema_extra = {
            "example": {
                "model_type": "Ridge + NN Ensemble (Equal Weightage)",
                "components": ["Ridge Regression", "Regularized NN (MLP)", "Voting Ensemble"],
                "r2_score": 0.7581,
                "mae": 187674,
                "rmse": 242985,
                "training_samples": 320000,
                "features": 37
            }
        }


class ErrorResponse(BaseModel):
    """Error response."""
    
    success: bool = Field(False, description="Always False for errors")
    error: str = Field(..., description="Error type")
    message: str = Field(..., description="Error message")
    details: Optional[Any] = Field(None, description="Additional error details")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Error timestamp")
    
    class Config:
        json_schema_extra = {
            "example": {
                "success": False,
                "error": "ValidationError",
                "message": "Invalid input data",
                "details": {
                    "field": "monthly_recurring_revenue",
                    "issue": "Value must be between 15000 and 500000"
                },
                "timestamp": "2026-08-15T20:58:00.000Z"
            }
        }
