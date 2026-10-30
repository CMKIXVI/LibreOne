from libreone.system.recovery import RecoveryManager
from libreone.system.state import SystemPhase, SystemState


def test_recovery_is_terminal_to_off():
    state = SystemState(SystemPhase.FAILED)
    RecoveryManager(state).recover()
    assert state.phase is SystemPhase.OFF
