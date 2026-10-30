from libreone.system.limits import ConcurrencyLimit


def verify_limits_contract() -> bool:
    return ConcurrencyLimit(4).limit == 4
