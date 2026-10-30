import os
from dataclasses import dataclass
from os import PathLike


@dataclass(frozen=True)
class SystemConfig:
    environment: str = "production"
    data_dir: str | PathLike[str] = ".libreone"

    def __post_init__(self) -> None:
        if not isinstance(self.environment, str) or not self.environment.strip():
            raise ValueError("environment cannot be empty")
        if not isinstance(self.data_dir, (str, PathLike)) or not os.fspath(self.data_dir).strip():
            raise ValueError("data_dir cannot be empty")

    @classmethod
    def from_environment(cls) -> "SystemConfig":
        environment = os.getenv("LIBREONE_ENVIRONMENT")
        if environment is None:
            environment = os.getenv("LIBREONE_ENV", "production")
        return cls(
            environment=environment,
            data_dir=os.getenv("LIBREONE_DATA_DIR", ".libreone"),
        )
