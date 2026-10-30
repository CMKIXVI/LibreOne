from libreone.system.registry import Registry


def test_registry_round_trip():
    registry = Registry()
    registry.register("system", 42)
    assert registry.get("system") == 42
    assert "system" in registry
