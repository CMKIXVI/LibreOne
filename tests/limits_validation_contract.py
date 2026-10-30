from libreone.system.limits import ConcurrencyLimit


def verify_limit_validation() -> bool:
    try:
        ConcurrencyLimit(0)
    except (ValueError, TypeError):
        return True
    return False
