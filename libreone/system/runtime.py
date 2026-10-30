from dataclasses import dataclass
from .resources import ResourceLimits


@dataclass(frozen=True)
class RuntimeTask:
    name: str
    limits: ResourceLimits = ResourceLimits()

    def validate(self) -> None:
        if not self.name.strip():
            raise ValueError("task name cannot be empty")
        self.limits.validate()
