from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


class Executor:
    def execute(self, operation: Callable[[], T]) -> T:
        return operation()
