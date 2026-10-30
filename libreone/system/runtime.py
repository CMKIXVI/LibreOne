from dataclasses import dataclass
from .resources import ResourceLimits


@dataclass(frozen=True)
class RuntimeTask:
    name: str
    limits: ResourceLimits = ResourceLimits()

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("task name cannot be empty")
        self.limits.validate()
