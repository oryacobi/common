import pytest

from common.domain.core import (
    CommonError,
    DomainError,
    Err,
    InfrastructureError,
    Ok,
    Result,
)


def test_ok_result_represents_success():
    result: Result[str, Exception] = Ok("value")

    assert result.is_ok()
    assert not result.is_err()
    assert result.unwrap() == "value"
    with pytest.raises(ValueError):
        result.unwrap_err()
    assert bool(result) is True


def test_err_result_represents_failure():
    error = DomainError("problem")
    result: Result[str, DomainError] = Err(error)

    assert not result.is_ok()
    assert result.is_err()
    assert result.unwrap_err() is error
    assert bool(result) is False

    with pytest.raises(DomainError):
        result.unwrap()


def test_base_exceptions_form_hierarchy():
    assert issubclass(DomainError, CommonError)
    assert issubclass(InfrastructureError, CommonError)

    with pytest.raises(CommonError):
        raise DomainError("domain issue")

    with pytest.raises(CommonError):
        raise InfrastructureError("infrastructure issue")
