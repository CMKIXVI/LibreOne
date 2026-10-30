from dataclasses import dataclass


@dataclass(frozen=True)
class SystemManifest:
    name: str = "LibreOne"
    api_version: str = "v1"

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        if not self.name or self.name != "LibreOne":
            raise ValueError("system name must be LibreOne")
        if not self.api_version:
            raise ValueError("api_version is required")
