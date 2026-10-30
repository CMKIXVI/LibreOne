from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID
from .ids import new_system_id


@dataclass(frozen=True)
class SystemEvent:
    name: str
    payload: dict[str, object] = field(default_factory=dict)
    id: UUID = field(default_factory=new_system_id)
    occurred_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
