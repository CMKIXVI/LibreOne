from .boot import BootMode


class BootPolicy:
    def __init__(self, *, allow_recovery: bool = True) -> None:
        self.allow_recovery = allow_recovery

    def authorize(self, mode: BootMode) -> bool:
        if mode is BootMode.RECOVERY and not self.allow_recovery:
            raise PermissionError("recovery boot is disabled")
        return True
