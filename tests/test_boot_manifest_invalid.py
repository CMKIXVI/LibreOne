import pytest
from libreone.system.boot_manifest import BootManifest


def test_boot_manifest_rejects_invalid_digest():
    with pytest.raises(ValueError):
        BootManifest("1", "x86_64", "libreone", "bad")
