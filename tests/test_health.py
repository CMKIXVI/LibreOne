from libreone.system.health import Health, HealthReport


def test_health_report_defaults_to_ok_when_requested():
    report = HealthReport(Health.OK, "ready")
    assert report.status is Health.OK
    assert report.message == "ready"
