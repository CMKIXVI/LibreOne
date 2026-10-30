from collections.abc import Callable
from time import sleep
from typing import TypeVar

T = TypeVar("T")

def retry(operation: Callable[[], T], attempts: int = 3, delay: float = 0.25) -> T:
    if attempts < 1:
        raise ValueError("attempts must be positive")
    last: Exception | None = None
    for index in range(attempts):
        try:
            return operation()
        except Exception as exc:
            last = exc
            if index + 1 < attempts:
                sleep(delay * (2 ** index))
    assert last is not None
    raise last
