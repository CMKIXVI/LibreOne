import os

from libreone.system.config import SystemConfig


def test_system_config_is_constructible(tmp_path):
    config = SystemConfig(environment="test", data_dir=tmp_path)
    assert config.environment == "test"
    assert config.data_dir == tmp_path


def test_system_config_reads_environment(monkeypatch, tmp_path):
    monkeypatch.setenv("LIBREONE_ENV", "ci")
    monkeypatch.setenv("LIBREONE_DATA_DIR", os.fspath(tmp_path))
    config = SystemConfig.from_environment()
    assert config.environment == "ci"
    assert config.data_dir == os.fspath(tmp_path)


def test_system_config_environment_defaults(monkeypatch):
    monkeypatch.delenv("LIBREONE_ENV", raising=False)
    monkeypatch.delenv("LIBREONE_DATA_DIR", raising=False)
    config = SystemConfig.from_environment()
    assert config.environment == "production"
    assert config.data_dir == ".libreone"
