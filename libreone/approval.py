from dataclasses import dataclass
from uuid import UUID
from .ids import new_id

@dataclass(frozen=True, slots=True)
class ApprovalRequest:
    action: str
    requester: str
    id: UUID = new_id()

@dataclass(frozen=True, slots=True)
class Approval:
    request_id: UUID
    approver: str
    approved: bool
