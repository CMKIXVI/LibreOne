from libreone.system.namespaces import Namespace
from libreone.system.tenant import Tenant


def test_namespace_is_tenant_scoped():
    tenant = Tenant("acme")
    namespace = Namespace(tenant, "default")
    assert namespace.key == f"{tenant.id}:default"
