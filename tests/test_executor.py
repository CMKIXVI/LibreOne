import pytest

from libreone.system.executor import Executor


def test_executor_returns_callable_result():
    assert Executor().execute(lambda: 7) == 7


def test_executor_propagates_operation_failure():
    def operation() -> None:
        raise ValueError("boom")

    with pytest.raises(ValueError, match="boom"):
        Executor().execute(operation)


def test_executor_rejects_non_callable_operation():
    with pytest.raises(TypeError, match="operation must be callable"):
        Executor().execute(None)  # type: ignore[arg-type]
