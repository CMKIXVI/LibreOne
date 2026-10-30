from dataclasses import dataclass
import re

_SECRET = re.compile(r"(?i)\b(api[_-]?key|secret|password|token)\s*[:=]\s*[^\s,;]+")

@dataclass(frozen=True, slots=True)
class WashingResult:
    text: str
    findings: tuple[str, ...]

def wash(text: str) -> WashingResult:
    findings = tuple(m.group(1).lower() for m in _SECRET.finditer(text))
    return WashingResult(_SECRET.sub(lambda m: f"{m.group(1)}=[REDACTED]", text), findings)
