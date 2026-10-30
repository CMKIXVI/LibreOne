import pytest

from libreone.system.capabilities import Capability
from libreone.system.capability_registry import CapabilityRegistry


def test_capability_registry_rejects_duplicate_key():
    registry = CapabilityRegistry()
    capability = Capability("ai", "1", "AI")
    registry.register(capability)
    with pytest.raises(Exception):
        registry.register(capability)
