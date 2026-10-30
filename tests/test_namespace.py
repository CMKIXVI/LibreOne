from libreone.system.namespaces import Namespace
from libreone.system.tenant import Tenant


def test_namespace_key_is_stable():
    tenant = Tenant("tenant")
    namespace = Namespace(tenant, "system")
    assert namespace.key.endswith(":system")
