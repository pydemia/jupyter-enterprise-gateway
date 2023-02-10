# from ..python.jupyter_kernel_blocking_client import GatewayClient, KernelClient, decode_cellmsg
from typing import Dict, List
import logging
import datetime as dt
import ast
# import async_client

from enterprise_gateway.client.gateway_client import GatewayClient, KernelClient
from tornado.escape import json_encode

from ..python import blocking_client
from ..python.utils import decode_cellmsg


logging.basicConfig(level="INFO")

log = logging.getLogger("TEST Jupyter Client")

def test_custom_client():

    DEFAULT_USERNAME = "jovyan"
    REQUEST_TIMEOUT = TIMEOUT = 120
    DEFAULT_KERNELSPEC_NAME = "python_kubernetes"

    BASE_GATEWAY_URL = "localhost:18888"
    # PASSWORD = "zxc"

    BASE_GATEWAY_HTTP_URL = f"http://{BASE_GATEWAY_URL}"
    BASE_GATEWAY_WS_URL = f"ws://{BASE_GATEWAY_URL}"
    # BASE_GATEWAY_HTTP_URL = f"http://localhost:18888"
    # BASE_GATEWAY_WS_URL = f"ws://localhost:18877"


    # blocking_client.get(f"{BASE_GATEWAY_HTTP_URL}/api/kernels/c82b1535-2d3d-4e57-a584-570f70ff8859")
    resp = blocking_client.get(f"{BASE_GATEWAY_HTTP_URL}/api/kernels")
    kernels_opened: List[Dict] = resp.json()
    try:
        kernel_info: Dict = kernels_opened[0]
        kernel_id: str = kernel_info["id"]
    except IndexError:
        resp = blocking_client.post(
            f"{BASE_GATEWAY_HTTP_URL}/api/kernels",
            # params={"namespace": "another"},
            data=json_encode({
                "name": DEFAULT_KERNELSPEC_NAME,
                "path": "",
                "env": {
                    "KERNEL_NAMESPACE": "default",
                    "KERNEL_SERVICE_ACCOUNT_NAME": "default",
                },
                # "env": ["NEE"],
            })
        )
        kernels_opened: List[Dict] = resp.json()
        kernel_info: Dict = kernels_opened[0]
        kernel_id: str = kernel_info["id"]

    
    gw_client = GatewayClient(host=BASE_GATEWAY_URL)
    gw_client.DEFAULT_USERNAME = "jovyan"

    kernel_client: KernelClient = gw_client.start_kernel(
        kernelspec_name=DEFAULT_KERNELSPEC_NAME,
        username=DEFAULT_USERNAME,
        timeout=REQUEST_TIMEOUT,
    )
    # start_dt = dt.datetime.now()
    # gw_client = GatewayClient(host=BASE_GATEWAY_URL, password=PASSWORD)
    # print(f"GateWayClient: elapsed: {dt.datetime.now() - start_dt}", sep="\n")
    # gw_client.DEFAULT_USERNAME = DEFAULT_USERNAME

    # start_dt = dt.datetime.now()
    # # kernel_client: KernelSessionClient = gw_client.start_kernel(
    # #     kernelspec_name=DEFAULT_KERNELSPEC_NAME,
    # #     username=DEFAULT_USERNAME,
    # #     timeout=REQUEST_TIMEOUT,
    # # )
    # kernel_client: KernelClient = gw_client.get_client()
    # print(f"KernelClient: elapsed: {dt.datetime.now() - start_dt}", sep="\n")

    code0 = """
print("test")    
"""
    code1 = """
import numpy as np
import logging
import time

log = logging.getLogger("Code Execution")

print(np.__version__)

time.sleep(10)

log.info('log test')
a = 5
"""
    code2 = """
a / 2
"""
    code3 = """
a / 0
"""

    code4 = """
b = a
b
"""


    # result0, elapsed0 = kernel_client.execute(code0)
    # result1, elapsed1 = kernel_client.execute(code1)
    # result2, elapsed2 = kernel_client.execute(code2)
    # result3, elapsed3 = kernel_client.execute(code3)
    # result4, elapsed4 = kernel_client.execute(code4)
    result0 = kernel_client.execute(code0, timeout=REQUEST_TIMEOUT)
    result1 = kernel_client.execute(code1, timeout=REQUEST_TIMEOUT)
    result2 = kernel_client.execute(code2, timeout=REQUEST_TIMEOUT)
    result3 = kernel_client.execute(code3, timeout=REQUEST_TIMEOUT)
    result4 = kernel_client.execute(code4, timeout=REQUEST_TIMEOUT)

    msg0 = decode_cellmsg(result0)
    msg1 = decode_cellmsg(result1)
    msg2 = decode_cellmsg(result2)
    msg3 = decode_cellmsg(result3)
    msg4 = decode_cellmsg(result4)

    # print(msg0, f"MSG0: elapsed: {elapsed0}", sep="\n")
    # print(msg1, f"MSG1: elapsed: {elapsed1}", sep="\n")
    # print(msg2, f"MSG2: elapsed: {elapsed2}", sep="\n")
    # print(msg3, f"MSG3: elapsed: {elapsed3}", sep="\n")
    # print(msg4, f"MSG3: elapsed: {elapsed4}", sep="\n")
    print(msg0, f"MSG0:", sep="\n")
    print(msg1, f"MSG1:", sep="\n")
    print(msg2, f"MSG2:", sep="\n")
    print(msg3, f"MSG3:", sep="\n")
    print(msg4, f"MSG3:", sep="\n")
    # kernel_client.restart()
    kernel_client.interrupt()
    print(kernel_client.get_state())
    kernel_client.shutdown()
    try:
        kernel_client.restart()
        kernel_client.shutdown()
    except AttributeError:
        pass
    print(kernel_client.get_state())

    # gw_client.shutdown_client(kernel_client)

    # async def execute(code: str, kernel_client: KernelClient):
    #     return kernel_client.execute(code)

    assert True