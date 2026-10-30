import pytest

from libreone.system.lifecycle import Lifecycle, LifecycleState


def test_lifecycle_starts_and_stops_deterministically():
    lifecycle = Lifecycle()
    assert lifecycle.state is LifecycleState.STOPPED
    lifecycle.start()
    assert lifecycle.state is LifecycleState.RUNNING
    lifecycle.stop()
    assert lifecycle.state is LifecycleState.STOPPED


def test_lifecycle_rejects_double_start():
    lifecycle = Lifecycle()
    lifecycle.start()
    with pytest.raises(RuntimeError):
        lifecycle.start()


def test_lifecycle_stop_is_idempotent_when_stopped():
    Lifecycle().stop()


def test_lifecycle_rejects_stop_while_starting():
    lifecycle = Lifecycle()
    lifecycle.state = LifecycleState.STARTING
    with pytest.raises(RuntimeError):
        lifecycle.stop()


def test_lifecycle_failure_is_explicit():
    lifecycle = Lifecycle()
    lifecycle.start()
    lifecycle.fail()
    assert lifecycle.state is LifecycleState.FAILED
    with pytest.raises(RuntimeError):
        lifecycle.start()
