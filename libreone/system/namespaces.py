from dataclasses import dataclass
from uuid import UUID


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
        if isinstance(tenant_id, UUID):
            return f"{tenant_id}:{self.name}"
        return f"{tenant_id}:{self.name}"
