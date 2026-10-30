import pytest

from libreone.system.bootstrap import Bootstrap
from libreone.system.state import SystemPhase, SystemState


def test_bootstrap_cannot_initialize_twice():
    state = SystemState()
    bootstrap = Bootstrap(state)
    bootstrap.initialize()
    assert state.phase is SystemPhase.RUNNING
    with pytest.raises(Exception):
        bootstrap.initialize()
