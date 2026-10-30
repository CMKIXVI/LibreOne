from dataclasses import FrozenInstanceError

import pytest

from libreone.system.namespaces import Namespace
from libreone.system.tenant import Tenant


def test_namespace_is_immutable():
    namespace = Namespace(Tenant("acme"), "default")
    with pytest.raises(FrozenInstanceError):
        namespace.name = "other"
