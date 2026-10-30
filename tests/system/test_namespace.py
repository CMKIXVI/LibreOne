from libreone.system.namespaces import Namespace
from libreone.system.tenant import Tenant


def test_namespace_key_is_stable():
    tenant = Tenant("tenant")
    namespace = Namespace(tenant, "runtime")
    assert namespace.key == "tenant/runtime"
