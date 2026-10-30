from dataclasses import FrozenInstanceError

import pytest

from libreone.system.audit import AuditRecord


def test_audit_record_is_immutable():
    record = AuditRecord("boot", "system")
    with pytest.raises(FrozenInstanceError):
        record.action = "other"
