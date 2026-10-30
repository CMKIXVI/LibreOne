from dataclasses import dataclass


@dataclass(frozen=True)
class Capability:
    name: str
    version: str
    description: str = ""

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("capability name cannot be empty")
        if not isinstance(self.version, str) or not self.version.strip():
            raise ValueError("capability version cannot be empty")
        if not isinstance(self.description, str):
            raise TypeError("capability description must be a string")

    @property
    def key(self) -> str:
        return f"{self.name}:{self.version}"
