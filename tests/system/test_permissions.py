from libreone.system.permissions import Permission


def test_permissions_are_composable():
    permissions = Permission.READ | Permission.WRITE
    assert permissions & Permission.READ
    assert permissions & Permission.WRITE
    assert not permissions & Permission.EXECUTE
