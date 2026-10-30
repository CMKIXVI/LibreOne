from dataclasses import dataclass


@dataclass(frozen=True)
class Timeout:
    seconds: float

    def validate(self) -> None:
        if self.seconds <= 0:
            raise ValueError("timeout must be positive")
