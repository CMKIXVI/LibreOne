from dataclasses import dataclass


@dataclass(frozen=True)
class Namespace:
    tenant: str
    name: str

    def key(self) -> str:
        return f"{self.tenant}:{self.name}"
