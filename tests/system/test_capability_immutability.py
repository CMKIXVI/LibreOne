from dataclasses import FrozenInstanceError

import pytest

from libreone.system.capabilities import Capability


def test_capability_is_immutable():
    capability = Capability("ai", "1", "AI")
    with pytest.raises(FrozenInstanceError):
        capability.version = "2"
