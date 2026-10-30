from collections import Counter

class Metrics:
    def __init__(self) -> None:
        self._counters: Counter[str] = Counter()

    def increment(self, name: str, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("amount must not be negative")
        self._counters[name] += amount

    def value(self, name: str) -> int:
        return self._counters[name]
