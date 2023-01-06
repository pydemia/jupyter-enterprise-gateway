from typing import Dict, List

import logging
import ast
import async_client

from jupyter_client import KernelClient, BlockingKernelClient, AsyncKernelClient
from enterprise_gateway.client.gateway_client import GatewayClient, KernelClient

DEFAULT_USERNAME = "jovyan"
BASE_GATEWAY_URL = "localhost:18888"
BASE_GATEWAY_HTTP_URL = f"http://{BASE_GATEWAY_URL}"
BASE_GATEWAY_WS_URL = f"ws://{BASE_GATEWAY_URL}"
# BASE_GATEWAY_HTTP_URL = f"http://localhost:18888"
# BASE_GATEWAY_WS_URL = f"ws://localhost:18877"
REQUEST_TIMEOUT = 120
DEFAULT_KERNELSPEC_NAME = "python_kubernetes"


resp = await async_client.get(f"{BASE_GATEWAY_HTTP_URL}/api/kernels")
kernels_opened: List[Dict] = resp.json()
kernel_info: Dict = kernels_opened[0]
kernel_id: str = kernel_info["id"]

# client = BlockingKernelClient()
# client.kernel_info()


# ws_req = HTTPRequest(url='{}/api/kernels/{}/channels'.format(
#         base_ws_url,
#         url_escape(kernel_id)
#     ),
#     auth_username='jovyan',
#     # auth_password='fakepass'
# )
# ws = await websocket_connect(ws_req)

gw_client = GatewayClient(host=BASE_GATEWAY_URL)
gw_client.DEFAULT_USERNAME = "jovyan"

kernel_client: KernelClient = gw_client.start_kernel(
    kernelspec_name="python_kubernetes",
    username=DEFAULT_USERNAME,
    timeout=REQUEST_TIMEOUT,
)

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

kernel_client.execute(code_str)

resp = await async_client.get(
    f"{BASE_GATEWAY_HTTP_URL}/api/kernels",
)


kernel_client = KernelClient(
    http_api_endpoint=f"{BASE_GATEWAY_HTTP_URL}/api/kernels",
    ws_api_endpoint=f"{BASE_GATEWAY_WS_URL}/api/kernels",
    kernel_id=kernel_id,
    timeout=REQUEST_TIMEOUT,
    logger=logging.getLogger("KernelClient"),
)

## Interrupt test


async def execute(code: str, kernel_client: KernelClient):
    return kernel_client.execute(code)


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
