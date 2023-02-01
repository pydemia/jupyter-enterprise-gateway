from typing import Dict, Union, Optional, List, Tuple

from autologging import logged
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

import queue
import uuid
import httpx
from pathlib import PosixPath, Path


from . import async_client, blocking_client

DEFAULT_UUID = "f1e163d1-463c-414b-b4d4-3e51fe427e5f"



import websockets
from websockets.uri import WebSocketURI
from websockets.extensions import ClientExtensionFactory
from websockets.client import ClientConnection
from websockets import connect
from websockets.utils import generate_key

from jupyter_client import BlockingKernelClient, AsyncKernelClient

import ast

def decode_cellmsg(res: str):
    interruptable_msg = ast.literal_eval(f"b'''{res}'''").decode()
    return interruptable_msg


@logged
class KernelClient(object):

    DEAD_MSG_ID = 'deadbeefdeadbeefdeadbeefdeadbeef'
    POST_IDLE_TIMEOUT = 0.5
    DEFAULT_INTERRUPT_WAIT = 1

    def __init__(
            self,
            http_api_endpoint,
            ws_api_endpoint,
            kernel_id: str,
            session_id: str,
            timeout=REQUEST_TIMEOUT,
            logger=None,
            cookies: Dict = None,
            headers: Union[httpx.Headers, Dict] = None,
            params: str = None,
            # session_info: Dict = None
            ):
        self.shutting_down = False
        self.restarting = False
        self.http_api_endpoint = http_api_endpoint
        self.kernel_http_api_endpoint = '{}/{}'.format(http_api_endpoint, kernel_id)
        self.ws_api_endpoint = ws_api_endpoint
        self.kernel_ws_api_endpoint = '{}/{}/channels'.format(ws_api_endpoint, kernel_id)
        self.kernel_id = kernel_id
        self.session_id = session_id
        self.cookies = cookies
        self.headers = headers
        self.params = params
        self.timeout = timeout
        self.log = logging.getLogger('GatewayClient')
        self.log.setLevel(log_level)
        self.log.debug('Initializing kernel client ({}) to {}'.format(kernel_id, self.kernel_ws_api_endpoint))

        params_dict = {"session_id": self.session_id}
        params_str = "&".join([
            f"{k}={v}" for k, v in params_dict.items()
        ])

        self.http_client = httpx.Client()
        checked_session = self.http_client.get(
            f"http://localhost:8888/api/sessions/{session_id}",
            headers=headers,
            cookies=cookies,
        )
        # Session_Info Dict
        # id: uuid_str (session_id)
        # name: str (session_name)
        # path: str (filepath)
        # type: str (file, ...)
        # kernel:
        #   id: uuid_str
        #   name: str
        #   last_activity: datetime_str
        #   execution_state: str
        #   connections: int
        cookie_header_str = "; ".join([f"{k}={v}" for k, v in cookies.items()])
        session_info: Dict = checked_session.json()
        headers.update(
            {
                "Accept": "*/*",
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "X-XSRFToken": cookie_header_str,
                "Upgrade": "websocket",
                "Connection": "Upgrade",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-WebSocket-Key": generate_key(),
                "Sec-WebSocket-Version": "13",
                "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
            }
        )
        check_me = self.http_client.get(
            "http://localhost:8888/api/me",
            headers=headers,
            # cookies=cookies,
        )
        available_kernels = self.http_client.get(
            self.http_api_endpoint,
            params=params,
            cookies=cookies,
            headers=headers,
        )
        available_kernels = available_kernels.json()

        self.websocket_extra_headers = {
            "X-XSRFToken": cookies["_xsrf"],
            "Cookie": cookie_header_str,
        }

        try:
            self.kernel_socket = websocket.create_connection(
                f"ws://localhost:8888/api/kernels/{kernel_id}/channels?session_id={session_id}",
                timeout=self.timeout,  # timeout,
                enable_multithread=True,
                header=self.websocket_extra_headers,
            )

        except websocket.WebSocketBadStatusException as e:
            self.kernel_socket = None
            raise e

        self.response_queues = {}

        # startup reader thread
        self.response_reader = Thread(target=self._read_responses)
        self.response_reader.start()
        self.interrupt_thread = None


    def shutdown(self):
        # Terminate thread, close socket and clear queues.
        self.shutting_down = True

        if self.kernel_socket:
            self.kernel_socket.close()
            self.kernel_socket = None

        if self.response_queues:
            self.response_queues.clear()
            self.response_queues = None

        if self.response_reader:
            self.response_reader.join(timeout=2.0)
            if self.response_reader.is_alive():
                self.log.warning("Response reader thread is not terminated, continuing...")
            self.response_reader = None

    def execute(self, code, timeout=REQUEST_TIMEOUT):
        """
        Executes the code provided and returns the result of that execution.
        """
        response = []
        try:
            msg_id = self._send_request(code)

            post_idle = False
            while True:
                response_message = self._get_response(msg_id, timeout, post_idle)
                if response_message:
                    response_message_type = response_message['msg_type']

                    if response_message_type == 'error' or \
                            (response_message_type == 'execute_reply' and
                             response_message['content']['status'] == 'error'):
                        response.append('{}:{}:{}'.format(response_message['content']['ename'],
                                                          response_message['content']['evalue'],
                                                          response_message['content']['traceback']))
                    elif response_message_type == 'stream':
                        response.append(KernelClient._convert_raw_response(response_message['content']['text']))

                    elif response_message_type == 'execute_result' or response_message_type == 'display_data':
                        if 'text/plain' in response_message['content']['data']:
                            response.append(
                                KernelClient._convert_raw_response(response_message['content']['data']['text/plain']))
                        elif 'text/html' in response_message['content']['data']:
                            response.append(
                                KernelClient._convert_raw_response(response_message['content']['data']['text/html']))
                    elif response_message_type == 'status':
                        if response_message['content']['execution_state'] == 'idle':
                            post_idle = True  # indicate we're at the logical end and timeout poll for next message
                            continue
                    else:
                        self.log.debug("Unhandled response for msg_id: {} of msg_type: {}".
                                       format(msg_id, response_message_type))

                if response_message is None:  # We timed out.  If post idle, its ok, else make mention of it
                    if not post_idle:
                        self.log.warning("Unexpected timeout occurred for msg_id: {} - no 'idle' status received!".
                                         format(msg_id))
                    break

        except BaseException as b:
            self.log.debug(b)

        return ''.join(response)

    def interrupt(self):
        url = "{}/{}".format(self.kernel_http_api_endpoint, "interrupt")
        response = requests.post(url)
        if response.status_code == 204:
            self.log.debug('Kernel {} interrupted'.format(self.kernel_id))
            return True
        else:
            raise RuntimeError('Unexpected response interrupting kernel {}: {}'.
                               format(self.kernel_id, response.content))

    def restart(self, timeout=REQUEST_TIMEOUT):
        self.restarting = True
        self.kernel_socket.close()
        self.kernel_socket = None
        url = "{}/{}".format(self.kernel_http_api_endpoint, "restart")
        response = requests.post(url)
        if response.status_code == 200:
            self.log.debug('Kernel {} restarted'.format(self.kernel_id))
            self.kernel_socket = websocket.create_connection(
                self.kernel_ws_api_endpoint,
                # f"ws://localhost:8888/api/kernels/{kernel_id}/channels?session_id={session_id}",
                timeout=self.timeout,  # timeout,
                enable_multithread=True,
                header=self.websocket_extra_headers,
            )
            # self.kernel_socket = \
            #     websocket.create_connection(self.kernel_ws_api_endpoint, timeout=timeout, enable_multithread=True)
            self.restarting = False
            return True
        else:
            self.restarting = False
            raise RuntimeError('Unexpected response restarting kernel {}: {}'.format(self.kernel_id, response.content))

    def get_state(self):
        url = "{}".format(self.kernel_http_api_endpoint)
        response = requests.get(url)
        if response.status_code == 200:
            json = response.json()
            self.log.debug('Kernel {} state: {}'.format(self.kernel_id, json))
            return json['execution_state']
        else:
            raise RuntimeError('Unexpected response retrieving state for kernel {}: {}'.
                               format(self.kernel_id, response.content))

    def start_interrupt_thread(self, wait_time=DEFAULT_INTERRUPT_WAIT):
        self.interrupt_thread = Thread(target=self.perform_interrupt, args=(wait_time,))
        self.interrupt_thread.start()

    def perform_interrupt(self, wait_time):
        time.sleep(wait_time)  # Allow parent to start executing cell to interrupt
        self.interrupt()

    def terminate_interrupt_thread(self):
        if self.interrupt_thread:
            self.interrupt_thread.join()
            self.interrupt_thread = None

    def _send_request(self, code):
        """
        Builds the request and submits it to the kernel.  Prior to sending the request it
        creates an empty response queue and adds it to the dictionary using msg_id as the
        key.  The msg_id is returned in order to read responses.
        """
        msg_id = uuid4().hex
        message = KernelClient.__create_execute_request(msg_id, code)

        # create response-queue and add to map for this msg_id
        self.response_queues[msg_id] = queue.Queue()

        self.kernel_socket.send(message)

        return msg_id

    def _get_response(self, msg_id, timeout, post_idle):
        """
        Pulls the next response message from the queue corresponding to msg_id.  If post_idle is true,
        the timeout parameter is set to a very short value since a majority of time, there won't be a
        message in the queue.  However, in cases where a race condition occurs between the idle status
        and the execute_result payload - where the two are out of order, then this will pickup the result.
        """

        if post_idle and timeout > KernelClient.POST_IDLE_TIMEOUT:
            timeout = KernelClient.POST_IDLE_TIMEOUT  # overwrite timeout to small value following idle messages.

        msg_queue = self.response_queues.get(msg_id)
        try:
            self.log.debug("Getting response for msg_id: {} with timeout: {}".format(msg_id, timeout))
            response = msg_queue.get(timeout=timeout)
            self.log.debug("Got response for msg_id: {}, msg_type: {}".
                           format(msg_id, response['msg_type'] if response else 'null'))
        except queue.Empty:
            response = None

        return response

    def _read_responses(self):
        """
        Reads responses from the websocket.  For each response read, it is added to the response queue based
        on the messages parent_header.msg_id.  It does this for the duration of the class's lifetime until its
        shutdown method is called, at which time the socket is closed (unblocking the reader) and the thread
        terminates.  If shutdown happens to occur while processing a response (unlikely), termination takes
        place via the loop control boolean.
        """
        try:
            while not self.shutting_down:
                try:
                    raw_message = self.kernel_socket.recv()
                    response_message = json_decode(utf8(raw_message))

                    msg_id = KernelClient._get_msg_id(response_message, self.log)

                    if msg_id not in self.response_queues:
                        # this will happen when the msg_id is generated by the server
                        self.response_queues[msg_id] = queue.Queue()

                    # insert into queue
                    self.log.debug("Inserting response for msg_id: {}, msg_type: {}".
                                   format(msg_id, response_message['msg_type']))
                    self.response_queues.get(msg_id).put_nowait(response_message)
                except BaseException as be1:
                    if self.restarting:  # If restarting, wait until restart has completed - which includes new socket
                        i = 1
                        while self.restarting:
                            if i >= 10 and i % 2 == 0:
                                self.log.debug("Still restarting after {} secs...".format(i))
                            time.sleep(1)
                            i += 1
                        continue
                    raise be1

        except websocket.WebSocketConnectionClosedException:
            pass  # websocket closure most likely due to shutdown

        except BaseException as be2:
            if not self.shutting_down:
                self.log.warning('Unexpected exception encountered ({})'.format(be2))

        self.log.debug('Response reader thread exiting...')

    @staticmethod
    def _get_msg_id(message, logger):
        msg_id = KernelClient.DEAD_MSG_ID
        if message:
            if 'msg_id' in message['parent_header'] and message['parent_header']['msg_id']:
                msg_id = message['parent_header']['msg_id']
            elif 'msg_id' in message:
                # msg_id may not be in the parent_header, see if present in response
                # IPython kernel appears to do this after restarts with a 'starting' status
                msg_id = message['msg_id']
        else:  # Dump the "dead" message...
            logger.debug("+++++ Dumping dead message: {}".format(message))
        return msg_id

    @staticmethod
    def _convert_raw_response(raw_response_message):
        result = raw_response_message
        if isinstance(raw_response_message, str):
            if "u'" in raw_response_message:
                result = raw_response_message.replace("u'", "")[:-1]

        return result

    @staticmethod
    def __create_execute_request(msg_id, code):
        return json_encode({
            'header': {
                'username': '',
                'version': '5.0',
                'session': '',
                'msg_id': msg_id,
                'msg_type': 'execute_request'
            },
            'parent_header': {},
            'channel': 'shell',
            'content': {
                'code': "".join(code),
                'silent': False,
                'store_history': False,
                'user_expressions': {},
                'allow_stdin': False
            },
            'metadata': {},
            'buffers': {}
        })


@logged
class GatewayClient(object):
    """
    *** E X P E R I M E N T A L *** *** E X P E R I M E N T A L ***

    An experimental Gateway Client that is used for Enterprise Gateway
    integration tests and can be leveraged for micro service type of
    connections.
    """
    DEFAULT_USERNAME = os.getenv('KERNEL_USERNAME', 'pydemia')
    DEFAULT_GATEWAY_HOST = BASE_GATEWAY_URL = os.getenv('GATEWAY_HOST', 'localhost:8888')
    KERNEL_LAUNCH_TIMEOUT = os.getenv('KERNEL_LAUNCH_TIMEOUT', '60')
    DEFAULT_KERNEL_NAME = os.getenv("DEFAULT_KERNEL_NAME", "python3")
    
    BASE_GATEWAY_HTTP_URL = f"http://{BASE_GATEWAY_URL}"
    BASE_GATEWAY_WS_URL = f"ws://{BASE_GATEWAY_URL}"

    def __init__(self, host=DEFAULT_GATEWAY_HOST, password=None):
        self.http_api_endpoint = 'http://{}/api/kernels'.format(host)
        self.ws_api_endpoint = 'ws://{}/api/kernels'.format(host)
        self.log = logging.getLogger('GatewayClient')
        self.log.setLevel(log_level)
        self.http_client = httpx.Client()
        self.password = password

        self._get_login()


    # def _get_login(self) -> Tuple[httpx.Cookies, httpx.Headers]:
    def _get_login(self) -> None:

        if self.password:
            # self.session = requests.Session()
            LOGIN_URL = f"{self.BASE_GATEWAY_HTTP_URL}/login"
            r = self.http_client.get(LOGIN_URL)
            self.xsrf_cookie = r.cookies["_xsrf"]
            self.auth_body = {
                "_xsrf": self.xsrf_cookie,
                "password": self.password,
            }

            before_logined = self.http_client.post(LOGIN_URL, data=self.auth_body)
            assert before_logined.status_code == 302
            request_cookies: httpx.Cookies = dict(r.cookies, **before_logined.cookies)
            redirected_headers = {
                "Host": self.BASE_GATEWAY_URL,
                "Origin": self.BASE_GATEWAY_HTTP_URL,
                "Content-Type": "application/x-www-form-urlencoded",
                "Referer": LOGIN_URL,
            }
            after_logined = self.http_client.post(
                f"{LOGIN_URL}?next=%2F",
                cookies=request_cookies,
                headers=redirected_headers,
                data=self.auth_body,
            )
            assert after_logined.status_code == 302
            # # self.request_headers = after_logined.headers
            # self.request_cookies = after_logined.headers['set-cookie']

            cookie_header_str = "; ".join([f"{k}={v}" for k, v in request_cookies.items()])
            # self.request_cookies = req_cookies
            self.request_cookies = request_cookies
            self.request_headers = httpx.Headers(
                {
                    # "Content-Type": "application/json",
                    # "X-XSRFToken": req_cookies["_xsrf"],
                    # "Cookie": after_logined.headers["set-cookie"],
                    "X-XSRFToken": self.xsrf_cookie,
                    "Cookie": cookie_header_str,
                }
            )


    def get_kernelspecs(self) -> List[Dict]:
        resp = self.http_client.get(
            f"{self.BASE_GATEWAY_HTTP_URL}/api/kernelspecs",
            cookies=self.request_cookies,
            headers=self.request_headers,
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            raise httpx.RequestError
    
    def get_kernels(self) -> List[Dict]:
        resp = self.http_client.get(
            f"{self.BASE_GATEWAY_HTTP_URL}/api/kernels",
            params=self.auth_body,
            cookies=self.request_cookies,
            headers=self.request_headers,
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            raise httpx.RequestError
    
    def start_new_kernel(self, kernelspec_name: str = None) -> Dict:
        if not kernelspec_name:
            kernelspec_name = self.DEFAULT_KERNEL_NAME
        resp = self.http_client.post(
            f"{self.BASE_GATEWAY_HTTP_URL}/api/kernels",
            cookies=self.request_cookies,
            headers=self.request_headers,
            data=json_encode({
                "name": kernelspec_name,
                "path": "",
            }),
        )
        if resp.status_code == 201:
            return resp.json()
        else:
            raise httpx.RequestError

    def get_sessions(self, kernelspec_name: str = None) -> List[Dict]:
        # if not kernelspec_name:
        #     kernelspec_name = self.DEFAULT_KERNEL_NAME
        resp = self.http_client.get(
            f"{self.BASE_GATEWAY_HTTP_URL}/api/sessions",
            cookies=self.request_cookies,
            headers=self.request_headers,
        )
        if resp.status_code == 200:
            if kernelspec_name:
                return [k for k in resp.json() if k.kernel == kernelspec_name]
            else:
                return resp.json()
        else:
            raise httpx.RequestError


    def get_client(self, default_kernelspec_name: str = "python3", timeout: int = REQUEST_TIMEOUT) -> KernelClient:

        self.kernelspecs = self.get_kernelspecs()
        self.DEFAULT_KERNEL_NAME = self.kernelspecs["default"]

        if default_kernelspec_name in self.kernelspecs["kernelspecs"]:
            self.DEFAULT_KERNEL_NAME = default_kernelspec_name
            self.log.warn("Use kernelspec name '{default_kernelspec_name}' as default...")
        else:
            self.log.warn("The given kernelspec name '{kernelspec_name}' does not exist. use system default '{self.DEFAULT_KERNEL_NAME}' instead...")

        kernel_info = {
            'name': self.DEFAULT_KERNEL_NAME,
            # 'env': {
            #     'KERNEL_USERNAME': username,
            #     'KERNEL_LAUNCH_TIMEOUT': self.KERNEL_LAUNCH_TIMEOUT,
            # }
        }

        kernels_opened: List[Dict] = self.get_kernels()
        try:
            kernel_info: Dict = kernels_opened[0]
        except IndexError:
            kernel_info: Dict = self.start_new_kernel(kernelspec_name=None)

        self.log.debug(f"kernel_info: {kernel_info}")
        kernel_id: str = kernel_info["id"]
        
        available_sessions: List[Dict] = self.get_sessions(kernelspec_name=None)
        self.log.debug(f"available_sessions: {available_sessions}")
        
        file_path = DEFAULT_UUID
        existing_file = self.http_client.get(
            f"{self.BASE_GATEWAY_HTTP_URL}/api/contents/{file_path}",
            cookies=self.request_cookies,
            headers=self.request_headers,
        )

        if existing_file.status_code == 200:
            pass
        elif existing_file.status_code == 404:

            created_file = self.http_client.post(
                f"{self.BASE_GATEWAY_HTTP_URL}/api/contents",
                cookies=self.request_cookies,
                headers=self.request_headers,
                params=json_encode({
                    "type": "file",  # "notebook",
                    "path": "",
                    # "path": "/work/test",  # ""
                })
            )
            old_path = created_file.headers.get("location").replace("/api/contents/", "", 1)
            new_path = DEFAULT_UUID
            renamed_file = self.http_client.patch(
                f"{self.BASE_GATEWAY_HTTP_URL}/api/contents/{old_path}",
                cookies=self.request_cookies,
                headers=self.request_headers,
                data=json_encode({
                    "path": new_path,
                })
            )
            if renamed_file.status_code == 200:
                self.log.debug(f"renamed_file OK: {renamed_file.json()}")
            elif renamed_file.status_code == 409:
                self.log.debug(f"renamed_file Conflict: {renamed_file.json()}")

        # deleted_file = self.http_client.delete(
        #     f"{self.BASE_GATEWAY_HTTP_URL}/api/contents/{new_path}",
        #     cookies=self.request_cookies,
        #     headers=self.request_headers,
        # )
        # if deleted_file.status_code == 204:
        #     print("OK", "No Content")
        # self.request_headers = httpx.Headers(
        #         {
        #             "Content-Type": "application/json",
        #             "Content"
        #             "X-XSRFToken": req_cookies["_xsrf"],
        #             # "Cookie": after_logined.headers["set-cookie"],
        #         }
        #     )

        available_sessions: List[Dict] = self.get_sessions(kernelspec_name=None)
        self.log.debug(f"available_sessions: {available_sessions}")
        if available_sessions:
            available_session = available_sessions[0]
            session_id = available_session.get("id")
        else:

            data_json = json_encode({
                "kernel": kernel_info,
                "name": f"{self.DEFAULT_USERNAME}-{file_path}",
                "type": "file",
                "path": file_path,
                "_xsrf": self.xsrf_cookie,
            })
            request_headers = self.request_headers.copy()
            request_headers["content-length"] = str(len(data_json))
            created_or_existing_session = self.http_client.post(
                f"{self.BASE_GATEWAY_HTTP_URL}/api/sessions",
                cookies=self.request_cookies,
                headers=request_headers,
                data=data_json,
            )
            if created_or_existing_session.status_code == 201:
                available_session = created_or_existing_session.json()
                session_id = available_session.get("id")  # kernel_id in enterprise-gateway
                kernel_id = available_session.get("kernel").get("id")
                self.log.debug(f'Started kernel with session id {session_id}')
            else:
                raise RuntimeError(
                    'Error starting kernel : {} response code \n {}'.format(
                        created_or_existing_session.status_code,
                        created_or_existing_session.content
                    )
                )
            self.log.debug(f"existing_session: {available_session}")


        return KernelClient(
            self.http_api_endpoint,
            self.ws_api_endpoint,
            kernel_id,
            session_id,
            timeout=30,
            logger=self.log,
            cookies=self.request_cookies,
            headers=self.request_headers,
            params=self.auth_body,
        )

    # def start_kernel(self, kernelspec_name="python3", username=DEFAULT_USERNAME, timeout=REQUEST_TIMEOUT):
    #     self.log.debug('Starting a {} kernel ....'.format(kernelspec_name))

    #     if kernelspec_name in self.kernelspecs["kernelspecs"]:
    #         system_default = self.kernelspecs["default"]
    #         print("The given name '{kernelspec_name}' does not exist. use '{system_default}' instead...")
    #         kernelspec_name = system_default

    #     json_data = {
    #         'name': kernelspec_name,
    #         # 'env': {
    #         #     'KERNEL_USERNAME': username,
    #         #     'KERNEL_LAUNCH_TIMEOUT': self.KERNEL_LAUNCH_TIMEOUT,
    #         # }
    #     }

    #     # json_data = self._add_xsrf_cookie(json_data)

    #     # json_data.update({"_xsrf": self.xsrf_cookie})
    #     kernel_info: Dict = {"name": kernelspec_name}
    #     available_sessions: List[Dict] = self.http_client.get(
    #         f"{self.BASE_GATEWAY_HTTP_URL}/api/sessions",
    #         cookies=self.request_cookies,
    #         headers=self.request_headers,
    #         # data=json_encode(json_data)
    #         # data={
    #         #     "id": None,
    #         #     "kernel": kernel_info,
    #         #     # "name": f"{self.DEFAULT_USERNAME}-2413",
    #         #     # "path": DEFAULT_UUID,
    #         #     "type": "notebook",
    #         # }
    #         # data=json_encode(self._add_xsrf_cookie(json_data))
    #     )

    #     # See: https://jupyter-notebook.readthedocs.io/en/stable/extending/contents.html#filesystem-entities
    #     created_directory = self.http_client.post(
    #         f"{self.BASE_GATEWAY_HTTP_URL}/api/contents",
    #         cookies=self.request_cookies,
    #         headers=self.request_headers,
    #         data=json_encode({
    #             "type": "directory",  # "notebook", "file"
    #             "path": "",
    #             # "path": "/work/test",  # ""
    #         })
    #     )
    #     old_path = created_directory.headers.get("location").replace("/api/contents/", "", 1)
    #     new_path = DEFAULT_UUID
    #     renamed_directory = self.http_client.patch(
    #         f"{self.BASE_GATEWAY_HTTP_URL}/api/contents/{old_path}",
    #         cookies=self.request_cookies,
    #         headers=self.request_headers,
    #         data=json_encode({
    #             "path": new_path,
    #         })
    #     )
    #     if renamed_directory.status_code == 200:
    #         print("OK")
    #     elif renamed_directory.status_code == 409:
    #         print("Conflict")
    #     deleted_directory = self.http_client.delete(
    #         f"{self.BASE_GATEWAY_HTTP_URL}/api/contents/{new_path}",
    #         cookies=self.request_cookies,
    #         headers=self.request_headers,
    #     )
    #     if deleted_directory.status_code == 204:
    #         print("OK", "No Content")


    def shutdown_kernel(self, kernel):
        self.log.debug("Shutting down kernel : {} ....".format(kernel.kernel_id))

        if not kernel:
            return False

        kernel.shutdown()

        url = "{}/{}".format(self.http_api_endpoint, kernel.kernel_id)
        response = self.session.delete(
            url,
            params=self._get_xsrf_params(),
        )
        if response.status_code == 204:
            self.log.debug('Kernel {} shutdown'.format(kernel.kernel_id))
            self.session.close()
            return True
        else:
            raise RuntimeError('Error shutting down kernel {}: {}'.format(kernel.kernel_id, response.content))

