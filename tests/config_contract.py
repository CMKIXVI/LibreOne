from libreone.system.config import SystemConfig


def verify_config_contract() -> bool:
    config = SystemConfig()
    return config.environment in {"development", "production", "test"}
