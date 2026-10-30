from libreone.system.clock import monotonic_ticks


def test_monotonic_ticks_increases():
    first = monotonic_ticks()
    second = monotonic_ticks()
    assert second >= first
