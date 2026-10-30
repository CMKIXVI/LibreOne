import pytest

from libreone.system.recovery import RecoveryManager
from libreone.system.state import SystemPhase, SystemState


def test_recovery_returns_failed_system_to_off():
    state = SystemState(SystemPhase.FAILED)
    RecoveryManager(state).recover()
    assert state.phase is SystemPhase.OFF


def test_recovery_requires_failed_state():
    state = SystemState()
    with pytest.raises(RuntimeError):
        RecoveryManager(state).recover()
