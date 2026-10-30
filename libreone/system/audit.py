from dataclasses import dataclass, field
from datetime import datetime, timezone
from .ids import new_system_id


@dataclass(frozen=True)
class AuditRecord:
    action: str
    actor: str
    id: str = field(default_factory=lambda: str(new_system_id()))
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    metadata: dict[str, object] = field(default_factory=dict)
