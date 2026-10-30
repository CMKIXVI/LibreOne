from libreone.system.devices import Device, DeviceType


def verify_device_contract() -> bool:
    device = Device("cpu0", DeviceType.CPU)
    return device.device_type is DeviceType.CPU
