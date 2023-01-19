from typing import Dict, List

import logging
import ast
import async_client

from jupyter_client import BlockingKernelClient, AsyncKernelClient
from enterprise_gateway.client.gateway_client import GatewayClient, KernelClient

DEFAULT_USERNAME = "jovyan"
BASE_GATEWAY_URL = "localhost:8888/modeler/sandbox/6535"
BASE_GATEWAY_HTTP_URL = f"http://{BASE_GATEWAY_URL}"
BASE_GATEWAY_WS_URL = f"ws://{BASE_GATEWAY_URL}"
# BASE_GATEWAY_HTTP_URL = f"http://localhost:18888"
# BASE_GATEWAY_WS_URL = f"ws://localhost:18877"
REQUEST_TIMEOUT = 120
DEFAULT_KERNELSPEC_NAME =  "python3" # "python_kubernetes"

COOKIE_HEADER = {
    "cookie": '_xsrf=2|ea3d1a3a|dc4211e14f314b65b50b04c33b24b2fc|1674026474; username-aiip-dev-skcc-com="2|1:0|10:1674026480|26:username-aiip-dev-skcc-com|44:YjFiZmZmMTMzNTZiNDA5ZjllZWZjMmVhNzJlZmNlYzM=|cb13e6c0ca230de13353391402fe241136740d9055e8275f8e84b3e7cdec11b3"; groupId=7; csrftoken=LbsgAC3im3KAXpvKIYKWWzuPIZrANgdWlY8CMt51HR6lkTEumI4Ikw0lZpL8FGMV'
}


# resp = await async_client.get(f"{BASE_GATEWAY_HTTP_URL}/api/kernels")
# kernels_opened: List[Dict] = resp.json()
# kernel_info: Dict = kernels_opened[0]
# kernel_id: str = kernel_info["id"]

# # client = BlockingKernelClient()
# # client.kernel_info()


# # ws_req = HTTPRequest(url='{}/api/kernels/{}/channels'.format(
# #         base_ws_url,
# #         url_escape(kernel_id)
# #     ),
# #     auth_username='jovyan',
# #     # auth_password='fakepass'
# # )
# # ws = await websocket_connect(ws_req)

# gw_client = GatewayClient(host=BASE_GATEWAY_URL)
# gw_client.DEFAULT_USERNAME = "jovyan"

# kernel_client: KernelClient = gw_client.start_kernel(
#     kernelspec_name="python_kubernetes",
#     username=DEFAULT_USERNAME,
#     timeout=REQUEST_TIMEOUT,
# )

# gw_client.shutdown_kernel(
# )


# kernel_client = KernelClient(
#     http_api_endpoint=BASE_GATEWAY_HTTP_URL,
#     ws_api_endpoint=BASE_GATEWAY_WS_URL,
#     kernel_id=kernel_id,
#     timeout=REQUEST_TIMEOUT,
#     logger=logging.getLogger("KernelClient"),
# )
code_str = """
import numpy as np
import logging

log = logging.getLogger("Code Execution")

print(np.__version__)

log.info('log test')
"""

# kernel_client.execute(code_str)

# resp = await async_client.get(
#     f"{BASE_GATEWAY_HTTP_URL}/api/kernels",
# )

kernel_id = "40313999-9ba9-4101-ad7f-dc1e91630595"
from jupyter_client.kernelspec import KernelSpecManager, NoSuchKernel
from jupyter_client.manager import (
    KernelManager, 
    AsyncKernelManager,
    start_new_async_kernel,
    start_new_kernel,
)
from jupyter_client.blocking.client import BlockingKernelClient

from enterprise_gateway.client.gateway_client import GatewayClient, KernelClient


aa = KernelSpecManager()
aa.get_all_specs()
DEFAULT_KERNELSPEC_NAME = "python3"
TIMEOUT = 60
kernel = aa.get_kernel_spec(DEFAULT_KERNELSPEC_NAME)

kernel_manager: AsyncKernelManager
kernel_client: AsyncKernelClient
kernel_manager, kernel_client = await start_new_async_kernel(kernel_name=DEFAULT_KERNELSPEC_NAME)


await kernel_client.is_alive()



kernel_client: BlockingKernelClient
kernel_manager, kernel_client = start_new_kernel(kernel_name=DEFAULT_KERNELSPEC_NAME)
result = kernel_client.execute_interactive(
    code=code_str, 
    timeout=TIMEOUT,
)



CF_PATH = "/home/notebook/.local/share/jupyter/runtime/kernel-4ba86b42-039f-4381-a3c9-291c841bfbbf.json"
kernel_manager.connection_file = CF_PATH
kernel_client = kernel_manager.blocking_client()

kernel_client = KernelClient()
kernel_client.load_connection_file(CF_PATH)

import requests

session = requests.Session()
url = f"{BASE_GATEWAY_HTTP_URL}/login"
resp = session.get(url)
xsrf_cookie = resp.cookies["_xsrf"]



kernel_client = KernelClient(
    http_api_endpoint=f"{BASE_GATEWAY_HTTP_URL}/api/kernels",
    ws_api_endpoint=f"{BASE_GATEWAY_WS_URL}/api/kernels",
    kernel_id=kernel_id,
    timeout=REQUEST_TIMEOUT,
    logger=logging.getLogger("KernelClient"),
)

resp = await async_client.get(
    f"{BASE_GATEWAY_HTTP_URL}/api/kernels",
    headers=COOKIE_HEADER,
)


## Interrupt test


async def execute(code: str, kernel_client: KernelClient):
    return kernel_client.execute(code)


kernel_client = AsyncKernelClient(connection_file=CF_PATH)
kernel_client.load_connection_file()
kernel_client.start_channels()

code_str = """
import numpy as np
import logging
import time

log = logging.getLogger("Code Execution")

print(np.__version__)

time.sleep(10)

log.info('log test')
"""
res = await execute(code=code_str, kernel_client=kernel_client)
res

def interrupt(kernel_client: KernelClient):
    return kernel_client.interrupt()

interrupt_msg = ast.literal_eval(f"b'''{res}'''").decode()
print(interrupt_msg)
