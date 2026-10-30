from .state import SystemPhase, SystemState


class RecoveryManager:
    def recover(self, state: SystemState) -> None:
        if state.phase != SystemPhase.FAILED:
            raise RuntimeError("recovery requires failed system state")
        state.transition(SystemPhase.OFF)
