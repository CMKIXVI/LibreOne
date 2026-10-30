from libreone.system.supervisor import Supervisor


class Service:
    def __init__(self, name, log):
        self.name = name
        self.log = log

    def start(self):
        self.log.append("start:" + self.name)

    def stop(self):
        self.log.append("stop:" + self.name)


def test_supervisor_starts_and_stops_in_order():
    log = []
    supervisor = Supervisor()
    supervisor.add(Service("a", log))
    supervisor.add(Service("b", log))
    supervisor.start_all()
    supervisor.stop_all()
    assert log == ["start:a", "start:b", "stop:b", "stop:a"]
