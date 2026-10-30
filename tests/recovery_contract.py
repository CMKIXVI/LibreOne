from libreone.system.recovery import RecoveryManager
from libreone.system.state import SystemPhase, SystemState


def verify_recovery_contract() -> bool:
    state = SystemState(SystemPhase.FAILED)
    RecoveryManager(state).recover()
    return state.phase is SystemPhase.OFF
