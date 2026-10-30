from abc import ABC, abstractmethod
from .health import HealthReport


class SystemService(ABC):
    @abstractmethod
    def start(self) -> None: ...

    @abstractmethod
    def stop(self) -> None: ...

    @abstractmethod
    def health(self) -> HealthReport: ...
