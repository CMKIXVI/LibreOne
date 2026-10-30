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
