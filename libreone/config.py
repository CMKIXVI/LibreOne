"""Immutable runtime configuration primitives."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class RuntimeConfig:
    environment: str = "production"
    log_level: str = "INFO"
    max_workers: int = 8

    def __post_init__(self) -> None:
        if self.max_workers < 1:
            raise ValueError("max_workers must be positive")
