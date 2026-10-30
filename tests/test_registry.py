import pytest

from libreone.system.registry import Registry


def test_generic_registry():
    registry = Registry()
    registry.register("key", 42)
    assert registry.get("key") == 42


def test_registry_normalizes_names():
    registry = Registry()
    registry.register(" key ", 42)
    assert registry.get("key") == 42
    assert " key " in registry


def test_registry_rejects_empty_or_non_string_names():
    registry = Registry()
    with pytest.raises(ValueError, match="name cannot be empty"):
        registry.register(" ", 1)
    with pytest.raises(TypeError, match="name must be a string"):
        registry.register(123, 1)


def test_registry_rejects_duplicate_normalized_names():
    registry = Registry()
    registry.register("key", 42)
    with pytest.raises(ValueError, match="already registered: key"):
        registry.register(" key ", 43)


def test_registry_contains_rejects_invalid_names_without_raising():
    registry = Registry()
    registry.register("key", 42)
    assert 123 not in registry
    assert " " not in registry
