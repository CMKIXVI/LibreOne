from collections import deque
from typing import Callable


class Scheduler:
    def __init__(self) -> None:
        self._queue: deque[Callable[[], object]] = deque()

    def submit(self, task: Callable[[], object]) -> None:
        if not callable(task):
            raise TypeError("scheduled task must be callable")
        self._queue.append(task)

    def run_once(self) -> object | None:
        if not self._queue:
            return None
        return self._queue.popleft()()

    @property
    def pending(self) -> int:
        return len(self._queue)
