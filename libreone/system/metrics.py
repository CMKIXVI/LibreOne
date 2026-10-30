from dataclasses import dataclass


@dataclass
class Counter:
    value: int = 0

    def increment(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("counter increment must be non-negative")
        self.value += amount
