import pytest

from libreone.system.manifest import SystemManifest


def test_manifest_rejects_non_libreone_name():
    with pytest.raises(ValueError):
        SystemManifest(name="OtherOS")
