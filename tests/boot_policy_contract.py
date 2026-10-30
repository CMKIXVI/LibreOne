from libreone.system.boot_policy import BootPolicy
from libreone.system.boot import BootMode


def verify_boot_policy_contract() -> bool:
    return BootPolicy().authorize(BootMode.NORMAL)
