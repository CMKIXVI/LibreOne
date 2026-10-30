from dataclasses import dataclass


@dataclass(frozen=True)
class Endpoint:
    host: str
    port: int

    def validate(self) -> None:
        if not self.host or not 1 <= self.port <= 65535:
            raise ValueError("invalid endpoint")
