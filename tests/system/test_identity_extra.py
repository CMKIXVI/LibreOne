from libreone.system.identity import Identity


def test_identity_is_uuid_backed():
    identity = Identity()
    assert identity.id.version == 4
