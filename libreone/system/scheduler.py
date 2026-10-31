from collections import deque
from threading import Lock
from typing import Callable


class Scheduler:
    def __init__(self, max_pending: int | None = None) -> None:
        if max_pending is not None and (not isinstance(max_pending, int) or isinstance(max_pending, bool)):
            raise TypeError("max_pending must be an integer or None")
        if max_pending is not None and max_pending < 1:
            raise ValueError("max_pending must be positive")
        self._queue: deque[tuple[int, Callable[[], object]]] = deque()
        self._lock = Lock()
        self._next_id = 1
        self._max_pending = max_pending
        self._closed = False

    def submit(self, task: Callable[[], object]) -> int:
        if not callable(task):
            raise TypeError("scheduled task must be callable")
        with self._lock:
            if self._closed:
                raise RuntimeError("scheduler is closed")
            if self._max_pending is not None and len(self._queue) >= self._max_pending:
                raise RuntimeError("scheduler queue is full")
            task_id = self._next_id
            self._next_id += 1
            self._queue.append((task_id, task))
            return task_id

    def cancel(self, task_id: int) -> bool:
        if not isinstance(task_id, int) or isinstance(task_id, bool):
            raise TypeError("task_id must be an integer")
        with self._lock:
            for index, (queued_id, _) in enumerate(self._queue):
                if queued_id == task_id:
                    del self._queue[index]
                    return True
        return False

    def run_once(self) -> object | None:
        with self._lock:
            if not self._queue:
                return None
            _, task = self._queue.popleft()
        return task()

    def close(self) -> None:
        with self._lock:
            if self._closed:
                raise RuntimeError("scheduler is already closed")
            self._closed = True
            self._queue.clear()

    @property
    def closed(self) -> bool:
        with self._lock:
            return self._closed

    @property
    def pending(self) -> int:
        with self._lock:
            return len(self._queue)
