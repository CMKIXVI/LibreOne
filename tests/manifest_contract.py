from libreone.system.manifest import SystemManifest


def verify_manifest_contract() -> bool:
    return SystemManifest().name == "LibreOne"
