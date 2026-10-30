from .lifecycle import LifecycleState


_ALLOWED = {
    LifecycleState.STOPPED: frozenset({LifecycleState.STARTING}),
    LifecycleState.STARTING: frozenset({LifecycleState.RUNNING, LifecycleState.FAILED}),
    LifecycleState.RUNNING: frozenset({LifecycleState.STOPPING, LifecycleState.FAILED}),
    LifecycleState.STOPPING: frozenset({LifecycleState.STOPPED, LifecycleState.FAILED}),
    LifecycleState.FAILED: frozenset({LifecycleState.STOPPED}),
}


def can_transition(source: LifecycleState, target: LifecycleState) -> bool:
    return target in _ALLOWED[source]
