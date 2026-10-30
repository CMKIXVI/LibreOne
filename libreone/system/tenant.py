from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(frozen=True)
class Tenant:
    name: str
    id: UUID = field(default_factory=uuid4)

    def validate(self) -> None:
        if not self.name.strip():
            raise ValueError("tenant name cannot be empty")
