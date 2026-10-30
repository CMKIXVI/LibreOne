from dataclasses import dataclass
from enum import Enum


class Decision(str, Enum):
    ALLOW = "allow"
    DENY = "deny"


@dataclass(frozen=True)
class Policy:
    name: str
    decision: Decision

    def permits(self) -> bool:
        return self.decision is Decision.ALLOW
