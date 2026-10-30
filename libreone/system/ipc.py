from dataclasses import dataclass
from queue import Empty, Queue
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Channel(Generic[T]):
    _queue: Queue[T]

    @classmethod
    def create(cls) -> "Channel[T]":
        return cls(Queue())

    def send(self, value: T) -> None:
        self._queue.put_nowait(value)

    def receive(self) -> T:
        try:
            return self._queue.get_nowait()
        except Empty as exc:
            raise RuntimeError("channel is empty") from exc

    @property
    def pending(self) -> int:
        return self._queue.qsize()

    def close(self) -> None:
        if self._queue is None:
            raise RuntimeError("channel is closed")
        self._queue = None  # type: ignore[assignment]
