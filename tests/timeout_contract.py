from libreone.system.timeout import Timeout


def verify_timeout_contract() -> bool:
    return Timeout(5).seconds == 5
