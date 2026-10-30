import pytest

from libreone.system.lifecycle import Lifecycle, LifecycleState


def test_runtime_enforces_lifecycle_policy():
    lifecycle = Lifecycle()
    lifecycle.state = LifecycleState.RUNNING
    with pytest.raises(RuntimeError, match="cannot transition from running to starting"):
        lifecycle.start()
