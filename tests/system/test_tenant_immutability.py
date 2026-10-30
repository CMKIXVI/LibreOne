from dataclasses import FrozenInstanceError

import pytest

from libreone.system.tenant import Tenant


def test_tenant_is_immutable():
    tenant = Tenant("acme")
    with pytest.raises(FrozenInstanceError):
        tenant.name = "other"
