from libreone.system.config import SystemConfig


def test_system_config_is_constructible(tmp_path):
    config = SystemConfig(environment="test", data_dir=tmp_path)
    assert config.environment == "test"
    assert config.data_dir == tmp_path
