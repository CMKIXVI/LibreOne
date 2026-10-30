from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(frozen=True)
class Tenant:
    name: str
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("tenant name cannot be empty")
