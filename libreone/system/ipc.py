from dataclasses import dataclass
from queue import Queue
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
        return self._queue.get_nowait()
