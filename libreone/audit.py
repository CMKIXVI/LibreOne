"""Structured audit record contract."""
from dataclasses import dataclass, field
from datetime import datetime, timezone
from .ids import new_id

@dataclass(frozen=True, slots=True)
class AuditRecord:
    action: str
    subject: str
    outcome: str
    id: str = field(default_factory=lambda: str(new_id()))
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
