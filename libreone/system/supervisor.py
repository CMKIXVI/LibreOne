from .service import SystemService


class Supervisor:
    def __init__(self, services: tuple[SystemService, ...] = ()) -> None:
        self._services = services

    def start(self) -> None:
        for service in self._services:
            service.start()

    def stop(self) -> None:
        for service in reversed(self._services):
            service.stop()
