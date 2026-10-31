import math

import pytest

from libreone.system.timeout import Timeout


def test_timeout_accepts_positive_finite_values():
    assert Timeout(1).seconds == 1
    assert Timeout(0.5).seconds == 0.5


def test_timeout_rejects_boolean_values():
    with pytest.raises(TypeError, match="timeout must be numeric"):
        Timeout(True)


def test_timeout_rejects_non_finite_values():
    for value in (math.inf, -math.inf, math.nan):
        with pytest.raises(ValueError, match="timeout must be finite"):
            Timeout(value)


def test_timeout_rejects_non_positive_values():
    with pytest.raises(ValueError, match="timeout must be positive"):
        Timeout(0)
    with pytest.raises(ValueError, match="timeout must be positive"):
        Timeout(-1)
