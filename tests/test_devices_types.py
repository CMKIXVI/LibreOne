from libreone.system.devices import DeviceType


def test_device_types_include_core_classes():
    assert DeviceType.CPU.value == "cpu"
    assert DeviceType.STORAGE.value == "storage"
    assert DeviceType.ACCELERATOR.value == "accelerator"
