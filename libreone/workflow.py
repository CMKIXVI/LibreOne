from dataclasses import dataclass
from enum import StrEnum

class WorkflowState(StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    WAITING = "waiting"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"

@dataclass(frozen=True, slots=True)
class Workflow:
    name: str
    state: WorkflowState = WorkflowState.PENDING
