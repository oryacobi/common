import pytest

from common.domain import Asset, AssetType, DomainError, Exchange


def test_create_valid_exchange_and_asset():
    exchange = Exchange(
        id="NYSE", name="New York Stock Exchange", timezone="America/New_York"
    )
    asset = Asset(
        symbol="AAPL",
        name="Apple Inc.",
        exchange=exchange,
        asset_type=AssetType.STOCK,
    )

    assert asset.symbol == "AAPL"
    assert asset.exchange is exchange
    assert asset.asset_type == AssetType.STOCK


def test_asset_accepts_string_asset_type():
    exchange = Exchange(id="NASDAQ", name="Nasdaq", timezone="America/New_York")
    asset = Asset(symbol="QQQ", name="Invesco QQQ", exchange=exchange, asset_type="etf")

    assert asset.asset_type is AssetType.ETF


def test_exchange_requires_non_empty_fields():
    with pytest.raises(DomainError):
        Exchange(id="", name="Test", timezone="UTC")
    with pytest.raises(DomainError):
        Exchange(id="XNAS", name="   ", timezone="UTC")
    with pytest.raises(DomainError):
        Exchange(id="XNAS", name="Nasdaq", timezone=" ")


def test_asset_requires_valid_inputs():
    exchange = Exchange(
        id="LSE", name="London Stock Exchange", timezone="Europe/London"
    )

    with pytest.raises(DomainError):
        Asset(symbol="", name="Test", exchange=exchange, asset_type=AssetType.STOCK)

    with pytest.raises(DomainError):
        Asset(symbol="VOD", name="", exchange=exchange, asset_type=AssetType.STOCK)

    with pytest.raises(DomainError):
        Asset(
            symbol="VOD",
            name="Vodafone",
            exchange="not exchange",
            asset_type=AssetType.STOCK,
        )

    with pytest.raises(DomainError):
        Asset(symbol="VOD", name="Vodafone", exchange=exchange, asset_type="invalid")

    with pytest.raises(DomainError):
        Asset(symbol="VOD", name="Vodafone", exchange=exchange, asset_type=123)
