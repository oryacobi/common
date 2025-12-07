"""Configuration helpers for infrastructure components."""

from __future__ import annotations

import os
from typing import Optional

from common.domain import InfrastructureError


def get_env_var(name: str, default: Optional[str] = None) -> str:
    """Return the value of an environment variable.

    Args:
        name: The environment variable name to read.
        default: Optional fallback when the variable is not set.

    Raises:
        InfrastructureError: If the variable is missing and no default is provided.

    Returns:
        The environment variable's value or the provided default.
    """

    value = os.environ.get(name)
    if value is not None:
        return value

    if default is not None:
        return default

    raise InfrastructureError(f"Missing required environment variable: {name}")


__all__ = ["get_env_var"]
