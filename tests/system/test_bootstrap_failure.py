import pytest

from libreone.system.bootstrap import Bootstrap
from libreone.system.state import SystemPhase, SystemState


def test_bootstrap_rejects_non_booting_state():
    state = SystemState(SystemPhase.RUNNING)
    with pytest.raises(Exception):
        Bootstrap(state).initialize()
