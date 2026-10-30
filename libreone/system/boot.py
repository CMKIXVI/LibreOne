from dataclasses import dataclass
from enum import Enum


class BootMode(str, Enum):
    NORMAL = "normal"
    RECOVERY = "recovery"
    SAFE = "safe"


@dataclass(frozen=True)
class BootConfig:
    mode: BootMode = BootMode.NORMAL
    image: str = "libreone"
    verify_image: bool = True
