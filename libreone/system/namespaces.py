from dataclasses import dataclass
from uuid import UUID


class _NamespaceKey(str):
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
class Namespace:
    tenant: object
    name: str

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("namespace name cannot be empty")

    @property
    def key(self) -> str:
        tenant_id = getattr(self.tenant, "id", self.tenant)
        tenant_name = getattr(self.tenant, "name", str(tenant_id))
        primary = f"{tenant_name}/{self.name}"
        scoped = f"{tenant_id}:{self.name}"
        return _NamespaceKey(primary, (scoped,))
