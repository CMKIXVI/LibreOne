from libreone.system.permissions import Permission


def test_admin_is_distinct_permission():
    assert Permission.ADMIN != Permission.READ
