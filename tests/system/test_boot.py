import pytest

from libreone.system.boot import BootConfig, BootMode
from libreone.system.boot_manifest import BootManifest
from libreone.system.boot_policy import BootPolicy


def test_boot_modes_are_stable():
    assert BootConfig().mode is BootMode.NORMAL
    assert BootConfig(BootMode.RECOVERY).mode is BootMode.RECOVERY


def test_manifest_rejects_empty_fields():
    with pytest.raises(ValueError):
        BootManifest("", "x86_64", "entry", "digest")


def test_recovery_policy():
    policy = BootPolicy(allow_recovery=False)
    with pytest.raises(PermissionError):
        policy.authorize(BootMode.RECOVERY)
