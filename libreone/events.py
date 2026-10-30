"""Event contract with per-instance identifiers and timestamps."""
from dataclasses import dataclass, field
from datetime import datetime, timezone
from .ids import new_id

@dataclass(frozen=True, slots=True)
class Event:
    kind: str
    payload: dict[str, object] = field(default_factory=dict)
    id: str = field(default_factory=lambda: str(new_id()))
    occurred_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
