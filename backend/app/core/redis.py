import time
from typing import Any

import redis.asyncio as aioredis

from app.core.config import get_settings

_redis_client: aioredis.Redis | None = None


def get_redis_client() -> aioredis.Redis:
    """Return a shared async Redis client instance."""
    global _redis_client
    if _redis_client is None:
        settings = get_settings()
        _redis_client = aioredis.from_url(
            settings.REDIS_URL,
            encoding="utf-8",
            decode_responses=True,
        )
    return _redis_client


async def close_redis_client() -> None:
    """Close the shared async Redis client."""
    global _redis_client
    if _redis_client is not None:
        await _redis_client.aclose()
        _redis_client = None


async def check_redis_health() -> dict[str, Any]:
    """Verify Redis connectivity with PING."""
    start = time.perf_counter()
    try:
        client = get_redis_client()
        pong = await client.ping()
        latency_ms = round((time.perf_counter() - start) * 1000, 2)
        return {
            "status": "healthy" if pong else "unhealthy",
            "latency_ms": latency_ms,
        }
    except Exception as exc:
        latency_ms = round((time.perf_counter() - start) * 1000, 2)
        return {
            "status": "unhealthy",
            "latency_ms": latency_ms,
            "error": str(exc),
        }
