from libreone.system.retry import RetryPolicy


def verify_retry_contract() -> bool:
    return RetryPolicy().attempts == 3
