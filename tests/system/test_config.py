from libreone.system.config import SystemConfig


def test_config_from_environment(monkeypatch):
    monkeypatch.setenv("LIBREONE_ENVIRONMENT", "test")
    monkeypatch.setenv("LIBREONE_DATA_DIR", "/tmp/libreone")
    config = SystemConfig.from_environment()
    assert config.environment == "test"
    assert config.data_dir == "/tmp/libreone"
