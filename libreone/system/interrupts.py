from collections.abc import Callable


class InterruptTable:
    def __init__(self) -> None:
        self._handlers: dict[int, Callable[..., None]] = {}

    def register(self, number: int, handler: Callable[..., None]) -> None:
        if number < 0 or number in self._handlers:
            raise ValueError("invalid or duplicate interrupt number")
        self._handlers[number] = handler

    def dispatch(self, number: int, *args: object) -> None:
        self._handlers[number](*args)
