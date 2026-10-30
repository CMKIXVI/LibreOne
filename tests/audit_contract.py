from libreone.system.audit import AuditRecord


def verify_audit_contract() -> bool:
    record = AuditRecord("boot", "system")
    return record.action == "boot" and record.actor == "system"
