from libreone.system.boot import BootMode
from libreone.system.boot_policy import BootPolicy


def test_normal_boot_is_authorized():
    assert BootPolicy().authorize(BootMode.NORMAL)
