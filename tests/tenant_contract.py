from libreone.system.tenant import Tenant


def verify_tenant_contract() -> bool:
    tenant = Tenant("default")
    return tenant.name == "default"
