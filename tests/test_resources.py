import pytest

from libreone.system.resources import ResourceLimits


def test_resource_limits_default_validates():
    ResourceLimits().validate()


def test_resource_limits_accepts_zero():
    ResourceLimits(cpu_seconds=0, memory_bytes=0, disk_bytes=0, wall_seconds=0).validate()


def test_resource_limits_rejects_negative_values():
    with pytest.raises(ValueError):
        ResourceLimits(cpu_seconds=-1).validate()
    with pytest.raises(ValueError):
        ResourceLimits(memory_bytes=-1).validate()
    with pytest.raises(ValueError):
        ResourceLimits(disk_bytes=-1).validate()
    with pytest.raises(ValueError):
        ResourceLimits(wall_seconds=-1).validate()


def test_resource_limits_is_immutable():
    limits = ResourceLimits(cpu_seconds=1)
    with pytest.raises(Exception):
        limits.cpu_seconds = 2
