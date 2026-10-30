import pytest

from libreone.system.namespaces import Namespace
from libreone.system.tenant import Tenant


def test_namespace_key_is_stable():
    tenant = Tenant("tenant")
    namespace = Namespace(tenant, "runtime")
    assert namespace.key == f"{tenant.id}:runtime"


def test_namespace_rejects_empty_name():
    with pytest.raises(ValueError):
        Namespace(Tenant("tenant"), " ")


def test_namespace_rejects_missing_tenant():
    with pytest.raises(ValueError):
        Namespace(None, "runtime")
