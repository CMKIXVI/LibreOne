from dataclasses import FrozenInstanceError

import pytest

from libreone.system.policy import Decision, Policy


def test_policy_is_immutable():
    policy = Policy("read", Decision.ALLOW)
    with pytest.raises(FrozenInstanceError):
        policy.action = "write"
