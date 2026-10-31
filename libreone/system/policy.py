from dataclasses import dataclass
from enum import Enum


class Decision(str, Enum):
    ALLOW = "allow"
    DENY = "deny"


@dataclass(frozen=True)
class Policy:
    name: str
    decision: Decision

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("policy name cannot be empty")
        if not isinstance(self.decision, Decision):
            raise TypeError("policy decision must be a Decision")
        object.__setattr__(self, "name", self.name.strip())

    def permits(self, resource: str | None = None) -> bool:
        if resource is not None:
            if not isinstance(resource, str) or not resource.strip():
                return False
            if resource.strip() != self.name:
                return False
        return self.decision is Decision.ALLOW
