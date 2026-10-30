import pytest

from libreone.system.timeout import Timeout


def test_timeout_rejects_negative_values():
    with pytest.raises(ValueError):
        Timeout(-1)
