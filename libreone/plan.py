from dataclasses import dataclass
from uuid import UUID
from .ids import new_id

@dataclass(frozen=True, slots=True)
class PlanStep:
    capability: str
    id: UUID = new_id()

@dataclass(frozen=True, slots=True)
class Plan:
    steps: tuple[PlanStep, ...]
    id: UUID = new_id()
