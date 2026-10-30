from libreone.system.health import Health, HealthReport
from libreone.system.supervisor import Supervisor


class _Service:
    def __init__(self, name: str, log: list[str]) -> None:
        self.name = name
        self.log = log

    def start(self) -> None:
        self.log.append(f"start:{self.name}")

    def stop(self) -> None:
        self.log.append(f"stop:{self.name}")

    def health(self) -> HealthReport:
        return HealthReport(self.name, Health.OK)


def verify_supervisor_contract() -> bool:
    log: list[str] = []
    supervisor = Supervisor((_Service("a", log), _Service("b", log)))
    supervisor.start()
    supervisor.stop()
    return log == ["start:a", "start:b", "stop:b", "stop:a"]
