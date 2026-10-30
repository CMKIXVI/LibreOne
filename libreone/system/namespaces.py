from dataclasses import dataclass


@dataclass(frozen=True)
class Namespace:
    tenant: object
    name: str

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("namespace name cannot be empty")
        tenant_id = getattr(self.tenant, "id", self.tenant)
        if tenant_id is None:
            raise ValueError("namespace tenant cannot be empty")

    @property
    def key(self) -> str:
        tenant_id = getattr(self.tenant, "id", self.tenant)
        return f"{tenant_id}:{self.name}"
