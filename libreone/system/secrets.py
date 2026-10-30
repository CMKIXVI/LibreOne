import os


class SecretStore:
    def __init__(self, prefix: str = "LIBREONE_SECRET_") -> None:
        self.prefix = prefix

    def get(self, name: str) -> str | None:
        if name.startswith(self.prefix):
            return os.getenv(name)
        return os.getenv(f"{self.prefix}{name}") or os.getenv(name)
