import pytest

from libreone.system.authorization import Authorizer
from libreone.system.policy import Decision, Policy


def test_authorizer_allows_when_all_policies_permit():
    authorizer = Authorizer((Policy("read", Decision.ALLOW), Policy("execute", Decision.ALLOW)))
    assert authorizer.allowed() is True


def test_authorizer_denies_when_any_policy_denies():
    authorizer = Authorizer((Policy("read", Decision.ALLOW), Policy("execute", Decision.DENY)))
    assert authorizer.allowed() is False


def test_authorizer_without_policies_is_default_deny():
    authorizer = Authorizer()
    assert authorizer.allowed() is False
    assert authorizer.authorize("read") is False


def test_authorizer_resource_must_match_all_policies():
    authorizer = Authorizer((Policy("read", Decision.ALLOW),))
    assert authorizer.authorize("read") is True
    assert authorizer.authorize("write") is False


def test_policy_validates_name_and_decision():
    with pytest.raises(ValueError, match="policy name cannot be empty"):
        Policy(" ", Decision.ALLOW)
    with pytest.raises(TypeError, match="policy decision"):
        Policy("read", "allow")


def test_policy_normalizes_names_and_rejects_invalid_resources():
    policy = Policy(" read ", Decision.ALLOW)
    assert policy.name == "read"
    assert policy.permits(" read ") is True
    assert policy.permits(" ") is False
    assert policy.permits(123) is False
