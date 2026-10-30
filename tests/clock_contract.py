from libreone.system.clock import monotonic_ticks


def verify_clock_contract() -> bool:
    first = monotonic_ticks()
    second = monotonic_ticks()
    return second >= first
