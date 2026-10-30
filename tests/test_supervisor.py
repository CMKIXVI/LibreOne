from libreone.system.health import Health, HealthReport
from libreone.system.supervisor import Supervisor


class Service:
    def __init__(self, name, log):
        self.name = name
        self.log = log

    def start(self):
        self.log.append("start:" + self.name)

    def stop(self):
        self.log.append("stop:" + self.name)

    def health(self):
        return HealthReport(self.name, Health.OK)


def test_supervisor_starts_and_stops_in_order():
    log = []
    supervisor = Supervisor((Service("a", log), Service("b", log)))
    supervisor.start()
    supervisor.stop()
    assert log == ["start:a", "start:b", "stop:b", "stop:a"]
