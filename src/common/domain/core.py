"""Core domain utilities for expressing success and failure."""
from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")
E = TypeVar("E")


class CommonError(Exception):
    """Base exception for common library errors."""


class DomainError(CommonError):
    """Base exception for domain-layer errors."""


class InfrastructureError(CommonError):
    """Base exception for infrastructure-layer errors."""


class Result(Generic[T, E]):
    """Represents either a success (``Ok``) or failure (``Err``)."""

    __slots__ = ()

    def is_ok(self) -> bool:
        """Return ``True`` when the result represents success."""

        raise NotImplementedError

    def is_err(self) -> bool:
        """Return ``True`` when the result represents failure."""

        return not self.is_ok()

    def unwrap(self) -> T:
        """Return the contained value, raising if this is an ``Err``."""

        raise NotImplementedError

    def unwrap_err(self) -> E:
        """Return the contained error, raising if this is an ``Ok``."""

        raise NotImplementedError

    def __bool__(self) -> bool:  # pragma: no cover - trivial
        return self.is_ok()


class Ok(Result[T, E]):
    """Represents a successful result."""

    __slots__ = ("value",)

    def __init__(self, value: T):
        self.value = value

    def is_ok(self) -> bool:
        return True

    def unwrap(self) -> T:
        return self.value

    def unwrap_err(self) -> E:
        raise ValueError("Cannot unwrap_err from Ok")

    def __repr__(self) -> str:  # pragma: no cover - representation
        return f"Ok({self.value!r})"

    def __eq__(self, other: object) -> bool:  # pragma: no cover - convenience
        return isinstance(other, Ok) and self.value == other.value


class Err(Result[T, E]):
    """Represents a failed result."""

    __slots__ = ("error",)

    def __init__(self, error: E):
        self.error = error

    def is_ok(self) -> bool:
        return False

    def unwrap(self) -> T:
        if isinstance(self.error, Exception):
            raise self.error
        raise RuntimeError(self.error)

    def unwrap_err(self) -> E:
        return self.error

    def __repr__(self) -> str:  # pragma: no cover - representation
        return f"Err({self.error!r})"

    def __eq__(self, other: object) -> bool:  # pragma: no cover - convenience
        return isinstance(other, Err) and self.error == other.error


__all__ = [
    "CommonError",
    "DomainError",
    "InfrastructureError",
    "Result",
    "Ok",
    "Err",
]
