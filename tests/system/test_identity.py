from libreone.system.identity import Identity


def test_identities_are_unique():
    first = Identity()
    second = Identity()
    assert first.id != second.id
