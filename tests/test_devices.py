import pytest

from libreone.system.device_registry import DeviceRegistry
from libreone.system.devices import Device, DeviceType


def test_device_registry_round_trip():
    registry = DeviceRegistry()
    device = Device(" cpu0 ", DeviceType.CPU, vendor=" Example ", address=" 0000:00:00.0 ")
    registry.register(device)
    assert registry.get("cpu0") == device
    assert device.name == "cpu0"
    assert device.vendor == "Example"
    assert device.address == "0000:00:00.0"


def test_device_rejects_invalid_identity():
    with pytest.raises(TypeError):
        Device(123, DeviceType.CPU)
    with pytest.raises(ValueError):
        Device("   ", DeviceType.CPU)
    with pytest.raises(TypeError):
        Device("cpu0", "cpu")
    with pytest.raises(TypeError):
        Device("cpu0", DeviceType.CPU, vendor=123)


def test_device_registry_rejects_invalid_registration_and_lookup():
    registry = DeviceRegistry()
    with pytest.raises(TypeError):
        registry.register(object())
    with pytest.raises(TypeError):
        registry.get(123)
    with pytest.raises(ValueError):
        registry.get("   ")


def test_device_registry_rejects_duplicates_and_supports_contains():
    registry = DeviceRegistry()
    registry.register(Device("cpu0", DeviceType.CPU))
    with pytest.raises(ValueError):
        registry.register(Device(" cpu0 ", DeviceType.CPU))
    assert " cpu0 " in registry
    assert "cpu1" not in registry
    assert 123 not in registry
