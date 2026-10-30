from libreone.system.boot import BootConfig, BootMode

def test_boot_config_defaults_to_verified_normal_boot():
    config = BootConfig()
    assert config.mode is BootMode.NORMAL
    assert config.verify_image is True
