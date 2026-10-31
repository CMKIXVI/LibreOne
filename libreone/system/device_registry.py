from .devices import Device


class DeviceRegistry:
    def __init__(self) -> None:
        self._devices: dict[str, Device] = {}

    def register(self, device: Device) -> None:
        if not isinstance(device, Device):
            raise TypeError("device must be a Device")
        key = device.name
        if key in self._devices:
            raise ValueError(f"device already registered: {key}")
        self._devices[key] = device

    def get(self, name: str) -> Device:
        if not isinstance(name, str):
            raise TypeError("device name must be a string")
        key = name.strip()
        if not key:
            raise ValueError("device name cannot be empty")
        return self._devices[key]

    def __contains__(self, name: object) -> bool:
        return isinstance(name, str) and bool(name.strip()) and name.strip() in self._devices

    def all(self) -> tuple[Device, ...]:
        return tuple(self._devices.values())
