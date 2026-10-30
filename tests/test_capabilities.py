import pytest

from libreone.system.capabilities import Capability
from libreone.system.capability_registry import CapabilityRegistry


def test_capability_registry():
    registry = CapabilityRegistry()
    capability = Capability("storage", "1", "storage access")
    registry.register(capability)
    assert registry.get(capability.key) == capability


def test_capability_rejects_empty_name():
    with pytest.raises(ValueError, match="name cannot be empty"):
        Capability(" ", "1")


def test_capability_rejects_empty_version():
    with pytest.raises(ValueError, match="version cannot be empty"):
        Capability("storage", "")


def test_capability_rejects_non_string_description():
    with pytest.raises(TypeError, match="description must be a string"):
        Capability("storage", "1", 123)


def test_capability_key_has_consistent_hash_semantics():
    capability = Capability("storage", "1")
    assert capability.key == "storage@1"
    assert hash(capability.key) == hash("storage@1")
