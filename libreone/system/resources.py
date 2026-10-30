from dataclasses import dataclass


@dataclass(frozen=True)
class ResourceLimits:
    cpu_seconds: float | None = None
    memory_bytes: int | None = None
    disk_bytes: int | None = None
    wall_seconds: float | None = None

    def validate(self) -> None:
        for name, value in self.__dict__.items():
            if value is not None and value < 0:
                raise ValueError(f"{name} must be non-negative")
