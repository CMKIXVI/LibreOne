from libreone.system.memory import MemoryRegion


def verify_memory_contract() -> bool:
    region = MemoryRegion(100, 50)
    return region.end == 150 and region.contains(120) and not region.contains(150)
