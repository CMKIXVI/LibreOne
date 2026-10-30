from libreone.system.clock import monotonic_ticks

def test_clock_is_monotonic_source():
    assert monotonic_ticks() >= 0
