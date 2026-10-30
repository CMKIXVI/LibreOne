import pytest

from libreone.system.limits import ConcurrencyLimit


def test_concurrency_limit_rejects_zero():
    with pytest.raises(ValueError):
        ConcurrencyLimit(0)
