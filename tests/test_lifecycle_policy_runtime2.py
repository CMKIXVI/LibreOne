from libreone.system.lifecycle import Lifecycle


def test_runtime_invalid_start_is_rejected():
    lifecycle = Lifecycle()
    lifecycle.start()
    try:
        lifecycle.start()
    except RuntimeError:
        return
    raise AssertionError("double start was accepted")
