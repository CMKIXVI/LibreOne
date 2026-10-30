from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class SandboxPolicy:
    network: bool = False
    filesystem: str = "workspace"
    timeout_seconds: int = 300

    def __post_init__(self) -> None:
        if self.timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be positive")
