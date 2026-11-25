import logging
from typing import Any

from arq.connections import RedisSettings

from app.core.config import get_settings

logger = logging.getLogger(__name__)


async def ping_task(ctx: dict[str, Any]) -> str:
    """Simple health task for verifying ARQ worker execution."""
    logger.info("ARQ ping_task executed.")
    return "pong"


async def startup(ctx: dict[str, Any]) -> None:
    logger.info("ARQ worker starting up.")


async def shutdown(ctx: dict[str, Any]) -> None:
    logger.info("ARQ worker shutting down.")


def get_redis_settings() -> RedisSettings:
    settings = get_settings()
    return RedisSettings(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        database=settings.REDIS_DB,
    )


class WorkerSettings:
    functions = [ping_task]
    on_startup = startup
    on_shutdown = shutdown
    redis_settings = get_redis_settings()
