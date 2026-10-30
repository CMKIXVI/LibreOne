import pytest

from libreone.system.namespaces import Namespace
from libreone.system.tenant import Tenant


def test_tenant_namespace_identity():
    tenant = Tenant("acme")
    namespace = Namespace(tenant, "default")
    assert namespace.key == "acme/default"


def test_tenant_rejects_empty_name():
    with pytest.raises(ValueError):
        Tenant("")
