from dataclasses import dataclass


@dataclass(frozen=True)
class RetryPolicy:
    attempts: int = 3

    def validate(self) -> None:
        if self.attempts < 1:
            raise ValueError("attempts must be positive")
