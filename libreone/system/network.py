from dataclasses import dataclass


@dataclass(frozen=True)
class Endpoint:
    host: str
    port: int

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        if not isinstance(self.host, str) or not self.host.strip():
            raise ValueError("endpoint host cannot be empty")
        if not isinstance(self.port, int) or isinstance(self.port, bool) or not 1 <= self.port <= 65535:
            raise ValueError("endpoint port must be between 1 and 65535")
