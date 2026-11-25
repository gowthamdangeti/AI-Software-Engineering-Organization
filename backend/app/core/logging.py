import logging
import sys

from app.core.config import get_settings


def configure_logging() -> None:
    """Configure structured application logging."""
    settings = get_settings()
    level = getattr(logging, settings.LOG_LEVEL, logging.INFO)

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        stream=sys.stdout,
        force=True,
    )
