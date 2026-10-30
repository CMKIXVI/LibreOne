from dataclasses import dataclass


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
        return f"{tenant_id}:{self.name}"
