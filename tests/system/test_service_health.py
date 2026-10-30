from libreone.system.health import Health
from libreone.system.service import SystemService


class HealthyService(SystemService):
    def start(self):
        pass

    def stop(self):
        pass

    def health(self):
        return Health.OK


def test_service_health_is_callable():
    assert HealthyService().health() is Health.OK
