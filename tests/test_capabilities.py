from libreone.system.capabilities import Capability
from libreone.system.capability_registry import CapabilityRegistry


def test_capability_registry():
    registry = CapabilityRegistry()
    capability = Capability("storage", "1", "storage access")
    registry.register(capability)
    assert registry.get(capability.key) == capability
