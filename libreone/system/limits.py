from dataclasses import dataclass


@dataclass(frozen=True)
class ConcurrencyLimit:
    maximum: int

    def validate(self) -> None:
        if self.maximum < 1:
            raise ValueError("maximum concurrency must be positive")
