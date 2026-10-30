from libreone.system.service import SystemService


class TestService(SystemService):
    def start(self):
        self.started = True

    def stop(self):
        self.started = False


def test_service_lifecycle():
    service = TestService()
    service.start()
    assert service.started
    service.stop()
    assert not service.started
