from libreone.system.registry import Registry


def verify_registry_contract() -> bool:
    registry = Registry()
    registry.register("core", object())
    return registry.get("core") is not None
