from libreone.system.lifecycle import LifecycleState
from libreone.system.lifecycle_policy import can_transition


def test_lifecycle_policy_accepts_valid_edges():
    assert can_transition(LifecycleState.STOPPED, LifecycleState.STARTING)
    assert can_transition(LifecycleState.STARTING, LifecycleState.RUNNING)
    assert can_transition(LifecycleState.RUNNING, LifecycleState.STOPPING)
    assert can_transition(LifecycleState.STOPPING, LifecycleState.STOPPED)
    assert can_transition(LifecycleState.RUNNING, LifecycleState.FAILED)


def test_lifecycle_policy_rejects_invalid_edges():
    assert not can_transition(LifecycleState.STOPPED, LifecycleState.RUNNING)
    assert not can_transition(LifecycleState.FAILED, LifecycleState.RUNNING)
    assert not can_transition(LifecycleState.RUNNING, LifecycleState.STARTING)
