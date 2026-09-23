"""
Main Application

FastAPI application setup and configuration.
"""

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from contextlib import asynccontextmanager
import logging
from pathlib import Path

from app.core.config import settings
from app.api.endpoints import router
from app.schemas.response import ErrorResponse

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup/shutdown lifespan with resilient model loading (Phase 5).

    Attempts to load ML models into ``app.state`` but never raises, so
    the API always boots and ``/health`` can report 503 instead of the
    process crash-looping when ``models/`` is missing.
    """
    # --- Startup Phase ---
    try:
        from app.services.prediction_service import PredictionService
        app.state.prediction_service = PredictionService()
        app.state.models_healthy = True
        logger.info("Models loaded successfully into application state.")
        print("Models loaded successfully into application state.")
    except Exception as e:
        logger.error(f"CRITICAL: Failed to load ML models. {str(e)}")
        print(f"CRITICAL: Failed to load ML models. {str(e)}")
        app.state.prediction_service = None
        app.state.models_healthy = False
        # Do not raise: let the API start so /health can report 503.

    yield  # App runs here

    # --- Shutdown Phase ---
    app.state.prediction_service = None
    app.state.models_healthy = False


# Create FastAPI application
app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

# Configure CORS - explicit origins from settings (fixes browser CORS errors).
# The middleware echoes back ONLY a matching Origin; the frontend dev server
# (Vite :5173 / TanStack Start :3000/:3001) must be listed in ALLOWED_ORIGINS.
# Set ALLOW_ALL_ORIGINS=true in env only as a temporary bypass (dev only).
_cors_origins = ["*"] if settings.ALLOW_ALL_ORIGINS else settings.ALLOWED_ORIGINS
app.add_middleware(
    CORSMiddleware,
    allow_origins=_cors_origins,
    allow_credentials=("*" not in _cors_origins),
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(router)


# Exception handlers
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """
    Catch-all exception handler that prevents stack trace leakage in production.
    """
    logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)

    # Only expose the actual error string if DEBUG mode is strictly True
    error_detail = str(exc) if settings.DEBUG else "An internal server error occurred."

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "success": False,
            "error": "Internal Server Error",
            "message": error_detail
        }
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Handle validation errors.
    
    Parameters
    ----------
    request : Request
        The incoming request
    exc : RequestValidationError
        The validation error
    
    Returns
    -------
    JSONResponse
        Error response with validation details
    """
    errors = []
    for error in exc.errors():
        errors.append({
            "field": ".".join(str(loc) for loc in error["loc"]),
            "message": error["msg"],
            "type": error["type"]
        })
    
    logger.warning(f"Validation error: {errors}")
    
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "success": False,
            "error": "ValidationError",
            "message": "Invalid input data",
            "details": errors
        }
    )


# Logging-only startup/shutdown hooks (lifespan owns model loading, so the
# app always boots even when models are missing).
@app.on_event("startup")
async def startup_event():
    """Execute on application startup (logging only)."""
    logger.info("=" * 80)
    logger.info(f"Starting {settings.API_TITLE} v{settings.API_VERSION}")
    logger.info(f"Environment: {settings.ENVIRONMENT}")
    logger.info(f"Debug mode: {settings.DEBUG}")
    logger.info("=" * 80)
    
    # Verify model file exists
    model_path = Path(settings.MODEL_PATH)
    if model_path.exists():
        logger.info(f"✓ Model file found: {model_path}")
    else:
        logger.error(f"✗ Model file not found: {model_path}")
        logger.error("Please ensure trained_models.pkl is in the models directory")
    
    logger.info("Application startup complete")


@app.on_event("shutdown")
async def shutdown_event():
    """Execute on application shutdown."""
    logger.info("Shutting down application...")
    logger.info("Goodbye!")


# Health check at root level
@app.get("/ping")
async def ping():
    """Simple ping endpoint."""
    return {"status": "pong"}


if __name__ == "__main__":
    import uvicorn
    
    logger.info(f"Starting server on {settings.API_HOST}:{settings.API_PORT}")
    
    uvicorn.run(
        "app.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower()
    )
