from dataclasses import dataclass


@dataclass(frozen=True)
class ConcurrencyLimit:
    maximum: int

    def __post_init__(self) -> None:
        self.validate()

    @property
    def value(self) -> int:
        return self.maximum

    def validate(self) -> None:
        if not isinstance(self.maximum, int) or isinstance(self.maximum, bool):
            raise TypeError("maximum concurrency must be an integer")
        if self.maximum < 1:
            raise ValueError("maximum concurrency must be positive")
