from libreone.system.tenant import Tenant


def test_tenants_have_unique_ids():
    assert Tenant("a").id != Tenant("b").id
