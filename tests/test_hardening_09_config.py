from libreone.system.config import SystemConfig

def test_system_config_defaults_to_production():
    config = SystemConfig()
    assert config.environment == "production"
    assert config.data_dir == ".libreone"
