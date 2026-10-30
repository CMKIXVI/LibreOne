"""Capability registration and lookup contract."""
from dataclasses import dataclass
from collections.abc import Callable

@dataclass(frozen=True, slots=True)
class Capability:
    name: str
    handler: Callable[..., object]

class CapabilityRegistry:
    def __init__(self) -> None:
        self._items: dict[str, Capability] = {}
    def register(self, name: str, handler: Callable[..., object]) -> None:
        if not name or name in self._items: raise ValueError("invalid or duplicate capability")
        self._items[name] = Capability(name, handler)
    def resolve(self, name: str) -> Capability:
        return self._items[name]
