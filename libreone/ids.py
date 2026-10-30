from uuid import UUID, uuid4


def new_id() -> UUID:
    """Return a cryptographically strong random identifier."""
    return uuid4()
