import pytest

from libreone.system.capabilities import Capability
from libreone.system.capability_registry import CapabilityRegistry


def test_registry_resolves_canonical_and_legacy_key_forms():
    registry = CapabilityRegistry()
    capability = Capability("compute", "1", "compute")
    registry.register(capability)

    assert registry.resolve("compute:1") is capability
    assert registry.resolve("compute@1") is capability


def test_registry_rejects_invalid_key_forms():
    registry = CapabilityRegistry()
    for key in ("", "compute", ":1", "compute:", "compute@1:2"):
        with pytest.raises((TypeError, ValueError)):
            registry.resolve(key)


def test_registry_rejects_non_capability_registration():
    with pytest.raises(TypeError):
        CapabilityRegistry().register(object())
