from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


class Executor:
    """Execute trusted runtime operations with deterministic validation."""

    def execute(self, operation: Callable[[], T]) -> T:
        if not callable(operation):
            raise TypeError("operation must be callable")
        return operation()
