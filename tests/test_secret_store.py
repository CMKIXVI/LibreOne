import pytest
from libreone.system.secrets import SecretStore


def test_secret_store_reads_environment(monkeypatch):
    monkeypatch.setenv("LIBREONE_TEST_SECRET", "value")
    assert SecretStore().get("LIBREONE_TEST_SECRET") == "value"
