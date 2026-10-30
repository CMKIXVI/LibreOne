from libreone.system.boot import BootMode
from libreone.system.boot_policy import BootPolicy


def test_safe_boot_is_authorized_by_default():
    assert BootPolicy().authorize(BootMode.SAFE)
