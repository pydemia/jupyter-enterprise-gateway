from ..python.client import GatewayClient, KernelClient, decode_cellmsg
import logging

logging.basicConfig(level="INFO")

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

    kernel_client: KernelClient = gw_client.get_client()

    # kernel_client: KernelSessionClient = gw_client.start_kernel(
    #     kernelspec_name=DEFAULT_KERNELSPEC_NAME,
    #     username=DEFAULT_USERNAME,
    #     timeout=REQUEST_TIMEOUT,
    # )

    code0 = """
import numpy as np
import logging
import time

log = logging.getLogger("Code Execution")

print(np.__version__)

time.sleep(10)

log.info('log test')
a = 5
"""
    code1 = """
a / 2
"""
    code2 = """
a / 0
"""

    code3 = """
b = a
b
"""


    result0 = kernel_client.execute(code0)
    result1 = kernel_client.execute(code1)
    result2 = kernel_client.execute(code2)
    result3 = kernel_client.execute(code3)

    msg0 = decode_cellmsg(result0)
    msg1 = decode_cellmsg(result1)
    msg2 = decode_cellmsg(result2)
    msg3 = decode_cellmsg(result3)

    print(msg0)
    print(msg1)
    print(msg2)
    print(msg3)
    kernel_client.restart()
    # async def execute(code: str, kernel_client: KernelClient):
    #     return kernel_client.execute(code)

    assert True