from libreone.system.manifest import SystemManifest


def test_manifest_api_version_is_stable():
    assert SystemManifest().api_version == "v1"
