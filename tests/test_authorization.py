from libreone.system.authorization import Authorizer
from libreone.system.policy import Decision, Policy


def test_authorizer_allows_when_all_policies_permit():
    authorizer = Authorizer((Policy("read", Decision.ALLOW), Policy("execute", Decision.ALLOW)))
    assert authorizer.allowed() is True


def test_authorizer_denies_when_any_policy_denies():
    authorizer = Authorizer((Policy("read", Decision.ALLOW), Policy("execute", Decision.DENY)))
    assert authorizer.allowed() is False


def test_authorizer_without_policies_is_permissive():
    assert Authorizer().allowed() is True
