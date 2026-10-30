from libreone.system.devices import DeviceType


def test_device_type_values_are_unique():
    values = [item.value for item in DeviceType]
    assert len(values) == len(set(values))
