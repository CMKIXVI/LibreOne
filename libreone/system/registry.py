from typing import TypeVar

T = TypeVar("T")


class Registry:
    def __init__(self) -> None:
        self._items: dict[str, object] = {}

    @staticmethod
    def _validate_name(name: str) -> str:
        if not isinstance(name, str):
            raise TypeError("registry name must be a string")
        value = name.strip()
        if not value:
            raise ValueError("registry name cannot be empty")
        return value

    def register(self, name: str, value: T) -> None:
        key = self._validate_name(name)
        if key in self._items:
            raise ValueError(f"already registered: {key}")
        self._items[key] = value

    def get(self, name: str) -> T:
        return self._items[self._validate_name(name)]  # type: ignore[return-value]

    def __contains__(self, name: object) -> bool:
        if not isinstance(name, str):
            return False
        value = name.strip()
        return bool(value) and value in self._items
