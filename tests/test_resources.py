from libreone.system.resources import ResourceLimits


def test_resource_limits_defaults_are_valid():
    limits = ResourceLimits()
    assert limits.cpu_seconds > 0
    assert limits.memory_bytes > 0


def test_resource_limits_reject_non_positive_values():
    try:
        ResourceLimits(cpu_seconds=0)
    except ValueError:
        return
    raise AssertionError("invalid resource limit accepted")
