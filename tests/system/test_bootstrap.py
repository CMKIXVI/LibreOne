from libreone.system.bootstrap import Bootstrap
from libreone.system.state import SystemPhase, SystemState


def test_bootstrap_reaches_running():
    state = SystemState()
    Bootstrap(state).initialize()
    assert state.phase is SystemPhase.RUNNING
