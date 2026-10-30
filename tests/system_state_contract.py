from libreone.system.state import SystemPhase, SystemState


def verify_state_contract() -> bool:
    state = SystemState()
    state.transition(SystemPhase.BOOTING)
    state.transition(SystemPhase.INITIALIZING)
    state.transition(SystemPhase.RUNNING)
    return state.phase is SystemPhase.RUNNING
