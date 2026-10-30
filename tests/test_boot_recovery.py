import pytest

from libreone.system.boot import BootConfig, BootMode
from libreone.system.recovery import RecoveryManager
from libreone.system.state import SystemPhase, SystemState


def test_boot_config_defaults_are_deterministic():
    config = BootConfig()
    assert config.mode is BootMode.NORMAL
    assert config.image == "libreone"
    assert config.verify_image is True


def test_boot_config_is_immutable():
    config = BootConfig()
    with pytest.raises(Exception):
        config.mode = BootMode.SAFE


def test_recovery_returns_failed_system_to_off():
    state = SystemState()
    state.transition(SystemPhase.BOOTING)
    state.transition(SystemPhase.FAILED)
    RecoveryManager().recover(state)
    assert state.phase is SystemPhase.OFF


def test_recovery_rejects_non_failed_system():
    state = SystemState()
    with pytest.raises(RuntimeError):
        RecoveryManager().recover(state)
