from dataclasses import dataclass
from enum import Enum


class DeviceType(str, Enum):
    CPU = "cpu"
    MEMORY = "memory"
    STORAGE = "storage"
    NETWORK = "network"
    DISPLAY = "display"
    ACCELERATOR = "accelerator"


@dataclass(frozen=True)
class Device:
    name: str
    kind: DeviceType
    vendor: str | None = None
    address: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.name, str):
            raise TypeError("device name must be a string")
        name = self.name.strip()
        if not name:
            raise ValueError("device name cannot be empty")
        if len(name) > 255:
            raise ValueError("device name is too long")
        if not isinstance(self.kind, DeviceType):
            raise TypeError("device kind must be a DeviceType")
        for field_name, value in (("vendor", self.vendor), ("address", self.address)):
            if value is not None and not isinstance(value, str):
                raise TypeError(f"device {field_name} must be a string or None")
            if isinstance(value, str) and len(value) > 255:
                raise ValueError(f"device {field_name} is too long")
        object.__setattr__(self, "name", name)
        if isinstance(self.vendor, str):
            object.__setattr__(self, "vendor", self.vendor.strip() or None)
        if isinstance(self.address, str):
            object.__setattr__(self, "address", self.address.strip() or None)

    @property
    def device_type(self) -> DeviceType:
        return self.kind
