from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import UUID
from .ids import new_id

@dataclass(frozen=True, slots=True)
class Provenance:
    source: str
    operation: str
    id: UUID = new_id()
    recorded_at: datetime = datetime.now(timezone.utc)
