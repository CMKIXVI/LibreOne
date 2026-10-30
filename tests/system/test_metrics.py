from libreone.system.metrics import Counter


def test_counter_increments():
    counter = Counter()
    assert counter.value == 0
    counter.increment()
    counter.increment(2)
    assert counter.value == 3
