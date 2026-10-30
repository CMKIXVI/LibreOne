from libreone.system.boot import BootConfig, BootMode
from libreone.system.boot_policy import BootPolicy


def test_normal_boot_is_authorized():
    config = BootConfig(mode=BootMode.NORMAL)
    assert BootPolicy().authorize(config)
