from libreone.system.health import Health
from libreone.system.lifecycle import Lifecycle
from libreone.system.lifecycle_health import lifecycle_health


def test_running_lifecycle_is_healthy():
    lifecycle = Lifecycle()
    lifecycle.start()
    report = lifecycle_health(lifecycle)
    assert report.status is Health.OK
    assert report.detail == "running"


def test_stopped_lifecycle_is_degraded():
    report = lifecycle_health(Lifecycle())
    assert report.status is Health.DEGRADED
    assert report.detail == "stopped"


def test_failed_lifecycle_is_failed():
    lifecycle = Lifecycle()
    lifecycle.start()
    lifecycle.fail()
    report = lifecycle_health(lifecycle)
    assert report.status is Health.FAILED
    assert report.detail == "failed"
