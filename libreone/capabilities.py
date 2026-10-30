from dataclasses import dataclass, field
from typing import Callable, Any
from uuid import UUID
from .ids import new_id

@dataclass(frozen=True, slots=True)
class Capability:
    name: str
    handler: Callable[..., Any]
    id: UUID = field(default_factory=new_id)
    risk: int = 0
    scopes: frozenset[str] = frozenset()

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("capability name must not be empty")
        if not 0 <= self.risk <= 100:
            raise ValueError("risk must be between 0 and 100")
