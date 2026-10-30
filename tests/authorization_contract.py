from libreone.system.authorization import Authorizer


def verify_authorization_contract() -> bool:
    return hasattr(Authorizer, "authorize") or hasattr(Authorizer, "check")
