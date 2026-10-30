from libreone.system.namespaces import Namespace


def verify_namespace_contract() -> bool:
    namespace = Namespace("tenant", "system")
    return namespace.key == "tenant/system"
