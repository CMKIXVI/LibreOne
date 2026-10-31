import math

import pytest

from libreone.system.retry import RetryPolicy


def test_retry_policy_defaults_are_deterministic():
    policy = RetryPolicy()
    assert policy.attempts == 3
    assert policy.initial_delay == 0.0
    assert policy.multiplier == 2.0
    assert policy.max_delay is None


def test_retry_policy_calculates_bounded_backoff():
    policy = RetryPolicy(attempts=4, initial_delay=1, multiplier=2, max_delay=2.5)
    assert policy.delay_for(0) == 1.0
    assert policy.delay_for(1) == 2.0
    assert policy.delay_for(2) == 2.5


def test_retry_policy_rejects_invalid_numeric_values():
    with pytest.raises(TypeError):
        RetryPolicy(initial_delay=True)
    with pytest.raises(ValueError):
        RetryPolicy(initial_delay=-1)
    with pytest.raises(ValueError):
        RetryPolicy(initial_delay=math.inf)
    with pytest.raises(ValueError):
        RetryPolicy(multiplier=0.5)
    with pytest.raises(ValueError):
        RetryPolicy(max_delay=-1)


def test_retry_policy_rejects_invalid_retry_number():
    policy = RetryPolicy(attempts=2, initial_delay=1)
    with pytest.raises(TypeError):
        policy.delay_for(True)
    with pytest.raises(ValueError):
        policy.delay_for(-1)
    with pytest.raises(ValueError):
        policy.delay_for(1)


def test_retry_policy_bounds_overflowing_backoff():
    bounded = RetryPolicy(attempts=3, initial_delay=1e308, multiplier=10, max_delay=60)
    assert bounded.delay_for(1) == 60.0

    unbounded = RetryPolicy(attempts=4, initial_delay=1e308, multiplier=10)
    with pytest.raises(ValueError, match="exceeds finite range"):
        unbounded.delay_for(2)
