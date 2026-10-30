from libreone.system.config import SystemConfig


def verify_config_contract() -> bool:
    config = SystemConfig()
    return config.environment == "production" and config.data_dir == ".libreone"
