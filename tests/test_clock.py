from libreone.system.clock import monotonic_ticks


def test_monotonic_ticks_increase():
    first = monotonic_ticks()
    second = monotonic_ticks()
    assert second >= first
