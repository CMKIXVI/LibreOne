from .lifecycle import Lifecycle, LifecycleState


def lifecycle_contract() -> tuple[LifecycleState, LifecycleState]:
    lifecycle = Lifecycle()
    lifecycle.start()
    running = lifecycle.state
    lifecycle.stop()
    return running, lifecycle.state
