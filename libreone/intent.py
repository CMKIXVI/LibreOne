from dataclasses import dataclass, field
from typing import Mapping
from uuid import UUID
from .ids import new_id

@dataclass(frozen=True, slots=True)
class Intent:
    """Normalized user goal carried through execution."""
    goal: str
    id: UUID = field(default_factory=new_id)
    constraints: Mapping[str, str] = field(default_factory=dict)
    priority: int = 0
    authorization: str | None = None

    def __post_init__(self) -> None:
        if not self.goal.strip():
            raise ValueError("goal must not be empty")
        if not 0 <= self.priority <= 100:
            raise ValueError("priority must be between 0 and 100")
