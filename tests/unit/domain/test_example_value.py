import pytest

from common.domain.example_value import ExampleValue
from common.domain.exceptions import DomainValueError


def test_greeting_includes_name():
    value = ExampleValue(name="Clean Architecture")

    assert value.greeting() == "Hello, Clean Architecture!"


def test_example_value_requires_non_empty_name():
    with pytest.raises(DomainValueError):
        ExampleValue(name=" ")
