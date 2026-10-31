from dataclasses import dataclass
import math


@dataclass(frozen=True)
class RetryPolicy:
    attempts: int = 3
    initial_delay: float = 0.0
    multiplier: float = 2.0
    max_delay: float | None = None

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        if not isinstance(self.attempts, int) or isinstance(self.attempts, bool):
            raise TypeError("attempts must be an integer")
        if self.attempts < 1:
            raise ValueError("attempts must be positive")
        for name, value in (("initial_delay", self.initial_delay), ("multiplier", self.multiplier)):
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise TypeError(f"{name} must be numeric")
            if not math.isfinite(float(value)):
                raise ValueError(f"{name} must be finite")
        if self.initial_delay < 0:
            raise ValueError("initial_delay cannot be negative")
        if self.multiplier < 1:
            raise ValueError("multiplier must be at least 1")
        if self.max_delay is not None:
            if not isinstance(self.max_delay, (int, float)) or isinstance(self.max_delay, bool):
                raise TypeError("max_delay must be numeric or None")
            if not math.isfinite(float(self.max_delay)):
                raise ValueError("max_delay must be finite")
            if self.max_delay < 0:
                raise ValueError("max_delay cannot be negative")

    def delay_for(self, retry_number: int) -> float:
        """Return the deterministic delay before a retry, using zero-based numbering."""
        if not isinstance(retry_number, int) or isinstance(retry_number, bool):
            raise TypeError("retry_number must be an integer")
        if retry_number < 0 or retry_number >= self.attempts - 1:
            raise ValueError("retry_number is outside the retry range")
        delay = float(self.initial_delay) * (float(self.multiplier) ** retry_number)
        if self.max_delay is not None:
            delay = min(delay, float(self.max_delay))
        return delay
