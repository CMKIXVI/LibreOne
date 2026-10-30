from libreone.system.capabilities import Capability


def verify_capability_contract() -> bool:
    capability = Capability("compute", "1", "compute")
    return capability.key == "compute@1"
