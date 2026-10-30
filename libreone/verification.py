from dataclasses import dataclass
from typing import Any, Callable

@dataclass(frozen=True, slots=True)
class Verification:
    passed: bool
    reason: str

def verify(value: Any, predicate: Callable[[Any], bool], reason: str = "predicate failed") -> Verification:
    passed = bool(predicate(value))
    return Verification(passed, "ok" if passed else reason)
