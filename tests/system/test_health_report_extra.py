from libreone.system.health import Health, HealthReport


def test_health_report_can_be_degraded():
    report = HealthReport(Health.DEGRADED, "partial")
    assert report.status is Health.DEGRADED
