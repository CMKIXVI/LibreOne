from libreone.system.retry import RetryPolicy


def test_retry_policy_defaults():
    policy = RetryPolicy()
    assert policy.attempts >= 1


def test_retry_policy_rejects_invalid_attempts():
    try:
        RetryPolicy(attempts=0)
    except ValueError:
        return
    raise AssertionError("RetryPolicy must reject zero attempts")
