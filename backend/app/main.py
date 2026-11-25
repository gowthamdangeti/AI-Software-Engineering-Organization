import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.api.v1.health import router as health_router
from app.core.config import get_settings
from app.core.database import engine
from app.core.logging import configure_logging
from app.core.redis import close_redis_client
from app.core.storage import ensure_default_bucket

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage startup and shutdown of infrastructure connections."""
    configure_logging()
    logger.info("Starting AI-Native Software Engineering Organization backend...")
    try:
        await ensure_default_bucket()
        logger.info("MinIO default bucket verified.")
    except Exception as exc:
        logger.warning("MinIO bucket check skipped during startup: %s", exc)

    yield

    logger.info("Shutting down backend resources...")
    await close_redis_client()
    await engine.dispose()


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Root-level health routes and versioned API routes
    app.include_router(health_router)
    app.include_router(api_router, prefix=settings.API_V1_PREFIX)

    return app


app = create_app()
