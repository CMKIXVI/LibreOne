from dataclasses import dataclass, field
from enum import Enum
from uuid import UUID, uuid4


class ProcessState(str, Enum):
    CREATED = "created"
    READY = "ready"
    RUNNING = "running"
    STOPPED = "stopped"
    FAILED = "failed"


@dataclass
class Process:
    name: str
    id: UUID = field(default_factory=uuid4)
    state: ProcessState = ProcessState.CREATED

    def start(self) -> None:
        if self.state not in {ProcessState.CREATED, ProcessState.STOPPED}:
            raise RuntimeError(f"cannot start process in {self.state.value}")
        self.state = ProcessState.RUNNING

    def stop(self) -> None:
        if self.state != ProcessState.RUNNING:
            raise RuntimeError(f"cannot stop process in {self.state.value}")
        self.state = ProcessState.STOPPED
