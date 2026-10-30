from libreone.system.boot import BootConfig, BootMode


def test_safe_mode_configuration():
    config = BootConfig(mode=BootMode.SAFE)
    assert config.mode is BootMode.SAFE
