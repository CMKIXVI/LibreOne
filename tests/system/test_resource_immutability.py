from dataclasses import FrozenInstanceError

import pytest

from libreone.system.resources import ResourceLimits


def test_resource_limits_are_immutable():
    limits = ResourceLimits(memory_bytes=1024)
    with pytest.raises(FrozenInstanceError):
        limits.memory_bytes = 2048
