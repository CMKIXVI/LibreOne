from libreone.system.permissions import Permission


def test_permission_values_are_unique():
    values = [item.value for item in Permission]
    assert len(values) == len(set(values))
