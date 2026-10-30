import os
from libreone.system.secrets import SecretStore

def test_secret_store_reads_prefixed_environment_value(monkeypatch):
    monkeypatch.setenv("LIBREONE_SECRET_TEST", "value")
    assert SecretStore().get("TEST") == "value"
