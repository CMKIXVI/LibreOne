import pytest

from libreone.system.namespaces import Namespace
from libreone.system.tenant import Tenant


def test_namespace_rejects_empty_name():
    with pytest.raises(ValueError):
        Namespace(Tenant("a"), "")
