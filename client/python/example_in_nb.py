from typing import Dict, List, Union

import logging
import ast
import async_client

from jupyter_client import KernelClient, BlockingKernelClient, AsyncKernelClient
from enterprise_gateway.client.gateway_client import GatewayClient, KernelClient

import queue
from jupyter_client.manager import start_new_kernel
from pprint import PrettyPrinter


DEFAULT_USERNAME = "pydemia"
BASE_GATEWAY_URL = "localhost:8989"
BASE_GATEWAY_HTTP_URL = f"http://{BASE_GATEWAY_URL}"
BASE_GATEWAY_WS_URL = f"ws://{BASE_GATEWAY_URL}"
# BASE_GATEWAY_HTTP_URL = f"http://localhost:18888"
# BASE_GATEWAY_WS_URL = f"ws://localhost:18877"
REQUEST_TIMEOUT = TIMEOUT = 120
DEFAULT_KERNELSPEC_NAME = "enterprise-gw-py38"

import requests

hostname = '127.0.0.1'
port = '8888'
password = 'zxc'

h = {}
if password:
    with requests.Session() as sess:
        LOGIN_URL = f"{BASE_GATEWAY_HTTP_URL}/login"
        r = sess.get(LOGIN_URL)
        xsrf_cookie = r.cookies["_xsrf"]
        params = {
            "_xsrf": xsrf_cookie,
            "password": password,
        }
        sess.post(LOGIN_URL, data=params)
    # sessions = requests.get(
    #     f"{BASE_GATEWAY_HTTP_URL}/api/sessions",
    #     headers=h
    # ).json()

# resp = await async_client.get(f"{BASE_GATEWAY_HTTP_URL}/login")


# resp = await async_client.get(f"{BASE_GATEWAY_HTTP_URL}/api/kernels")
resp = sess.get(f"{BASE_GATEWAY_HTTP_URL}/api/kernels")
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
import os
import logging
import requests
import time
from uuid import uuid4
from tornado.escape import json_encode, json_decode, utf8
from threading import Thread
import websocket
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 120))
log_level = os.getenv("LOG_LEVEL", "INFO")

class GatewayClient(object):
    """
    *** E X P E R I M E N T A L *** *** E X P E R I M E N T A L ***

    An experimental Gateway Client that is used for Enterprise Gateway
    integration tests and can be leveraged for micro service type of
    connections.
    """
    DEFAULT_USERNAME = os.getenv('KERNEL_USERNAME', 'bob')
    DEFAULT_GATEWAY_HOST = os.getenv('GATEWAY_HOST', 'localhost:8888')
    KERNEL_LAUNCH_TIMEOUT = os.getenv('KERNEL_LAUNCH_TIMEOUT', '40')

    def __init__(self, host=DEFAULT_GATEWAY_HOST, password=None):
        self.http_api_endpoint = 'http://{}/api/kernels'.format(host)
        self.ws_api_endpoint = 'ws://{}/api/kernels'.format(host)
        self.log = logging.getLogger('GatewayClient')
        self.log.setLevel(log_level)
        if password:
            self.session = requests.Session()
            LOGIN_URL = f"{BASE_GATEWAY_HTTP_URL}/login"
            r = self.session.get(LOGIN_URL)
            self.xsrf_cookie = r.cookies["_xsrf"]
            params = {
                "_xsrf": self.xsrf_cookie,
                "password": password,
            }
            self.session.post(LOGIN_URL, data=params)
        else:
            self.session = requests

    # def _get_xsrf_token(self, password: str) -> Union[requests.Session, requests]:
    #     if password:
    #         self.session = requests.Session()
    #         LOGIN_URL = f"{BASE_GATEWAY_HTTP_URL}/login"
    #         r = self.session.get(LOGIN_URL)
    #         self.xsrf_cookie = r.cookies["_xsrf"]
    #         params = {
    #             "_xsrf": self.xsrf_cookie,
    #             "password": password,
    #         }
    #         self.session.post(LOGIN_URL, data=params)
    #     else:
    #         self.session = requests

    def _add_xsrf_cookie(self, json_data: Dict) -> Dict:
        if self.xsrf_cookie:
            json_data.update({"_xsrf": self.xsrf_cookie})
        return json_data

    def start_kernel(self, kernelspec_name, username=DEFAULT_USERNAME, timeout=REQUEST_TIMEOUT):
        self.log.info('Starting a {} kernel ....'.format(kernelspec_name))

        json_data = {'name': kernelspec_name,
                     'env': {'KERNEL_USERNAME': username,
                             'KERNEL_LAUNCH_TIMEOUT': GatewayClient.KERNEL_LAUNCH_TIMEOUT}}
        
        json_data = self._add_xsrf_cookie(json_data)

        response = self.session.post(self.http_api_endpoint, data=json_encode(json_data))
        if response.status_code == 201:
            json_data = response.json()
            kernel_id = json_data.get("id")
            self.log.info('Started kernel with id {}'.format(kernel_id))
        else:
            raise RuntimeError('Error starting kernel : {} response code \n {}'.
                               format(response.status_code, response.content))

        return KernelClient(self.http_api_endpoint, self.ws_api_endpoint, kernel_id, timeout=timeout, logger=self.log)

    def shutdown_kernel(self, kernel):
        self.log.info("Shutting down kernel : {} ....".format(kernel.kernel_id))

        if not kernel:
            return False

        kernel.shutdown()

        url = "{}/{}".format(self.http_api_endpoint, kernel.kernel_id)
        response = self.session.delete(url)
        if response.status_code == 204:
            self.log.debug('Kernel {} shutdown'.format(kernel.kernel_id))
            self.session.close()
            return True
        else:
            raise RuntimeError('Error shutting down kernel {}: {}'.format(kernel.kernel_id, response.content))



gw_client = GatewayClient(host=BASE_GATEWAY_URL, password="zxc")
gw_client.DEFAULT_USERNAME = DEFAULT_USERNAME

kernel_client: KernelClient = gw_client.start_kernel(
    kernelspec_name=DEFAULT_KERNELSPEC_NAME,
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
