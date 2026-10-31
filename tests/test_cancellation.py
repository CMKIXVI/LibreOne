import pytest

from libreone.system.cancellation import CancellationToken


def test_cancellation_token_starts_clear():
    token = CancellationToken()
    assert token.cancelled is False
    token.raise_if_cancelled()


def test_cancellation_is_idempotent():
    token = CancellationToken()
    token.cancel()
    token.cancel()
    assert token.cancelled is True
    with pytest.raises(RuntimeError, match="operation cancelled"):
        token.raise_if_cancelled()
