from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID
from .ids import new_id

@dataclass(frozen=True, slots=True)
class Event:
    type: str
    payload: dict[str, Any]
    id: UUID = field(default_factory=new_id)
    occurred_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
