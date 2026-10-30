from abc import ABC, abstractmethod
from .health import Health, HealthReport


class SystemService(ABC):
    @abstractmethod
    def start(self) -> None: ...

    @abstractmethod
    def stop(self) -> None: ...

    def health(self) -> HealthReport:
        return HealthReport("system", Health.OK)
