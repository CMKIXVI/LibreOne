from libreone.system.version import BOOT_API_VERSION, RUNTIME_API_VERSION


def verify_version_contract() -> bool:
    return bool(BOOT_API_VERSION) and bool(RUNTIME_API_VERSION)
