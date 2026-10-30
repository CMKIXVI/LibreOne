import pytest

from libreone.system.resources import ResourceLimits


def test_resource_limits_type_validation():
    with pytest.raises((TypeError, ValueError)):
        ResourceLimits(memory_bytes="invalid")
