from libreone.system.version import BOOT_API_VERSION, RUNTIME_API_VERSION, SYSTEM_VERSION


def test_version_contract():
    assert SYSTEM_VERSION
    assert BOOT_API_VERSION.startswith("v")
    assert RUNTIME_API_VERSION.startswith("v")
