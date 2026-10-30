from .capabilities import Capability


class CapabilityRegistry:
    def __init__(self) -> None:
        self._items: dict[str, Capability] = {}

    @staticmethod
    def _canonical_key(key: str) -> str:
        if not isinstance(key, str):
            raise TypeError("capability key must be a string")
        value = key.strip()
        if not value:
            raise ValueError("capability key cannot be empty")
        if "@" in value:
            if ":" in value:
                raise ValueError("capability key cannot mix @ and : separators")
            name, version = value.split("@", 1)
            name = name.strip()
            version = version.strip()
            if not name or not version:
                raise ValueError("capability key must contain name and version")
            return f"{name}:{version}"
        if ":" in value:
            name, version = value.split(":", 1)
            name = name.strip()
            version = version.strip()
            if not name or not version:
                raise ValueError("capability key must contain name and version")
            return f"{name}:{version}"
        raise ValueError("capability key must contain name and version")

    def register(self, capability: Capability) -> None:
        if not isinstance(capability, Capability):
            raise TypeError("capability must be a Capability")
        key = self._canonical_key(capability.key)
        if key in self._items:
            raise ValueError(f"capability already registered: {key}")
        self._items[key] = capability

    def get(self, key: str) -> Capability:
        return self._items[key]

    def resolve(self, key: str) -> Capability:
        return self._items[self._canonical_key(key)]

    def all(self) -> tuple[Capability, ...]:
        return tuple(self._items.values())
