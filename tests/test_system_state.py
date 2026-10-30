from libreone.system.state import SystemPhase, SystemState


def test_system_state_starts_off():
    assert SystemState().phase is SystemPhase.OFF


def test_system_state_boot_sequence():
    state = SystemState()
    state.transition(SystemPhase.BOOTING)
    state.transition(SystemPhase.INITIALIZING)
    state.transition(SystemPhase.RUNNING)
    assert state.phase is SystemPhase.RUNNING


def test_system_state_rejects_invalid_transition():
    state = SystemState()
    try:
        state.transition(SystemPhase.RUNNING)
    except Exception:
        pass
    else:
        raise AssertionError("invalid transition was accepted")
