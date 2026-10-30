from libreone.system.resources import ResourceLimits


def verify_resource_contract() -> bool:
    limits = ResourceLimits(cpu_seconds=1, memory_bytes=1024, disk_bytes=2048, wall_seconds=3)
    limits.validate()
    return limits.memory_bytes == 1024
