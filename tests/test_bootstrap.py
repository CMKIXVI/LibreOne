from libreone.system.bootstrap import Bootstrap
from libreone.system.state import SystemPhase


def test_bootstrap_reaches_running_state():
    bootstrap = Bootstrap()
    bootstrap.initialize()
    assert bootstrap.state.phase is SystemPhase.RUNNING


def test_bootstrap_accepts_explicit_config():
    from libreone.system.config import SystemConfig

    bootstrap = Bootstrap()
    bootstrap.initialize(SystemConfig(environment="test"))
    assert bootstrap.state.phase is SystemPhase.RUNNING
