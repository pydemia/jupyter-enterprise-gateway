from ..python.client import GatewayClient, KernelClient

def test_custom_client():
    
    DEFAULT_USERNAME = "pydemia"
    BASE_GATEWAY_URL = "localhost:8989"
    BASE_GATEWAY_HTTP_URL = f"http://{BASE_GATEWAY_URL}"
    BASE_GATEWAY_WS_URL = f"ws://{BASE_GATEWAY_URL}"
    # BASE_GATEWAY_HTTP_URL = f"http://localhost:18888"
    # BASE_GATEWAY_WS_URL = f"ws://localhost:18877"
    REQUEST_TIMEOUT = TIMEOUT = 120
    DEFAULT_KERNELSPEC_NAME = "enterprise-gw-py38"

    assert True