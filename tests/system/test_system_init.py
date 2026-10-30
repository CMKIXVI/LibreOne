from libreone.system import SystemError, StateError, ResourceError, SystemPhase


def test_system_public_exports():
    assert issubclass(StateError, SystemError)
    assert issubclass(ResourceError, SystemError)
    assert SystemPhase.RUNNING.value == "running"
