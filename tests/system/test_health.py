from libreone.system.health import Health, HealthReport


def test_health_report():
    report = HealthReport(Health.OK, "system ready")
    assert report.status is Health.OK
    assert report.message == "system ready"
