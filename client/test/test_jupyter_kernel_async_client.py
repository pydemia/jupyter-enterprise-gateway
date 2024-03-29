from ..python.jupyter_kernel_async_client import GatewayClient, KernelClient
from ..python.utils import decode_cellmsg
import logging
import pytest
import datetime as dt

logging.basicConfig(level="INFO")

log = logging.getLogger("TEST Jupyter Client")


@pytest.mark.asyncio
async def test_custom_client():

    DEFAULT_USERNAME = "jovyan"
    REQUEST_TIMEOUT = TIMEOUT = 120
    DEFAULT_KERNELSPEC_NAME = "python3"

    BASE_GATEWAY_URL = "http://localhost:8888"
    PASSWORD = "zxc"

    start_dt = dt.datetime.now()
    gw_client = GatewayClient(host=BASE_GATEWAY_URL, password=PASSWORD)
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


    import asyncio
    from asyncio import Future
    from functools import partial
    # def print_wall_time(start_dt: dt.timedelta, _: Future[None]) -> None:
    def print_wall_time(start_dt: dt.timedelta, _) -> None:
        print(f'Job duration: {dt.datetime.now() - start_dt}')
    
    # loop = asyncio.get_event_loop()
    # result0 = loop.run_until_complete(asyncio.gather())

    # start_dt = dt.datetime.now()

    # async with asyncio.get_running_loop() as loop:
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    future = asyncio.create_task(kernel_client.execute_async(code0))
    future.add_done_callback(partial(print_wall_time, start_dt))
    
    result0 = loop.run_until_complete(asyncio.gather())
    loop.close()


    # loop = asyncio.get_event_loop()
    # result0 = loop.run_until_complete(asyncio.gather())


    # result0 = await kernel_client.execute_async(code0)

    # asyncio.run(kernel_client.execute_async(code0))
    # result1 = await kernel_client.execute_async(code1)
    result2, elapsed2 = kernel_client.execute_sync(code2)
    result3, elapsed3 = kernel_client.execute(code3)
    result4, elapsed4 = kernel_client.execute(code4)

    msg0 = decode_cellmsg(result0)
    # msg1 = decode_cellmsg(result1)
    msg2 = decode_cellmsg(result2)
    msg3 = decode_cellmsg(result3)
    msg4 = decode_cellmsg(result4)

    elapsed_tmp = "00:00:00.00000"
    # print(msg0, f"MSG0: elapsed: {elapsed0}", sep="\n")
    # print(msg1, f"MSG1: elapsed: {elapsed1}", sep="\n")
    print(msg0, f"MSG0: elapsed: {elapsed_tmp}", sep="\n")
    # print(msg1, f"MSG1: elapsed: {elapsed_tmp}", sep="\n")
    print(msg2, f"MSG2: elapsed: {elapsed2}", sep="\n")
    print(msg3, f"MSG3: elapsed: {elapsed3}", sep="\n")
    print(msg4, f"MSG3: elapsed: {elapsed4}", sep="\n")
    # kernel_client.restart()
    kernel_client.interrupt()
    kernel_client.shutdown()
    kernel_client.restart()
    kernel_client.shutdown()
    print(kernel_client.get_state())

    gw_client.shutdown_client(kernel_client)

    # async def execute(code: str, kernel_client: KernelClient):
    #     return kernel_client.execute(code)

    assert True