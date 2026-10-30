from libreone.system.identity import Identity


def test_identity_ids_are_unique():
    assert Identity().id != Identity().id
