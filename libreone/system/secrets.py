import os


class SecretStore:
    def __init__(self, prefix: str = "LIBREONE_SECRET_") -> None:
        self.prefix = prefix

    def get(self, name: str) -> str | None:
        return os.getenv(f"{self.prefix}{name}")
