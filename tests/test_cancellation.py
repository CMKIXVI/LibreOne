from libreone.system.cancellation import CancellationToken


def test_cancellation_is_idempotent():
    token = CancellationToken()
    token.cancel()
    token.cancel()
    assert token.cancelled
