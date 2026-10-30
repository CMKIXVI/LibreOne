import pytest

from libreone.system.resources import ResourceLimits


def test_resource_limits_reject_negative_cpu():
    with pytest.raises(ValueError):
        ResourceLimits(cpu_seconds=-0.1)


def test_resource_limits_reject_negative_wall_time():
    with pytest.raises(ValueError):
        ResourceLimits(wall_seconds=-0.1)
