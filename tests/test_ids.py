from libreone.system.ids import new_system_id


def test_system_ids_are_unique():
    assert new_system_id() != new_system_id()
