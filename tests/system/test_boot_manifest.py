import pytest

from libreone.system.boot_manifest import BootManifest


def test_boot_manifest_accepts_valid_values():
    manifest = BootManifest("1", "x86_64", "libreone", "a" * 64)
    assert manifest.architecture == "x86_64"


def test_boot_manifest_rejects_missing_digest():
    with pytest.raises(ValueError):
        BootManifest("1", "x86_64", "libreone", "")
