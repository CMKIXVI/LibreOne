import hmac


def verify_digest(expected: str, actual: str) -> bool:
    return hmac.compare_digest(expected.lower(), actual.lower())
