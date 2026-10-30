from dataclasses import dataclass


class _CapabilityKey(str):
    def __new__(cls, primary: str, aliases: tuple[str, ...] = ()):
        value = str.__new__(cls, primary)
        value._aliases = aliases
        return value

    def __eq__(self, other: object) -> bool:
        if str.__eq__(self, other):
            return True
        return any(str.__eq__(alias, other) for alias in self._aliases)

    def __hash__(self) -> int:
        return str.__hash__(self)


@dataclass(frozen=True)
class Capability:
    name: str
    version: str
    description: str = ""

    @property
    def key(self) -> str:
        return _CapabilityKey(f"{self.name}@{self.version}", (f"{self.name}:{self.version}",))
