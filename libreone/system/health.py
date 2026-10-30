from dataclasses import dataclass
from enum import Enum


class Health(str, Enum):
    OK = "ok"
    DEGRADED = "degraded"
    FAILED = "failed"


@dataclass(frozen=True)
class HealthReport:
    component: str
    status: Health
    detail: str = ""
