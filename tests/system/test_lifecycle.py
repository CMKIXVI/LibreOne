from libreone.system.lifecycle import LifecycleState


def test_lifecycle_states_are_stable():
    assert [state.value for state in LifecycleState] == [
        "stopped",
        "starting",
        "running",
        "stopping",
        "failed",
    ]
