import pytest

from libreone.system.errors import StateError
from libreone.system.state import SystemPhase, SystemState


def test_state_transitions_to_running():
    state = SystemState()
    state.transition(SystemPhase.BOOTING)
    state.transition(SystemPhase.INITIALIZING)
    state.transition(SystemPhase.RUNNING)
    assert state.phase is SystemPhase.RUNNING


def test_state_rejects_invalid_transition():
    state = SystemState()
    with pytest.raises(StateError):
        state.transition(SystemPhase.RUNNING)
