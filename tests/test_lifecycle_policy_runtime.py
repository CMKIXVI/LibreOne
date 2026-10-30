import pytest

from libreone.system.lifecycle import Lifecycle, LifecycleState


def test_runtime_rejects_invalid_start_transition():
    lifecycle = Lifecycle()
    lifecycle.state = LifecycleState.RUNNING
    with pytest.raises(RuntimeError, match="cannot start from running"):
        lifecycle.start()
