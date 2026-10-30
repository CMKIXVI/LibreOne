from libreone.system.bootstrap import Bootstrap
from libreone.system.state import SystemPhase

def test_bootstrap_is_deterministic_for_fresh_state():
    bootstrap = Bootstrap()
    bootstrap.initialize()
    assert bootstrap.state.phase is SystemPhase.RUNNING
