from dataclasses import dataclass


@dataclass(frozen=True)
class SystemManifest:
    name: str = "LibreOne"
    api_version: str = "v1"

    def validate(self) -> None:
        if self.name != "LibreOne":
            raise ValueError("system name must be LibreOne")
