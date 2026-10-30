from dataclasses import FrozenInstanceError

import pytest

from libreone.system.manifest import SystemManifest


def test_manifest_is_immutable():
    manifest = SystemManifest()
    with pytest.raises(FrozenInstanceError):
        manifest.name = "Other"
