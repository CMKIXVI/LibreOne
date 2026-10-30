"""Typed service registry with explicit replacement semantics."""
from typing import TypeVar
T = TypeVar("T")

class Registry:
    def __init__(self) -> None:
        self._services: dict[str, object] = {}
    def bind(self, name: str, service: object) -> None:
        if not name: raise ValueError("service name is required")
        if name in self._services: raise ValueError(f"service already bound: {name}")
        self._services[name] = service
    def get(self, name: str, expected: type[T] | None = None) -> T | object:
        value = self._services[name]
        if expected is not None and not isinstance(value, expected): raise TypeError(name)
        return value
