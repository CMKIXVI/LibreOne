from .capabilities import Capability


class CapabilityRegistry:
    def __init__(self) -> None:
        self._items: dict[str, Capability] = {}

    @staticmethod
    def _canonical_key(key: str) -> str:
        if not isinstance(key, str) or not key.strip():
            raise ValueError("capability key cannot be empty")
        value = key.strip()
        if "@" in value and ":" not in value:
            name, version = value.split("@", 1)
            return f"{name}:{version}"
        return value

    def register(self, capability: Capability) -> None:
        key = capability.key
        if key in self._items:
            raise ValueError(f"capability already registered: {key}")
        self._items[key] = capability

    def get(self, key: str) -> Capability:
        return self._items[key]

    def resolve(self, key: str) -> Capability:
        return self._items[self._canonical_key(key)]

    def all(self) -> tuple[Capability, ...]:
        return tuple(self._items.values())
