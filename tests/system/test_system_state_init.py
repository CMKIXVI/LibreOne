from libreone.system.state import SystemPhase, SystemState


def test_system_state_starts_off():
    assert SystemState().phase is SystemPhase.OFF
