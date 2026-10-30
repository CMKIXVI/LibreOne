from dataclasses import dataclass


@dataclass(frozen=True)
class BootManifest:
    version: str
    architecture: str
    entrypoint: int
    image_digest: str

    def validate(self) -> None:
        if not self.version or not self.architecture or not self.image_digest:
            raise ValueError("boot manifest contains empty required fields")
        if self.entrypoint < 0:
            raise ValueError("entrypoint must be non-negative")
