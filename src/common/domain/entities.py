from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .core import DomainError


class AssetType(Enum):
    STOCK = "stock"
    ETF = "etf"
    BOND = "bond"
    CRYPTO = "crypto"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.value


@dataclass(frozen=True)
class Exchange:
    id: str
    name: str
    timezone: str

    def __post_init__(self) -> None:
        if not self.id or not self.id.strip():
            raise DomainError("Exchange id must be non-empty")

        if not self.name or not self.name.strip():
            raise DomainError("Exchange name must be non-empty")

        if not self.timezone or not self.timezone.strip():
            raise DomainError("Exchange timezone must be non-empty")


@dataclass(frozen=True)
class Asset:
    symbol: str
    name: str
    exchange: Exchange
    asset_type: AssetType

    def __post_init__(self) -> None:
        if not self.symbol or not self.symbol.strip():
            raise DomainError("Asset symbol must be non-empty")

        if not self.name or not self.name.strip():
            raise DomainError("Asset name must be non-empty")

        if not isinstance(self.exchange, Exchange):
            raise DomainError("Asset exchange must be an Exchange instance")

        if isinstance(self.asset_type, str):
            try:
                object.__setattr__(
                    self, "asset_type", AssetType(self.asset_type.lower())
                )
            except ValueError as error:
                raise DomainError("Invalid asset type") from error
        elif not isinstance(self.asset_type, AssetType):
            raise DomainError("Asset type must be an AssetType or valid string")


__all__ = ["Exchange", "Asset", "AssetType"]
