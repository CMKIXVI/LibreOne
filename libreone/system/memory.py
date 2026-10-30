from dataclasses import dataclass


@dataclass(frozen=True)
class MemoryRegion:
    start: int
    size: int

    def __post_init__(self) -> None:
        if not isinstance(self.start, int) or not isinstance(self.size, int):
            raise TypeError("memory region bounds must be integers")
        if self.start < 0:
            raise ValueError("memory region start must be non-negative")
        if self.size <= 0:
            raise ValueError("memory region size must be positive")

    @property
    def end(self) -> int:
        return self.start + self.size

    def contains(self, address: int) -> bool:
        return self.start <= address < self.end
