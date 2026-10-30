from libreone.system.audit import AuditRecord


def test_audit_record_has_unique_id():
    first = AuditRecord("boot", "system")
    second = AuditRecord("boot", "system")
    assert first.id != second.id
