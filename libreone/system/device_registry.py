from .devices import Device


class DeviceRegistry:
    def __init__(self) -> None:
        self._devices: dict[str, Device] = {}

    def register(self, device: Device) -> None:
        if device.name in self._devices:
            raise ValueError(f"device already registered: {device.name}")
        self._devices[device.name] = device

    def get(self, name: str) -> Device:
        return self._devices[name]

    def all(self) -> tuple[Device, ...]:
        return tuple(self._devices.values())
