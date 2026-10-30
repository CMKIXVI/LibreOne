import os

from libreone.system.secrets import SecretStore


def verify_secret_contract() -> bool:
    os.environ["LIBREONE_SECRET_TEST_SECRET"] = "ok"
    return SecretStore().get("TEST_SECRET") == "ok"
