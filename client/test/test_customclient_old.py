from ..python.client import GatewayClient, KernelClient

def test_custom_client():
    
    DEFAULT_USERNAME = "jovyan"
    BASE_GATEWAY_URL = "localhost:8888"
    BASE_GATEWAY_HTTP_URL = f"http://{BASE_GATEWAY_URL}"
    BASE_GATEWAY_WS_URL = f"ws://{BASE_GATEWAY_URL}"
    # BASE_GATEWAY_HTTP_URL = f"http://localhost:18888"
    # BASE_GATEWAY_WS_URL = f"ws://localhost:18877"
    REQUEST_TIMEOUT = TIMEOUT = 120
    DEFAULT_KERNELSPEC_NAME = "python3"


    gw_client = GatewayClient(host=BASE_GATEWAY_URL, password="zxc")
    gw_client.DEFAULT_USERNAME = DEFAULT_USERNAME

    kernel_client: KernelClient = gw_client.start_kernel(
        kernelspec_name=DEFAULT_KERNELSPEC_NAME,
        username=DEFAULT_USERNAME,
        timeout=REQUEST_TIMEOUT,
    )

    
    code = """
import numpy as np
import logging
import time

log = logging.getLogger("Code Execution")

print(np.__version__)

time.sleep(10)

log.info('log test')"""

    kernel_client.restart()
    result = kernel_client.execute(code)
    # async def execute(code: str, kernel_client: KernelClient):
    #     return kernel_client.execute(code)

    assert True