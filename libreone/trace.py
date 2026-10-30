from contextlib import contextmanager
from dataclasses import dataclass
from time import perf_counter
from collections.abc import Iterator

@dataclass(frozen=True, slots=True)
class Span:
    name: str
    duration_ms: float

@contextmanager
def span(name: str) -> Iterator[Span]:
    start = perf_counter()
    result = Span(name, 0.0)
    try:
        yield result
    finally:
        object.__setattr__(result, "duration_ms", (perf_counter() - start) * 1000)
