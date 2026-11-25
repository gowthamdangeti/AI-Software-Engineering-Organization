from datetime import datetime, timezone
from typing import Any

from fastapi import APIRouter, Response, status

from app.core.config import get_settings
from app.core.database import check_database_health
from app.core.redis import check_redis_health
from app.core.storage import check_minio_health

router = APIRouter(tags=["Health"])


@router.get("/health")
async def liveness() -> dict[str, Any]:
    """Basic liveness probe for the API service."""
    settings = get_settings()
    return {
        "status": "ok",
        "service": "backend",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.APP_ENV,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@router.get("/health/ready")
async def readiness(response: Response) -> dict[str, Any]:
    """Readiness probe verifying PostgreSQL, Redis, and MinIO connectivity."""
    settings = get_settings()
    db_status = await check_database_health()
    redis_status = await check_redis_health()
    minio_status = await check_minio_health()

    dependencies = {
        "postgres": db_status,
        "redis": redis_status,
        "minio": minio_status,
    }
    all_healthy = all(dep["status"] == "healthy" for dep in dependencies.values())

    if not all_healthy:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

    return {
        "status": "ready" if all_healthy else "degraded",
        "service": "backend",
        "version": settings.APP_VERSION,
        "environment": settings.APP_ENV,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "dependencies": dependencies,
    }
