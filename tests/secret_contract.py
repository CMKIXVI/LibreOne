from libreone.system.secrets import SecretStore


def verify_secret_contract() -> bool:
    store = SecretStore({"LIBREONE_TEST_SECRET": "ok"})
    return store.get("LIBREONE_TEST_SECRET") == "ok"
