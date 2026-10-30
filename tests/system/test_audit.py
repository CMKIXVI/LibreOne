from libreone.system.audit import AuditRecord


def test_audit_records_have_identity():
    record = AuditRecord("boot", "system")
    assert record.action == "boot"
    assert record.actor == "system"
    assert record.id is not None
    assert record.timestamp is not None
