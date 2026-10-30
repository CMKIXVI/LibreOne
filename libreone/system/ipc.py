from dataclasses import dataclass, field
from queue import Empty, Queue
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Channel(Generic[T]):
    _queue: Queue[T] | None = field(default_factory=Queue)

    @classmethod
    def create(cls) -> "Channel[T]":
        return cls()

    def _require_open(self) -> Queue[T]:
        if self._queue is None:
            raise RuntimeError("channel is closed")
        return self._queue

    def send(self, value: T) -> None:
        self._require_open().put_nowait(value)

    def receive(self) -> T:
        try:
            return self._require_open().get_nowait()
        except Empty as exc:
            raise RuntimeError("channel is empty") from exc

    @property
    def pending(self) -> int:
        return self._require_open().qsize()

    def close(self) -> None:
        if self._queue is None:
            raise RuntimeError("channel is already closed")
        self._queue = None
