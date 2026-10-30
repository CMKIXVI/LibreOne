import pytest

from libreone.system.registry import Registry


def test_registry_rejects_duplicate_key():
    registry = Registry()
    registry.register("x", 1)
    with pytest.raises(Exception):
        registry.register("x", 2)
