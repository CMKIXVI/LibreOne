from .boot import BootMode


class BootPolicy:
    def __init__(self, *, allow_recovery: bool = True) -> None:
        self.allow_recovery = allow_recovery

    def authorize(self, mode: BootMode) -> bool:
        return mode != BootMode.RECOVERY or self.allow_recovery
