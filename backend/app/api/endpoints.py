"""
API Endpoints

Defines all REST API routes for the application.
"""

from fastapi import APIRouter, HTTPException, Request, status
from typing import Dict, Any, Union, List
import logging

from app.schemas.request import (
    DowryData,
    InferredPredictItem,
    PredictItem,
    PredictionRequest,
    StartupData,
    BatchPredictionRequest,
)
from app.schemas.response import (
    PredictionResponse,
    BatchPredictionResponse,
    HealthResponse,
    ModelInfo,
    ErrorResponse
)
from app.services.prediction_service import get_prediction_service
from app.core.config import settings

logger = logging.getLogger(__name__)

# Create router
router = APIRouter()


def get_service(request: Request):
    """Retrieve the PredictionService from lifespan state (Phase 5).

    Prefers ``request.app.state.prediction_service`` populated by the
    lifespan handler; falls back to the module-level lazy singleton so
    TestClient usage without lifespan still works. Returns None when
    the prediction engine is offline.
    """
    try:
        svc = getattr(request.app.state, "prediction_service", None)
        if svc is not None and getattr(svc, "is_loaded", lambda: False)():
            return svc
        # Lifespan flagged healthy but instance missing/unloaded -> lazy retry
        if getattr(request.app.state, "models_healthy", False) is True and svc is not None:
            return svc
    except Exception:
        pass
    try:
        return get_prediction_service()
    except Exception:
        return None


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Health Check",
    description="Check if the API and ML model are running correctly",
    tags=["Health"]
)
async def health_check(request: Request) -> HealthResponse:
    """
    Perform health check on the API service.
    
    Returns
    -------
    HealthResponse
        Service health status
    """
    try:
        svc = get_service(request)
        model_loaded = bool(svc is not None and svc.is_loaded())
        if not model_loaded:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="API is running, but machine learning models are unavailable."
            )
        return HealthResponse(
            status="healthy",
            model_loaded=True,
            version=settings.API_VERSION
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="API is running, but machine learning models are unavailable."
        )


@router.get(
    "/model/info",
    response_model=ModelInfo,
    summary="Model Information",
    description="Get detailed information about the ML model",
    tags=["Model"]
)
async def get_model_info(request: Request) -> ModelInfo:
    """
    Get ML model metadata and performance metrics.
    
    Returns
    -------
    ModelInfo
        Model information and metrics
    """
    try:
        svc_tmp = get_service(request)
        if svc_tmp is None or not svc_tmp.is_loaded():
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Model not loaded"
            )
        
        return ModelInfo(**svc_tmp.get_model_info())
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get model info: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve model information"
        )


@router.post(
    "/predict",
    response_model=PredictionResponse,
    summary="Single Prediction",
    description="Predict acquisition price for a single startup",
    tags=["Prediction"],
    status_code=status.HTTP_200_OK
)
async def predict_single(data: InferredPredictItem, request: Request) -> PredictionResponse:
    """
    Make a prediction for a single profile.

    Accepts either a StartupData payload (payload_type='startup', the common
    case - a flat JSON object) or a DowryData payload
    (payload_type='dowry'). Empty objects {} fail with 422 via the
    discriminated union (Phase 4 validation check).

    Parameters
    ----------
    data : Union[StartupData, DowryData]
        Validated profile information (discriminated by payload_type)
    
    Returns
    -------
    PredictionResponse
        Prediction result with price estimate and confidence
    
    Raises
    ------
    HTTPException
        If prediction fails or model is not loaded
    """
    try:
        svc2 = get_service(request)
        if svc2 is None or not svc2.is_loaded():
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Prediction engine offline."
            )
        
        # Make prediction (dump pydantic model to plain dict first)
        payload = data.model_dump() if hasattr(data, "model_dump") else data
        result = svc2.predict_single(payload)
        
        logger.info(
            f"Prediction: ₹{result['predicted_acquisition_price_inr']:,} "
            f"(confidence: {result['confidence_score']:.4f})"
        )
        
        return PredictionResponse(
            success=True,
            data=result,
            message="Prediction successful"
        )
        
    except HTTPException:
        raise
    except ValueError as e:
        logger.warning(f"Validation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Prediction failed. Please check your input data."
        )


@router.post(
    "/predict/batch",
    response_model=BatchPredictionResponse,
    summary="Batch Prediction",
    description="Predict valuations for multiple profiles (max 100)",
    tags=["Prediction"],
    status_code=status.HTTP_200_OK
)
async def predict_batch(payload: BatchPredictionRequest, request: Request) -> BatchPredictionResponse:
    """
    Make predictions for multiple profiles.
    
    Parameters
    ----------
    request : BatchPredictionRequest
        List of profile data (max 100)
    
    Returns
    -------
    BatchPredictionResponse
        Batch prediction results with statistics
    
    Raises
    ------
    HTTPException
        If prediction fails or model is not loaded
    """
    try:
        svc3 = get_service(request)
        if svc3 is None or not svc3.is_loaded():
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Prediction engine offline."
            )
        
        # Get items from request (supporting both 'items' and 'startups' fields)
        items = payload.items or payload.startups or []
        
        # Validate batch size
        if len(items) == 0:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Batch must contain at least 1 item"
            )
        if len(items) > 100:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Maximum 100 items allowed per batch"
            )
        
        # Make predictions (dump pydantic models to plain dicts first)
        items = payload.items or payload.startups or []
        payloads = [
            it.model_dump() if hasattr(it, "model_dump") else it for it in items
        ]
        result = svc3.predict_batch(payloads)
        
        logger.info(
            f"Batch prediction completed: {result['total_count']} items, "
            f"avg price: ₹{result['average_acquisition_price']:,}"
        )
        
        return BatchPredictionResponse(
            success=True,
            data=result,
            message=f"Batch prediction completed for {result['total_count']} items"
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Batch prediction failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Batch prediction failed. Please check your input data."
        )


@router.get(
    "/",
    summary="API Root",
    description="Welcome endpoint with API information",
    tags=["Info"]
)
async def root() -> Dict:
    """
    API root endpoint.
    
    Returns
    -------
    Dict
        Welcome message and API links
    """
    return {
        "message": "Welcome to Startup Acquisition Valuation API",
        "version": settings.API_VERSION,
        "documentation": {
            "swagger_ui": "/docs",
            "redoc": "/redoc",
            "openapi_json": "/openapi.json"
        },
        "endpoints": {
            "health": "/health",
            "model_info": "/model/info",
            "predict": "/predict",
            "batch_predict": "/predict/batch"
        }
    }
