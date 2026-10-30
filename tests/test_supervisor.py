import pytest

from libreone.system.health import Health, HealthReport
from libreone.system.supervisor import Supervisor


class Service:
    def __init__(self, name, log, fail_start=False, fail_stop=False):
        self.name = name
        self.log = log
        self.fail_start = fail_start
        self.fail_stop = fail_stop

    def start(self):
        self.log.append("start:" + self.name)
        if self.fail_start:
            raise RuntimeError("start failed")

    def stop(self):
        self.log.append("stop:" + self.name)
        if self.fail_stop:
            raise RuntimeError("stop failed")

    def health(self):
        return HealthReport(self.name, Health.OK)


def test_supervisor_starts_and_stops_in_order():
    log = []
    supervisor = Supervisor((Service("a", log), Service("b", log)))
    supervisor.start()
    supervisor.stop()
    assert log == ["start:a", "start:b", "stop:b", "stop:a"]


def test_supervisor_rolls_back_started_services_when_start_fails():
    log = []
    supervisor = Supervisor((Service("a", log), Service("b", log, fail_start=True)))
    with pytest.raises(RuntimeError):
        supervisor.start()
    assert log == ["start:a", "start:b", "stop:a"]
    supervisor.start()


def test_supervisor_rejects_double_start():
    supervisor = Supervisor((Service("a", []),))
    supervisor.start()
    with pytest.raises(RuntimeError):
        supervisor.start()
    supervisor.stop()


def test_supervisor_stop_is_idempotent():
    supervisor = Supervisor((Service("a", []),))
    supervisor.stop()
    supervisor.start()
    supervisor.stop()
    supervisor.stop()


def test_supervisor_aggregates_stop_failure():
    log = []
    supervisor = Supervisor((Service("a", log, fail_stop=True), Service("b", log)))
    supervisor.start()
    with pytest.raises(RuntimeError):
        supervisor.stop()
    assert log == ["start:a", "start:b", "stop:b", "stop:a"]
