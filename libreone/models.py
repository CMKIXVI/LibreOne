from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID
from .ids import new_id

@dataclass(frozen=True, slots=True)
class Entity:
    id: UUID = field(default_factory=new_id)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __post_init__(self) -> None:
        if self.created_at.tzinfo is None:
            raise ValueError("created_at must be timezone-aware")
