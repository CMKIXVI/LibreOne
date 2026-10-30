from libreone.system.limits import ConcurrencyLimit


def test_concurrency_limit():
    limit = ConcurrencyLimit(2)
    assert limit.maximum == 2
