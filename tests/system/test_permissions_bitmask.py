from libreone.system.permissions import Permission


def test_permission_bitmask_is_nonzero():
    combined = Permission.READ | Permission.WRITE | Permission.EXECUTE | Permission.ADMIN
    assert combined.value != 0
