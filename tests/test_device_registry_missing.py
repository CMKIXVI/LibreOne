import pytest
from libreone.system.device_registry import DeviceRegistry


def test_missing_device_is_not_returned():
    registry = DeviceRegistry()
    with pytest.raises(KeyError):
        registry.get("missing")
