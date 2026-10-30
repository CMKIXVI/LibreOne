import pytest
from libreone.system.resources import ResourceLimits


def test_resource_limits_are_immutable():
    limits = ResourceLimits()
    with pytest.raises(Exception):
        limits.cpu_seconds = 10
