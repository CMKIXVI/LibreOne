from dataclasses import dataclass


@dataclass(frozen=True)
class Capability:
    name: str
    version: str
    description: str = ""

    def key(self) -> str:
        return f"{self.name}@{self.version}"
