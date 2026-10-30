from libreone.system.identity import Identity


def verify_identity_contract() -> bool:
    return Identity().id != Identity().id
