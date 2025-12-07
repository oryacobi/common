"""Tests for configuration utilities."""

import pytest

from common.infrastructure.config import get_env_var
from common.domain import InfrastructureError


def test_get_env_var_returns_value(monkeypatch):
    monkeypatch.setenv("TEST_ENV_VAR", "expected")

    assert get_env_var("TEST_ENV_VAR") == "expected"


def test_get_env_var_returns_default_when_missing(monkeypatch):
    monkeypatch.delenv("MISSING_ENV", raising=False)

    assert get_env_var("MISSING_ENV", default="fallback") == "fallback"


def test_get_env_var_raises_when_missing_without_default(monkeypatch):
    monkeypatch.delenv("REQUIRED_ENV", raising=False)

    with pytest.raises(InfrastructureError) as exc_info:
        get_env_var("REQUIRED_ENV")

    assert "Missing required environment variable: REQUIRED_ENV" == str(exc_info.value)
