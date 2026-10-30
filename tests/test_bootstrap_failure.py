from libreone.system.bootstrap import Bootstrap
from libreone.system.config import SystemConfig
from libreone.system.state import SystemPhase


def test_bootstrap_starts_from_off(tmp_path):
    state = Bootstrap().initialize(SystemConfig(environment="test", data_dir=tmp_path))
    assert state.phase is SystemPhase.RUNNING
