from libreone.system.permissions import Permission


def verify_permission_model() -> bool:
    combined = Permission.READ | Permission.EXECUTE
    return bool(combined & Permission.READ) and bool(combined & Permission.EXECUTE)
