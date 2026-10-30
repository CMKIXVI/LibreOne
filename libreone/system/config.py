import os
from dataclasses import dataclass


@dataclass(frozen=True)
class SystemConfig:
    environment: str = "production"
    data_dir: str = ".libreone"

    @classmethod
    def from_environment(cls) -> "SystemConfig":
        environment = os.getenv("LIBREONE_ENVIRONMENT")
        if environment is None:
            environment = os.getenv("LIBREONE_ENV", "production")
        return cls(
            environment=environment,
            data_dir=os.getenv("LIBREONE_DATA_DIR", ".libreone"),
        )
