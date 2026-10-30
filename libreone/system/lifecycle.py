from enum import Enum


class LifecycleState(str, Enum):
    STOPPED = "stopped"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
    FAILED = "failed"


from .lifecycle_policy import can_transition


class Lifecycle:
    def __init__(self) -> None:
        self.state = LifecycleState.STOPPED

    def _transition(self, target: LifecycleState) -> None:
        if not can_transition(self.state, target):
            raise RuntimeError(f"cannot transition from {self.state.value} to {target.value}")
        self.state = target

    def start(self) -> None:
        self._transition(LifecycleState.STARTING)
        self._transition(LifecycleState.RUNNING)

    def stop(self) -> None:
        if self.state is LifecycleState.STOPPED:
            return
        self._transition(LifecycleState.STOPPING)
        self._transition(LifecycleState.STOPPED)

    def fail(self) -> None:
        self._transition(LifecycleState.FAILED)
