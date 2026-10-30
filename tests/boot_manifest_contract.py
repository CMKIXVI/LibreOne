from libreone.system.boot_manifest import BootManifest


def verify_boot_manifest_contract() -> bool:
    manifest = BootManifest("1", "x86_64", "libreone", "a" * 64)
    manifest.validate()
    return manifest.entrypoint == "libreone"
