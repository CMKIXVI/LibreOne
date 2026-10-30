from .service import SystemService


class Supervisor:
    def __init__(self, services: tuple[SystemService, ...] | list[SystemService] = ()) -> None:
        self._services = tuple(services)
        self._started: list[SystemService] = []

    def start(self) -> None:
        if self._started:
            raise RuntimeError("supervisor is already started")
        started: list[SystemService] = []
        try:
            for service in self._services:
                service.start()
                started.append(service)
        except Exception:
            for service in reversed(started):
                try:
                    service.stop()
                except Exception:
                    pass
            self._started.clear()
            raise
        self._started = started

    def stop(self) -> None:
        if not self._started:
            return
        errors: list[Exception] = []
        for service in reversed(self._started):
            try:
                service.stop()
            except Exception as exc:
                errors.append(exc)
        self._started.clear()
        if errors:
            raise RuntimeError("one or more services failed to stop") from errors[0]


ServiceSupervisor = Supervisor
