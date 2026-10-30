from dataclasses import dataclass
from .errors import PolicyDenied

@dataclass(frozen=True, slots=True)
class SecurityDecision:
    allowed: bool
    reason: str

def require_authenticated(identity: str | None) -> SecurityDecision:
    if not identity:
        raise PolicyDenied("authenticated identity required")
    return SecurityDecision(True, "authenticated")
