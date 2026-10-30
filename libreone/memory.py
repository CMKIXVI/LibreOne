from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

@dataclass(frozen=True, slots=True)
class Memory:
    key: str
    value: Any
    scope: str
    created_at: datetime

class MemoryStore:
    def __init__(self) -> None:
        self._items: dict[tuple[str, str], Memory] = {}

    def put(self, key: str, value: Any, scope: str = "session") -> Memory:
        item = Memory(key, value, scope, datetime.now(timezone.utc))
        self._items[(scope, key)] = item
        return item

    def get(self, key: str, scope: str = "session") -> Memory | None:
        return self._items.get((scope, key))
