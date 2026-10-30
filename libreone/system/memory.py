from dataclasses import dataclass


@dataclass(frozen=True)
class MemoryRegion:
    start: int
    size: int

    @property
    def end(self) -> int:
        return self.start + self.size

    def contains(self, address: int) -> bool:
        return self.start <= address < self.end
