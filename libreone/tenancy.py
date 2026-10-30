from dataclasses import dataclass
from uuid import UUID
from .ids import new_id

@dataclass(frozen=True, slots=True)
class Tenant:
    name: str
    id: UUID = new_id()

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("tenant name must not be empty")
