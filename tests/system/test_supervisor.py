from libreone.system.health import Health
from libreone.system.service import SystemService
from libreone.system.supervisor import ServiceSupervisor


class Service(SystemService):
    def __init__(self, events, name):
        self.events = events
        self.name = name

    def start(self):
        self.events.append(f"start:{self.name}")

    def stop(self):
        self.events.append(f"stop:{self.name}")

    def health(self):
        return Health.OK


def test_supervisor_stops_in_reverse_order():
    events = []
    supervisor = ServiceSupervisor([Service(events, "a"), Service(events, "b")])
    supervisor.start()
    supervisor.stop()
    assert events == ["start:a", "start:b", "stop:b", "stop:a"]
