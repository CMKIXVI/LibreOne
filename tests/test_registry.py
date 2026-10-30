from libreone.system.registry import Registry


def test_generic_registry():
    registry = Registry()
    registry.register("key", 42)
    assert registry.get("key") == 42
