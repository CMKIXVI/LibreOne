"""Execution context shared across LibreOne boundaries."""
from dataclasses import dataclass, field
from typing import Any

@dataclass(slots=True)
class Context:
    values: dict[str, Any] = field(default_factory=dict)
    trace_id: str | None = None

    def get(self, key: str, default: Any = None) -> Any:
        return self.values.get(key, default)
