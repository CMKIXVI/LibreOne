from libreone.system.device_registry import DeviceRegistry
from libreone.system.devices import Device, DeviceType


def verify_device_registry_contract() -> bool:
    registry = DeviceRegistry()
    device = Device("cpu0", DeviceType.CPU)
    registry.register(device)
    return registry.get("cpu0") == device
