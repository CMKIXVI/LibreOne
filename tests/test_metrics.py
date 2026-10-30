from libreone.system.metrics import Counter


def test_counter_increments():
    counter = Counter()
    counter.increment()
    counter.increment(2)
    assert counter.value == 3
