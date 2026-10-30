from dataclasses import FrozenInstanceError

import pytest

from libreone.system.boot_manifest import BootManifest


def test_boot_manifest_is_immutable():
    manifest = BootManifest("1", "x86_64", "entry", "digest")
    with pytest.raises(FrozenInstanceError):
        manifest.version = "2"
