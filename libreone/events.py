from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any
from uuid import UUID
from .ids import new_id

@dataclass(frozen=True, slots=True)
class Event:
    type: str
    payload: dict[str, Any]
    id: UUID = new_id()
    occurred_at: datetime = datetime.now(timezone.utc)
