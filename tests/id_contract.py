from libreone.system.ids import new_system_id


def verify_id_contract() -> bool:
    return new_system_id() != new_system_id()
