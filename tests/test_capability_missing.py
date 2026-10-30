import pytest
from libreone.system.capability_registry import CapabilityRegistry


def test_missing_capability_is_not_returned():
    registry = CapabilityRegistry()
    with pytest.raises(KeyError):
        registry.get("missing@1")
