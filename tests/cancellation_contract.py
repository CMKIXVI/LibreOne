from libreone.system.cancellation import CancellationToken


def verify_cancellation_contract() -> bool:
    token = CancellationToken()
    assert not token.cancelled
    token.cancel()
    return token.cancelled
