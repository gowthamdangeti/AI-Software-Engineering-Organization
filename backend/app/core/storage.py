import asyncio
import time
from typing import Any

from minio import Minio

from app.core.config import get_settings

_minio_client: Minio | None = None


def get_minio_client() -> Minio:
    """Return a shared MinIO client instance."""
    global _minio_client
    if _minio_client is None:
        settings = get_settings()
        _minio_client = Minio(
            settings.MINIO_ENDPOINT,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            secure=settings.MINIO_SECURE,
        )
    return _minio_client


def _ensure_bucket_sync(bucket_name: str) -> bool:
    client = get_minio_client()
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
    return True


async def ensure_default_bucket() -> None:
    """Ensure the default artifact bucket exists in MinIO."""
    settings = get_settings()
    await asyncio.to_thread(_ensure_bucket_sync, settings.MINIO_BUCKET)


def _check_minio_sync(bucket_name: str) -> bool:
    client = get_minio_client()
    return client.bucket_exists(bucket_name)


async def check_minio_health() -> dict[str, Any]:
    """Verify MinIO connectivity and default bucket availability."""
    settings = get_settings()
    start = time.perf_counter()
    try:
        bucket_exists = await asyncio.to_thread(_check_minio_sync, settings.MINIO_BUCKET)
        latency_ms = round((time.perf_counter() - start) * 1000, 2)
        return {
            "status": "healthy",
            "latency_ms": latency_ms,
            "bucket": settings.MINIO_BUCKET,
            "bucket_exists": bucket_exists,
        }
    except Exception as exc:
        latency_ms = round((time.perf_counter() - start) * 1000, 2)
        return {
            "status": "unhealthy",
            "latency_ms": latency_ms,
            "error": str(exc),
        }
