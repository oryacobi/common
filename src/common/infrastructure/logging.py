"""Logging helpers for infrastructure modules."""

from __future__ import annotations

import logging

_DEFAULT_LOG_FORMAT = "%(asctime)s %(levelname)s [%(name)s] %(message)s"


def _configure_root_logger() -> None:
    """Set up a basic configuration for the root logger if missing."""

    root_logger = logging.getLogger()
    if root_logger.handlers:
        return

    logging.basicConfig(level=logging.INFO, format=_DEFAULT_LOG_FORMAT)


def get_logger(name: str) -> logging.Logger:
    """Return a logger with standard configuration applied.

    Args:
        name: The name of the logger to retrieve.

    Returns:
        A configured ``logging.Logger`` instance.
    """

    _configure_root_logger()
    return logging.getLogger(name)


__all__ = ["get_logger"]
