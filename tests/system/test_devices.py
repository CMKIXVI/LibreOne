from libreone.system.device_registry import DeviceRegistry
from libreone.system.devices import Device, DeviceType


def test_device_registry():
    device = Device("cpu0", DeviceType.CPU)
    registry = DeviceRegistry()
    registry.register(device)
    assert registry.get("cpu0") == device
