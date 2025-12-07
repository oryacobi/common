from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from enum import Enum

from .exceptions import DomainValueError


class Currency(Enum):
    USD = "USD"
    EUR = "EUR"
    ILS = "ILS"
    GBP = "GBP"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.value


@dataclass(frozen=True)
class Money:
    amount: Decimal
    currency: Currency

    def __post_init__(self) -> None:
        try:
            coerced_amount = (
                self.amount
                if isinstance(self.amount, Decimal)
                else Decimal(str(self.amount))
            )
        except (InvalidOperation, ValueError, TypeError) as error:
            raise DomainValueError(
                "amount must be a number convertible to Decimal"
            ) from error

        if not isinstance(self.currency, Currency):
            raise DomainValueError("currency must be an instance of Currency")

        object.__setattr__(self, "amount", coerced_amount)

    def _assert_same_currency(self, other: Money) -> None:
        if self.currency != other.currency:
            raise DomainValueError(
                f"Currency mismatch: {self.currency.value} vs {other.currency.value}"
            )

    def __add__(self, other: Money) -> Money:
        if not isinstance(other, Money):
            return NotImplemented

        self._assert_same_currency(other)
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other: Money) -> Money:
        if not isinstance(other, Money):
            return NotImplemented

        self._assert_same_currency(other)
        return Money(self.amount - other.amount, self.currency)

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.amount} {self.currency.value}"


__all__ = ["Currency", "Money"]
