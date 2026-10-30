from libreone.system.lifecycle import Lifecycle, LifecycleState


def test_runtime_uses_policy_for_invalid_transition():
    lifecycle = Lifecycle()
    lifecycle.state = LifecycleState.RUNNING
    try:
        lifecycle.start()
    except RuntimeError as exc:
        assert "invalid lifecycle transition" in str(exc)
    else:
        raise AssertionError("invalid transition was accepted")
