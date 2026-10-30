import pytest

from libreone.system.resources import ResourceLimits


def test_resource_limits_accept_valid_values():
    limits = ResourceLimits(cpu_seconds=1.0, memory_bytes=1024, disk_bytes=2048, wall_seconds=2.0)
    assert limits.memory_bytes == 1024


def test_resource_limits_reject_negative_values():
    with pytest.raises(ValueError):
        ResourceLimits(memory_bytes=-1)


def test_resource_limits_reject_boolean_numeric_values():
    with pytest.raises(TypeError):
        ResourceLimits(cpu_seconds=True)


def test_resource_limits_require_integer_storage_limits():
    with pytest.raises(TypeError):
        ResourceLimits(memory_bytes=1024.5)
    with pytest.raises(TypeError):
        ResourceLimits(disk_bytes=2048.5)
