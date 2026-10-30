from libreone.system.errors import ResourceError, StateError, SystemError


def test_system_errors_share_base_type():
    assert issubclass(StateError, SystemError)
    assert issubclass(ResourceError, SystemError)
