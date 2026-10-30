from libreone.system.config import SystemConfig


def test_config_has_environment_defaults():
    config = SystemConfig()
    assert config.environment
    assert config.data_dir
