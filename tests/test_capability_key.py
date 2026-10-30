from libreone.system.capabilities import Capability


def test_capability_key_is_stable():
    capability = Capability("compute", "1", "compute")
    assert capability.key == "compute@1"
