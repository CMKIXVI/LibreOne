"""Core data contracts for LibreOne requests and results."""
from dataclasses import dataclass, field
from typing import Any
from .ids import new_id

@dataclass(frozen=True, slots=True)
class Request:
    action: str
    input: Any = None
    id: str = field(default_factory=lambda: str(new_id()))

@dataclass(frozen=True, slots=True)
class Result:
    request_id: str
    value: Any = None
    success: bool = True
