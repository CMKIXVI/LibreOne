from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID
from .ids import new_id

@dataclass(frozen=True, slots=True)
class Artifact:
    name: str
    media_type: str
    uri: str
    id: UUID = field(default_factory=new_id)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
