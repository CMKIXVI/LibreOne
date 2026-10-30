from dataclasses import dataclass
from enum import Enum


class Decision(str, Enum):
    ALLOW = "allow"
    DENY = "deny"


@dataclass(frozen=True)
class Policy:
    name: str
    decision: Decision

    def permits(self, resource: str | None = None) -> bool:
        if resource is not None and resource != self.name:
            return False
        return self.decision is Decision.ALLOW
