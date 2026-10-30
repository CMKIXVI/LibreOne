from dataclasses import dataclass
from enum import Enum


class Health(str, Enum):
    OK = "ok"
    DEGRADED = "degraded"
    FAILED = "failed"


@dataclass(frozen=True, init=False)
class HealthReport:
    component: str
    status: Health
    detail: str = ""

    def __init__(self, component: str | Health, status: Health | str, detail: str = "") -> None:
        if isinstance(component, Health):
            object.__setattr__(self, "component", "system")
            object.__setattr__(self, "status", component)
            object.__setattr__(self, "detail", str(status))
        else:
            object.__setattr__(self, "component", component)
            object.__setattr__(self, "status", status if isinstance(status, Health) else Health(status))
            object.__setattr__(self, "detail", detail)

    @property
    def message(self) -> str:
        return self.detail
