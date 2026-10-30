from libreone.system.boot import BootConfig, BootMode


def test_boot_config_supports_recovery():
    assert BootConfig(mode=BootMode.RECOVERY).mode is BootMode.RECOVERY
