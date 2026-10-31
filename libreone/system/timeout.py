from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Timeout:
    seconds: float

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        if not isinstance(self.seconds, (int, float)) or isinstance(self.seconds, bool):
            raise TypeError("timeout must be numeric")
        if not math.isfinite(float(self.seconds)):
            raise ValueError("timeout must be finite")
        if self.seconds <= 0:
            raise ValueError("timeout must be positive")
