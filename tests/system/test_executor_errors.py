import pytest

from libreone.system.executor import Executor


def test_executor_propagates_failure():
    def fail():
        raise ValueError("failure")

    with pytest.raises(ValueError, match="failure"):
        Executor().execute(fail)
