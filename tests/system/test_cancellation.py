from libreone.system.cancellation import CancellationToken


def test_cancellation_token():
    token = CancellationToken()
    assert not token.cancelled
    token.cancel()
    assert token.cancelled
