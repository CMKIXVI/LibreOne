from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass(frozen=True, slots=True)
class HealthStatus:
    service: str
    healthy: bool
    checked_at: datetime

def healthy(service: str) -> HealthStatus:
    return HealthStatus(service, True, datetime.now(timezone.utc))
