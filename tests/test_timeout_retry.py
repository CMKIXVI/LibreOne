from libreone.system.retry import RetryPolicy
from libreone.system.timeout import Timeout


def test_retry_policy_and_timeout_validate():
    assert RetryPolicy(attempts=3).attempts == 3
    assert Timeout(seconds=1).seconds == 1
