from libreone.system.bootstrap import Bootstrap
from libreone.system.config import SystemConfig
from libreone.system.state import SystemPhase, SystemState


def verify_bootstrap_contract() -> bool:
    state = SystemState()
    Bootstrap(state, SystemConfig()).initialize()
    return state.phase is SystemPhase.RUNNING
