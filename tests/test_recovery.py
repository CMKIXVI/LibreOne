from libreone.system.recovery import RecoveryManager
from libreone.system.state import SystemPhase, SystemState


def test_recovery_returns_failed_system_to_off():
    state = SystemState(SystemPhase.FAILED)
    RecoveryManager().recover(state)
    assert state.phase is SystemPhase.OFF
