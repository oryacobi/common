from decimal import Decimal

import pytest

from common.domain import Currency, DomainValueError, Money


def test_money_addition_with_matching_currency():
    usd_ten = Money(Decimal("10.00"), Currency.USD)
    usd_five = Money(Decimal("5.50"), Currency.USD)

    result = usd_ten + usd_five

    assert result.amount == Decimal("15.50")
    assert result.currency is Currency.USD


def test_money_addition_with_mismatched_currency_raises_error():
    usd_value = Money(Decimal("1.00"), Currency.USD)
    eur_value = Money(Decimal("1.00"), Currency.EUR)

    with pytest.raises(DomainValueError, match="Currency mismatch"):
        _ = usd_value + eur_value


def test_money_equality_relies_on_amount_and_currency():
    usd_one = Money(Decimal("1.00"), Currency.USD)
    usd_one_again = Money(Decimal(1), Currency.USD)
    eur_one = Money(Decimal("1.00"), Currency.EUR)
    usd_two = Money(Decimal("2.00"), Currency.USD)

    assert usd_one == usd_one_again
    assert usd_one != eur_one
    assert usd_one != usd_two
