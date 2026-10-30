import pytest

from libreone.system.audit import AuditRecord


def test_audit_requires_actor():
    with pytest.raises((TypeError, ValueError)):
        AuditRecord("boot", "")
