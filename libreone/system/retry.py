from dataclasses import dataclass


@dataclass(frozen=True)
class RetryPolicy:
    attempts: int = 3

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        if not isinstance(self.attempts, int) or isinstance(self.attempts, bool):
            raise TypeError("attempts must be an integer")
        if self.attempts < 1:
            raise ValueError("attempts must be positive")
