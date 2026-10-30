from libreone.system.service import SystemService


def verify_service_contract() -> bool:
    return hasattr(SystemService, "start") and hasattr(SystemService, "stop")
