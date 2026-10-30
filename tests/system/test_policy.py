from libreone.system.authorization import Authorizer
from libreone.system.policy import Decision, Policy


def test_policy_authorization():
    allow = Policy("read", Decision.ALLOW)
    deny = Policy("write", Decision.DENY)
    assert allow.permits("read")
    assert not allow.permits("write")
    assert Authorizer([allow]).authorize("read")
    assert not Authorizer([allow]).authorize("write")
    assert not Authorizer([deny]).authorize("write")
