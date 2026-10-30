from libreone.system.identity import Identity

def test_identity_values_are_unique():
    first = Identity()
    second = Identity()
    assert first.id != second.id
