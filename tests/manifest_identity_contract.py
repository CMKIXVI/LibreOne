from libreone.system.manifest import SystemManifest
from libreone.system.identity import Identity


def verify_identity_manifest_contract() -> bool:
    return SystemManifest().name == "LibreOne" and Identity().id is not None
