import pytest

from libreone.system.device_registry import DeviceRegistry
from libreone.system.devices import Device, DeviceType


def test_device_registry_rejects_duplicate_id():
    registry = DeviceRegistry()
    registry.register(Device("cpu0", DeviceType.CPU))
    with pytest.raises(Exception):
        registry.register(Device("cpu0", DeviceType.CPU))
