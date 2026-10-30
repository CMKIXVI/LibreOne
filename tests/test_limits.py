from libreone.system.limits import ConcurrencyLimit


def test_concurrency_limit_is_constructible():
    limit = ConcurrencyLimit(4)
    assert limit.value == 4
