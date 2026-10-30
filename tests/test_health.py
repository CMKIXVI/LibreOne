import pytest

from libreone.system.health import Health, HealthReport


def test_health_report_fields_are_stable():
    report = HealthReport("system", Health.OK, "ready")
    assert report.component == "system"
    assert report.status is Health.OK
    assert report.detail == "ready"


def test_health_report_is_immutable():
    report = HealthReport("system", Health.OK)
    with pytest.raises(Exception):
        report.status = Health.FAILED


def test_health_values_are_distinct():
    assert {Health.OK, Health.DEGRADED, Health.FAILED} == {
        Health("ok"), Health("degraded"), Health("failed")
    }
