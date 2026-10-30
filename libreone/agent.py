from dataclasses import dataclass, field
from uuid import UUID
from .ids import new_id

@dataclass(frozen=True, slots=True)
class Agent:
    name: str
    id: UUID = field(default_factory=new_id)
    capabilities: frozenset[str] = frozenset()

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("agent name must not be empty")
