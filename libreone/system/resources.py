from dataclasses import dataclass


@dataclass(frozen=True)
class ResourceLimits:
    cpu_seconds: float | None = None
    memory_bytes: int | None = None
    disk_bytes: int | None = None
    wall_seconds: float | None = None

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        numeric = (self.cpu_seconds, self.memory_bytes, self.disk_bytes, self.wall_seconds)
        for name, value in zip(("cpu_seconds", "memory_bytes", "disk_bytes", "wall_seconds"), numeric):
            if value is None:
                continue
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise TypeError(f"{name} must be numeric")
            if value < 0:
                raise ValueError(f"{name} must be non-negative")
        for name, value in (("memory_bytes", self.memory_bytes), ("disk_bytes", self.disk_bytes)):
            if value is not None and not isinstance(value, int):
                raise TypeError(f"{name} must be an integer")
