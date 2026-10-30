from dataclasses import dataclass
import os

@dataclass(frozen=True, slots=True)
class Settings:
    environment: str = "production"
    log_level: str = "INFO"

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(os.getenv("LIBREONE_ENV", "production"), os.getenv("LIBREONE_LOG_LEVEL", "INFO"))
