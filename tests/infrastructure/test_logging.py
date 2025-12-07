"""Tests for logging utilities."""

import logging

from common.infrastructure.logging import get_logger


def test_get_logger_emits_messages(caplog):
    logger = get_logger(__name__)
    message = "hello from logging"

    with caplog.at_level(logging.INFO, logger=logger.name):
        logger.info(message)

    assert message in caplog.text
    assert any(record.name == logger.name for record in caplog.records)


def test_get_logger_is_safe_to_call_multiple_times():
    first_logger = get_logger("first")
    second_logger = get_logger("second")

    assert first_logger.name == "first"
    assert second_logger.name == "second"
