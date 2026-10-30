from dataclasses import dataclass, field
from typing import Any
from uuid import UUID
from .ids import new_id

@dataclass(slots=True)
class Context:
    """Execution context kept separate from user intent."""
    session_id: UUID = field(default_factory=new_id)
    identity: UUID | None = None
    values: dict[str, Any] = field(default_factory=dict)

    def get(self, key: str, default: Any = None) -> Any:
        return self.values.get(key, default)
