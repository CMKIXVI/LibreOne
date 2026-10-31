import pytest

from libreone.system.metrics import Counter


def test_counter_increments():
    counter = Counter()
    counter.increment()
    counter.increment(2)
    assert counter.value == 3
    assert counter.snapshot() == 3


def test_counter_rejects_invalid_initial_value():
    with pytest.raises(TypeError, match="counter value"):
        Counter(True)
    with pytest.raises(ValueError, match="counter value"):
        Counter(-1)


def test_counter_rejects_invalid_increment():
    counter = Counter()
    with pytest.raises(TypeError, match="counter increment"):
        counter.increment(True)
    with pytest.raises(TypeError, match="counter increment"):
        counter.increment(1.5)
    with pytest.raises(ValueError, match="counter increment"):
        counter.increment(-1)
