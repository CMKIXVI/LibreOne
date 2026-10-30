from libreone.system.boot import BootConfig, BootMode


def verify_boot_contract() -> bool:
    config = BootConfig()
    return config.mode is BootMode.NORMAL
