from libreone.system.audit import AuditRecord


def test_audit_metadata_defaults_to_mapping():
    first = AuditRecord("x", "a")
    second = AuditRecord("x", "a")
    assert first.metadata == {}
    assert second.metadata == {}
    assert first.metadata is not second.metadata
