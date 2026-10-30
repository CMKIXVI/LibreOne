from enum import Enum


class LifecycleState(str, Enum):
    STOPPED = "stopped"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
    FAILED = "failed"


class Lifecycle:
    def __init__(self) -> None:
        self.state = LifecycleState.STOPPED

    def start(self) -> None:
        if self.state is not LifecycleState.STOPPED:
            raise RuntimeError(f"cannot start from {self.state.value}")
        self.state = LifecycleState.STARTING
        self.state = LifecycleState.RUNNING

    def stop(self) -> None:
        if self.state is LifecycleState.STOPPED:
            return
        if self.state is not LifecycleState.RUNNING:
            raise RuntimeError(f"cannot stop from {self.state.value}")
        self.state = LifecycleState.STOPPING
        self.state = LifecycleState.STOPPED

    def fail(self) -> None:
        if self.state is LifecycleState.STOPPED:
            raise RuntimeError("cannot fail a stopped lifecycle")
        self.state = LifecycleState.FAILED
