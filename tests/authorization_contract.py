from libreone.system.authorization import Authorizer
from libreone.system.policy import Decision, Policy


def verify_authorization_contract() -> bool:
    authorizer = Authorizer((Policy("execute", Decision.ALLOW),))
    return authorizer.allowed() is True
