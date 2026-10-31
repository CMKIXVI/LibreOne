from dataclasses import dataclass, field
from threading import Lock


@dataclass
class Counter:
    value: int = 0
    _lock: Lock = field(default_factory=Lock, init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        if not isinstance(self.value, int) or isinstance(self.value, bool):
            raise TypeError("counter value must be an integer")
        if self.value < 0:
            raise ValueError("counter value must be non-negative")

    def increment(self, amount: int = 1) -> None:
        if not isinstance(amount, int) or isinstance(amount, bool):
            raise TypeError("counter increment must be an integer")
        if amount < 0:
            raise ValueError("counter increment must be non-negative")
        with self._lock:
            self.value += amount

    def snapshot(self) -> int:
        with self._lock:
            return self.value
