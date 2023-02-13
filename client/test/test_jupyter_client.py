from ..python.jupyter_kernel_client import GatewayClient, KernelClient
from ..python.utils import decode_cellmsg
import logging
import pytest
import datetime as dt

logging.basicConfig(level="INFO")

log = logging.getLogger("TEST Jupyter Client")

DEFAULT_USERNAME = "jovyan"
REQUEST_TIMEOUT = TIMEOUT = 120
DEFAULT_KERNELSPEC_NAME = "python_kubernetes"  # "python3"

BASE_GATEWAY_URL = "http://localhost:18888"
PASSWORD = "zxc"

def test_blocking_client():

    start_dt = dt.datetime.now()
    gw_client = GatewayClient(
        host=BASE_GATEWAY_URL,
        type="gw",
        password=PASSWORD,
    )
    print(f"GateWayClient: elapsed: {dt.datetime.now() - start_dt}", sep="\n")
    gw_client.DEFAULT_USERNAME = DEFAULT_USERNAME

    start_dt = dt.datetime.now()
    # kernel_client: KernelSessionClient = gw_client.start_kernel(
    #     kernelspec_name=DEFAULT_KERNELSPEC_NAME,
    #     username=DEFAULT_USERNAME,
    #     timeout=REQUEST_TIMEOUT,
    # )
    kernel_client: KernelClient = gw_client.get_client()
    print(f"KernelClient: elapsed: {dt.datetime.now() - start_dt}", sep="\n")

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


    result0, elapsed0 = kernel_client.execute(code0)
    result1, elapsed1 = kernel_client.execute(code1)
    result2, elapsed2 = kernel_client.execute(code2)
    result3, elapsed3 = kernel_client.execute(code3)
    result4, elapsed4 = kernel_client.execute(code4)

    msg0 = decode_cellmsg(result0)
    msg1 = decode_cellmsg(result1)
    msg2 = decode_cellmsg(result2)
    msg3 = decode_cellmsg(result3)
    msg4 = decode_cellmsg(result4)

    print(msg0, f"MSG0: elapsed: {elapsed0}", sep="\n")
    print(msg1, f"MSG1: elapsed: {elapsed1}", sep="\n")
    print(msg2, f"MSG2: elapsed: {elapsed2}", sep="\n")
    print(msg3, f"MSG3: elapsed: {elapsed3}", sep="\n")
    print(msg4, f"MSG3: elapsed: {elapsed4}", sep="\n")

    # kernel_client.restart()
    kernel_client.interrupt()
    print(kernel_client.get_state())
    kernel_client.shutdown()
    try:
        kernel_client.restart()
        kernel_client.shutdown()
    except AttributeError:
        pass

    gw_client.shutdown_client(kernel_client)

    # async def execute(code: str, kernel_client: KernelClient):
    #     return kernel_client.execute(code)

    assert True

@pytest.mark.asyncio
async def test_async_client():

    start_dt = dt.datetime.now()
    gw_client = GatewayClient(
        host=BASE_GATEWAY_URL,
        type="gw",
        password=PASSWORD,
    )
    print(f"GateWayClient: elapsed: {dt.datetime.now() - start_dt}", sep="\n")
    gw_client.DEFAULT_USERNAME = DEFAULT_USERNAME

    start_dt = dt.datetime.now()
    # kernel_client: KernelSessionClient = gw_client.start_kernel(
    #     kernelspec_name=DEFAULT_KERNELSPEC_NAME,
    #     username=DEFAULT_USERNAME,
    #     timeout=REQUEST_TIMEOUT,
    # )
    kernel_client: KernelClient = gw_client.get_client()
    print(f"KernelClient: elapsed: {dt.datetime.now() - start_dt}", sep="\n")

    code5 = """
import time
for _ in range(5):
    print(_)
    time.sleep(3)
"""
    # result5, elapsed5 = kernel_client.execute(code5)
    # msg5 = decode_cellmsg(result5)
    # print(msg5, f"MSG0: elapsed: {elapsed5}", sep="\n")

    import asyncio

    # msg_resp, elapsed_time = yield from kernel_client.execute_async(code5)
    # loop = asyncio.get_event_loop()
    import websocket

    # loop = asyncio.get_event_loop()
    # task = loop.create_task(kernel_client.execute_async(code5))
    # async for msg_resp, elapsed_time in task:
    #     print(msg_resp, f"MSG3: elapsed: {elapsed_time}", sep="\n")

    # msg_resp, elapsed_time = await asyncio.gather(kernel_client.execute_async(code5))
    # print(msg_resp, f"MSG3: elapsed: {elapsed_time}", sep="\n")

    finished = False
    while not finished:
        try:
            msg_resp, elapsed_time = await kernel_client.execute_async(code5)
            print(msg_resp, f"MSG3: elapsed: {elapsed_time}", sep="\n")
        except websocket.WebSocketConnectionClosedException:
            print(msg_resp, f"MSG3: elapsed: {elapsed_time}", sep="\n")
            finished = True
        
        # try:
        #     msg_resp, elapsed_time = await kernel_client.execute_async(code5)
        #     print(msg_resp, f"MSG3: elapsed: {elapsed_time}", sep="\n")

    # msg_resp, elapsed_time = await kernel_client.execute_async(code5)
    # print(msg_resp, f"MSG3: elapsed: {elapsed_time}", sep="\n")

    # try:
    #     msg_resp, elapsed_time = await asyncio.wait_for(kernel_client.execute_async(code5), timeout=100)
    # except asyncio.TimeoutError:
    #     print("Timeout")
    
    # msg_resp, elapsed_time = loop.run_until_complete(
    #     asyncio.gather(
    #         kernel_client.execute_async(code5)
    #     )
    # )
    # async for msg_resp, elapsed_time in kernel_client.execute_async(code5):
    #     try:
    #         msg5 = decode_cellmsg(msg_resp)
    #         print(msg5, f"MSG0: elapsed: {elapsed_time}", sep="\n")
            
    
    # kernel_client.restart()
    kernel_client.interrupt()
    print(kernel_client.get_state())
    kernel_client.shutdown()
    try:
        kernel_client.restart()
        kernel_client.shutdown()
    except AttributeError:
        pass

    gw_client.shutdown_client(kernel_client)

    # async def execute(code: str, kernel_client: KernelClient):
    #     return kernel_client.execute(code)

    assert True