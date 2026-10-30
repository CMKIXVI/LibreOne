from libreone.system.authorization import Authorizer
from libreone.system.policy import Decision, Policy


def test_authorizer_requires_all_policies():
    authorizer = Authorizer([
        Policy("read", Decision.ALLOW),
        Policy("read", Decision.DENY),
    ])
    assert not authorizer.authorize("read")
