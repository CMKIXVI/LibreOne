from libreone.system.capabilities import Capability


def test_capability_key():
    capability = Capability("ai", "1.0", "AI runtime")
    assert capability.key == "ai:1.0"
