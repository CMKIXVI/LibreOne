from libreone.system.network import Endpoint


def verify_network_contract() -> bool:
    endpoint = Endpoint("localhost", 8080)
    return endpoint.port == 8080
