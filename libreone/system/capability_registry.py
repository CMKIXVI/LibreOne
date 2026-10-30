from .capabilities import Capability


class CapabilityRegistry:
    def __init__(self) -> None:
        self._items: dict[str, Capability] = {}

    def register(self, capability: Capability) -> None:
        key = capability.key
        if key in self._items:
            raise ValueError(f"capability already registered: {key}")
        self._items[key] = capability

    def get(self, key: str) -> Capability:
        return self._items[key]

    def resolve(self, key: str) -> Capability:
        return self.get(key)

    def all(self) -> tuple[Capability, ...]:
        return tuple(self._items.values())
