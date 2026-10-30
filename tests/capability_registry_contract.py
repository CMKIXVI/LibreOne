from libreone.system.capability_registry import CapabilityRegistry
from libreone.system.capabilities import Capability


def verify_capability_registry_contract() -> bool:
    registry = CapabilityRegistry()
    capability = Capability("compute", "1", "compute")
    registry.register(capability)
    return registry.get(capability.key) == capability
