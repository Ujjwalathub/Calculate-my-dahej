"""
Application Runner

Simple script to start the FastAPI server.
"""

import uvicorn
from app.core.config import settings

if __name__ == "__main__":
    print("=" * 80)
    print(f"Starting {settings.API_TITLE}")
    print(f"Version: {settings.API_VERSION}")
    print(f"Environment: {settings.ENVIRONMENT}")
    print("=" * 80)
    print(f"\nServer will start at: http://{settings.API_HOST}:{settings.API_PORT}")
    print(f"API Documentation: http://{settings.API_HOST}:{settings.API_PORT}/docs")
    print(f"ReDoc: http://{settings.API_HOST}:{settings.API_PORT}/redoc")
    print("\nPress CTRL+C to stop the server\n")
    print("=" * 80)
    
    uvicorn.run(
        "app.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower()
    )
