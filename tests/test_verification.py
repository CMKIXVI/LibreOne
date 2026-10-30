from libreone.system.verification import verify_digest


def test_verify_digest_accepts_equal_values():
    assert verify_digest("abc123", "ABC123")


def test_verify_digest_rejects_different_values():
    assert not verify_digest("abc123", "abc124")
