import pytest
from libreone.system.recovery import RecoveryManager
from libreone.system.state import SystemPhase, SystemState

def test_recovery_requires_failed_state():
    with pytest.raises(RuntimeError):
        RecoveryManager().recover(SystemState())

def test_recovery_returns_failed_system_to_off():
    state = SystemState()
    state.transition(SystemPhase.BOOTING)
    state.transition(SystemPhase.FAILED)
    RecoveryManager().recover(state)
    assert state.phase is SystemPhase.OFF
