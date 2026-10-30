from libreone.system.permissions import Permission


def verify_permissions_contract() -> bool:
    return bool(Permission.READ | Permission.WRITE)
