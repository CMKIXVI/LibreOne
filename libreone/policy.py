from dataclasses import dataclass
from .errors import PolicyDenied

@dataclass(frozen=True, slots=True)
class Policy:
    max_risk: int = 50
    allowed_scopes: frozenset[str] = frozenset()

    def authorize(self, risk: int, scopes: frozenset[str]) -> None:
        if risk > self.max_risk:
            raise PolicyDenied("capability risk exceeds policy")
        if not scopes.issubset(self.allowed_scopes):
            raise PolicyDenied("capability scope is not authorized")
