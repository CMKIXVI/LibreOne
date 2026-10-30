from libreone.system.config import SystemConfig


def test_config_can_load_environment(monkeypatch):
    monkeypatch.setenv("LIBREONE_ENVIRONMENT", "ci")
    config = SystemConfig.from_environment()
    assert config.environment == "ci"
