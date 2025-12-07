"""Basic smoke tests for the common package."""


def test_import_common():
    import common

    assert common is not None


def test_truthiness():
    assert True is True
