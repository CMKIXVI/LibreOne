from libreone.system.health import Health
from libreone.system.service import SystemService


class _TestService(SystemService):
    def __init__(self):
        self.started = False

    def start(self):
        self.started = True

    def stop(self):
        self.started = False

    def health(self):
        return Health.OK


def test_service_contract():
    service = _TestService()
    service.start()
    assert service.started
    assert service.health() is Health.OK
    service.stop()
    assert not service.started
