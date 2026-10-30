from libreone.system.permissions import Permission


def test_permission_flags_are_composable():
    permissions = Permission.READ | Permission.WRITE
    assert Permission.READ in permissions
    assert Permission.EXECUTE not in permissions
