from libreone.system.health import Health, HealthReport


def verify_health_contract() -> bool:
    report = HealthReport(Health.OK, "healthy")
    return report.status is Health.OK
