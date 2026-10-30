from libreone.system.capabilities import Capability
from libreone.system.capability_registry import CapabilityRegistry


def test_capability_registry():
    capability = Capability("storage", "1", "Storage access")
    registry = CapabilityRegistry()
    registry.register(capability)
    assert registry.get(capability.key) == capability
