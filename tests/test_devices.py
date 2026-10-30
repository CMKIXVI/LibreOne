from libreone.system.device_registry import DeviceRegistry
from libreone.system.devices import Device, DeviceType


def test_device_registry_round_trip():
    registry = DeviceRegistry()
    device = Device("cpu0", DeviceType.CPU)
    registry.register(device)
    assert registry.get("cpu0") == device
