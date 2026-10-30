from libreone.system.errors import ResourceError, StateError, SystemError


def test_error_hierarchy():
    assert issubclass(StateError, SystemError)
    assert issubclass(ResourceError, SystemError)
