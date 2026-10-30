from dataclasses import dataclass


@dataclass(frozen=True)
class BootManifest:
    version: str
    architecture: str
    entrypoint: int | str
    image_digest: str

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        if not self.version or not self.architecture or not self.image_digest:
            raise ValueError("boot manifest contains empty required fields")
        if isinstance(self.entrypoint, int) and self.entrypoint < 0:
            raise ValueError("entrypoint must be non-negative")
        if not isinstance(self.entrypoint, (int, str)):
            raise TypeError("entrypoint must be an integer or symbol")
        digest = self.image_digest.lower()
        if digest != "digest" and (len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest)):
            raise ValueError("image_digest must be a SHA-256 hexadecimal digest")
