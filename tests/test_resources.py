import pytest

from libreone.system.resources import ResourceLimits


def test_resource_limits_default_validates():
    ResourceLimits().validate()


def test_resource_limits_rejects_non_positive_values():
    with pytest.raises(ValueError):
        ResourceLimits(cpu_seconds=0).validate()
