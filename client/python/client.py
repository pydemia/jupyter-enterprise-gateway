from typing import Dict, Union, Optional, List

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

async def get_xsrf_cookie(url):
    response = await async_client.get(f"{url}/login")
    return response.cookies["_xsrf"]

async def get_login(xsrf_cookie_val, password, url):
    pw_body = {
        "_xsrf": xsrf_cookie_val,
        "password": password,
    }
    response = await async_client.post(
        f"{url}/login",
        data=pw_body,
    )
    response = await async_client.post(
        f"{url}/login?next=%2F",
        data=pw_body,
        cookies={"_xsrf": xsrf_cookie_val},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    return response


async def get_token_callback(r, cookies: httpx.Cookies):
    if isinstance(r, requests.Response):
        parsed = urlparse(r.url)
        params = parse_qs(parsed.query)
    elif isinstance(r, httpx.Response):
        parsed = urlparse(r.headers["location"])
        params: Dict = parse_qs(parsed.query)
    else:
        return httpx.Response(status_code=422)

    if "code" in params:
        r.hook_called = True  # for `requests` only.
        params: httpx.QueryParams = httpx.QueryParams(params).merge(r.url.params)
        callback_url: str = params.get("callback")
        resp = await async_client.get(
            f"{callback_url}/getToken", params=params, cookies=cookies,
        )
        return resp
    else:
        return httpx.Response(status_code=401)


async def auth_code(user_id: str, cookies: Union[httpx.Cookies, Dict], sso_url: str):
    # sso_url = SSO_URL
    params = {
        "clientId": user_id,
        "callback": sso_url
    }
    response = await async_client.get(
        f"{sso_url}/authCode", params=params, cookies=cookies)
    resp = await get_token_callback(response, cookies=cookies)
    return resp



class GatewayClient(object):
    """
    *** E X P E R I M E N T A L *** *** E X P E R I M E N T A L ***

    An experimental Gateway Client that is used for Enterprise Gateway
    integration tests and can be leveraged for micro service type of
    connections.
    """
    DEFAULT_USERNAME = os.getenv('KERNEL_USERNAME', 'pydemia')
    DEFAULT_GATEWAY_HOST = BASE_GATEWAY_URL = os.getenv('GATEWAY_HOST', 'localhost:8888')
    KERNEL_LAUNCH_TIMEOUT = os.getenv('KERNEL_LAUNCH_TIMEOUT', '40')
    DEFAULT_KERNEL_NAME = os.getenv("DEFAULT_KERNEL_NAME", "python3")
    
    BASE_GATEWAY_HTTP_URL = f"http://{BASE_GATEWAY_URL}"
    BASE_GATEWAY_WS_URL = f"ws://{BASE_GATEWAY_URL}"

    def __init__(self, host=DEFAULT_GATEWAY_HOST, password=None):
        self.http_api_endpoint = 'http://{}/api/kernels'.format(host)
        self.ws_api_endpoint = 'ws://{}/api/kernels'.format(host)
        self.log = logging.getLogger('GatewayClient')
        self.log.setLevel(log_level)
        if password:
            self.session = requests.Session()
            self.http_client = httpx.Client()
            LOGIN_URL = f"{self.BASE_GATEWAY_HTTP_URL}/login"
            r = self.http_client.get(LOGIN_URL)
            self.xsrf_cookie = r.cookies["_xsrf"]
            xsrf_params = {
                "_xsrf": self.xsrf_cookie
            }
            p = {
                "password": password,
            }
            params = {
                "_xsrf": self.xsrf_cookie,
                "password": password,
            }
            s = self.http_client.post(LOGIN_URL, data=params)
            req_cookies: httpx.Cookies = dict(r.cookies, **s.cookies)
            redirected_headers = {
                "Host": self.BASE_GATEWAY_URL,
                "Origin": self.BASE_GATEWAY_HTTP_URL,
            }
            ss = self.http_client.post(
                f"{LOGIN_URL}?next=%2F",
                # cookies=xsrf_params,
                cookies=req_cookies,
                headers=dict(
                    redirected_headers,
                    **{
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Referer": LOGIN_URL,
                    }
                ),
                data=params,
            )
            # sss = self.session.post(
            #     f"{LOGIN_URL}?next=%2Flab%3F",
            #     # cookies=xsrf_params,
            #     cookies=req_cookies,
            #     headers=redirected_headers,
            #     data=params,
            # )
            resp = self.http_client.get(
                self.http_api_endpoint,
                params=params,
                cookies=ss.cookies,
                headers=ss.headers,
            )
            kernels_opened: List[Dict] = resp.json()
            if resp.status_code == 200:
                self.request_cookies = req_cookies
                self.request_headers = dict(
                    redirected_headers,
                    **{"X-XSRFToken": self.xsrf_cookie},
                )

            self.kernelspecs = self.get_kernelspecs()
            if self.kernelspecs:
                self.DEFAULT_KERNEL_NAME = self.kernelspecs["default"]

            # kernel_info: Dict = kernels_opened[0]
            # kernel_id: str = kernel_info["id"]
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

    def _get_xsrf_headers(self, headers: Dict = {}) -> Dict:
        if self.xsrf_cookie:
            headers.update({"X-XSRFToken": self.xsrf_cookie})
        return headers

    def _get_xsrf_params(self, params: Dict = {}) -> Dict:
        if self.xsrf_cookie:
            params.update({"_xsrf": self.xsrf_cookie})
        return params

    def get_kernelspecs(self) -> List[Dict]:
        resp = self.session.get(
            f"{self.BASE_GATEWAY_HTTP_URL}/api/kernelspecs",
            data={
                "_xsrf": self.xsrf_cookie,
                # "password": "zxc",
            },
            cookies=self.request_cookies,
            headers=self.request_headers,
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            raise httpx.RequestError

    def start_kernel(self, kernelspec_name="python3", username=DEFAULT_USERNAME, timeout=REQUEST_TIMEOUT):
        self.log.info('Starting a {} kernel ....'.format(kernelspec_name))

        if kernelspec_name in self.kernelspecs["kernelspecs"]:
            system_default = self.kernelspecs["default"]
            print("The given name '{kernelspec_name}' does not exist. use '{system_default}' instead...")
            kernelspec_name = system_default

        json_data = {
            'name': kernelspec_name,
            # 'env': {
            #     'KERNEL_USERNAME': username,
            #     'KERNEL_LAUNCH_TIMEOUT': self.KERNEL_LAUNCH_TIMEOUT,
            # }
        }

        # json_data = self._add_xsrf_cookie(json_data)

        # json_data.update({"_xsrf": self.xsrf_cookie})
        kernel_info: Dict = {"name": kernelspec_name}
        available_sessions: List[Dict] = self.http_client.get(
            f"{self.BASE_GATEWAY_HTTP_URL}/api/sessions",
            cookies=self.request_cookies,
            headers=self.request_headers,
            # data=json_encode(json_data)
            # data={
            #     "id": None,
            #     "kernel": kernel_info,
            #     # "name": f"{self.DEFAULT_USERNAME}-2413",
            #     # "path": DEFAULT_UUID,
            #     "type": "notebook",
            # }
            # data=json_encode(self._add_xsrf_cookie(json_data))
        )

        # See: https://jupyter-notebook.readthedocs.io/en/stable/extending/contents.html#filesystem-entities
        # created_directory = self.http_client.post(
        #     f"{self.BASE_GATEWAY_HTTP_URL}/api/contents",
        #     cookies=self.request_cookies,
        #     headers=self.request_headers,
        #     data=json_encode({
        #         "type": "directory",  # "notebook", "file"
        #         "path": "",
        #         # "path": "/work/test",  # ""
        #     })
        # )
        # old_path = created_directory.headers.get("location").replace("/api/contents/", "", 1)
        # new_path = DEFAULT_UUID
        # renamed_directory = self.http_client.patch(
        #     f"{self.BASE_GATEWAY_HTTP_URL}/api/contents/{old_path}",
        #     cookies=self.request_cookies,
        #     headers=self.request_headers,
        #     data=json_encode({
        #         "path": new_path,
        #     })
        # )
        # if renamed_directory.status_code == 200:
        #     print("OK")
        # elif renamed_directory.status_code == 409:
        #     print("Conflict")
        # deleted_directory = self.http_client.delete(
        #     f"{self.BASE_GATEWAY_HTTP_URL}/api/contents/{new_path}",
        #     cookies=self.request_cookies,
        #     headers=self.request_headers,
        # )
        # if deleted_directory.status_code == 204:
        #     print("OK", "No Content")

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
                print("OK")
            elif renamed_file.status_code == 409:
                print("Conflict")
        # deleted_file = self.http_client.delete(
        #     f"{self.BASE_GATEWAY_HTTP_URL}/api/contents/{new_path}",
        #     cookies=self.request_cookies,
        #     headers=self.request_headers,
        # )
        # if deleted_file.status_code == 204:
        #     print("OK", "No Content")

        created_or_existing_session = self.http_client.post(
            f"{self.BASE_GATEWAY_HTTP_URL}/api/sessions",
            cookies=self.request_cookies,
            headers=self.request_headers,
            data=json_encode({
                "kernel": kernel_info,
                "name": f"{self.DEFAULT_USERNAME}-{file_path}",
                "type": "file",
                "path": file_path
            }),
            # data=json_encode(json_data)
            # data={
            #     "id": None,
            #     "kernel": kernel_info,
            #     "name": f"{self.DEFAULT_USERNAME}-2413",
            #     "path": DEFAULT_UUID,
            #     "type": "notebook",
            # }
            # data=json_encode(self._add_xsrf_cookie(json_data))
        )
        if created_or_existing_session.status_code == 201:
            json_data = created_or_existing_session.json()
            session_id = json_data.get("id")  # kernel_id in enterprise-gateway
            kernel_id = json_data.get("kernel").get("id")
            self.log.info(f'Started kernel with session id {session_id}')
        else:
            raise RuntimeError(
                'Error starting kernel : {} response code \n {}'.format(
                    created_or_existing_session.status_code,
                    created_or_existing_session.content
                )
            )

        return KernelSessionClient(
            self.http_api_endpoint,
            self.ws_api_endpoint,
            kernel_id,
            session_id,
            timeout=timeout,
            logger=self.log,
            cookies=self.request_cookies,
            headers=self.request_headers,
            session_info=created_or_existing_session.json(),
            # session_id=created_or_existing_session.get("id")
            # headers=self.request_headers,
        )

    def shutdown_kernel(self, kernel):
        self.log.info("Shutting down kernel : {} ....".format(kernel.kernel_id))

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


class KernelSessionClient(object):

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
            cookies=None,
            headers=None,
            session_info: Dict = None):
        self.shutting_down = False
        self.restarting = False
        self.http_api_endpoint = http_api_endpoint
        self.kernel_http_api_endpoint = '{}/{}'.format(http_api_endpoint, kernel_id)
        self.ws_api_endpoint = ws_api_endpoint
        self.kernel_ws_api_endpoint = '{}/{}/channels'.format(ws_api_endpoint, kernel_id)
        self.kernel_id = kernel_id
        self.session_id = session_id
        self.session_info = session_info
        self.cookies = cookies
        self.headers = headers
        self.log = logger
        self.log.debug('Initializing kernel client ({}) to {}'.format(kernel_id, self.kernel_ws_api_endpoint))

        try:
            params_dict = {"session_id": self.session_id}
            params_str = "&".join([
                f"{k}={v}" for k, v in params_dict.items()
            ])
            headers.update({"Sec-WebSocket-Key": "vSIvyDm4+qW272YTdauU5w=="})
            self.kernel_socket = websocket.create_connection(
                f"{self.kernel_ws_api_endpoint}?{params_str}",
                timeout=timeout,
                enable_multithread=True,
                cookies=cookies,
                headers=headers,
                origin="http://localhost:8888",
                # params={"session_id": self.session_id}
            )
        except websocket.WebSocketBadStatusException as e:
            pass

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
            self.kernel_socket = \
                websocket.create_connection(self.kernel_ws_api_endpoint, timeout=timeout, enable_multithread=True)
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
