from libreone.system.devices import Device, DeviceType


def test_device_types_cover_core_classes():
    assert {DeviceType.CPU, DeviceType.MEMORY, DeviceType.STORAGE, DeviceType.NETWORK, DeviceType.DISPLAY, DeviceType.ACCELERATOR}
    assert Device("gpu0", DeviceType.ACCELERATOR).device_type is DeviceType.ACCELERATOR
