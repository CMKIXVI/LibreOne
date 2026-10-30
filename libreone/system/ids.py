from uuid import UUID, uuid4


def new_system_id() -> UUID:
    return uuid4()
