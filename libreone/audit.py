from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

@dataclass(frozen=True, slots=True)
class AuditRecord:
    action: str
    actor: str
    outcome: str
    metadata: dict[str, Any]
    timestamp: datetime

class AuditLog:
    def __init__(self) -> None:
        self._records: list[AuditRecord] = []

    def append(self, action: str, actor: str, outcome: str, metadata: dict[str, Any] | None = None) -> AuditRecord:
        record = AuditRecord(action, actor, outcome, metadata or {}, datetime.now(timezone.utc))
        self._records.append(record)
        return record

    def records(self) -> tuple[AuditRecord, ...]:
        return tuple(self._records)
