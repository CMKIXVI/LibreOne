from .state import SystemPhase, SystemState


class RecoveryManager:
    def __init__(self, state: SystemState | None = None) -> None:
        self.state = state

    def recover(self, state: SystemState | None = None) -> None:
        target = state or self.state
        if target is None:
            raise TypeError("recovery requires a system state")
        if target.phase != SystemPhase.FAILED:
            raise RuntimeError("recovery requires failed system state")
        target.transition(SystemPhase.OFF)
