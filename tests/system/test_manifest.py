from libreone.system.manifest import SystemManifest


def test_manifest_is_libreone():
    manifest = SystemManifest()
    assert manifest.name == "LibreOne"
    assert manifest.api_version == "v1"
