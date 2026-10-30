import pytest

from libreone.system.tenant import Tenant


def test_tenant_name_is_preserved():
    tenant = Tenant("tenant")
    assert tenant.name == "tenant"
    assert tenant.id is not None


def test_tenant_rejects_empty_name():
    with pytest.raises(ValueError):
        Tenant("")
    with pytest.raises(ValueError):
        Tenant("   ")


def test_tenant_is_immutable():
    tenant = Tenant("tenant")
    with pytest.raises(Exception):
        tenant.name = "other"
