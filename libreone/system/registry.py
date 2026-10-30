from typing import TypeVar

T = TypeVar("T")


class Registry:
    def __init__(self) -> None:
        self._items: dict[str, object] = {}

    def register(self, name: str, value: T) -> None:
        if name in self._items:
            raise ValueError(f"already registered: {name}")
        self._items[name] = value

    def get(self, name: str) -> T:
        return self._items[name]  # type: ignore[return-value]

    def __contains__(self, name: object) -> bool:
        return name in self._items
