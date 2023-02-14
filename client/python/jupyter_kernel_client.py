from typing import Dict, Union, Optional, List, Tuple, Iterable, Literal

import asyncio
import datetime as dt
from autologging import logged
import os
import logging
import requests
import time
from uuid import uuid4
from tornado.escape import json_encode, json_decode, utf8
from threading import Thread
import websocket
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 300))
log_level = os.getenv("LOG_LEVEL", "INFO")


import queue
import uuid
import httpx
from httpx import URL, InvalidURL
from pathlib import PosixPath, Path, PurePath


from . import async_client, blocking_client
from .utils import joinpaths, build_url

DEFAULT_UUID = "f1e163d1-463c-414b-b4d4-3e51fe427e5f"



import websockets
from websockets.uri import WebSocketURI
from websockets.extensions import ClientExtensionFactory
from websockets.client import ClientConnection
from websockets import connect
from websockets.utils import generate_key

from jupyter_client import BlockingKernelClient, AsyncKernelClient

import ast

def decode_cellmsg(res: Union[str, List[str]]):
    if isinstance(res, str):
        res = [res]
    msg = ["\n".join(m) if isinstance(m, list) else m for m in res]
    # msg = [ast.literal_eval(f"b'''{m}'''").decode() for m in res]
    return '\n'.join(msg)
    # return msg



URLPATH_LOGIN = "/login"
URLPATH_KERNELSPECS = "/api/kernelspecs"
URLPATH_KERNELS = "/api/kernels"
URLPATH_SESSIONS = "/api/sessions"
URLPATH_CONTENTS = "/api/contents"
URLPATH_ME = "/api/me"


@logged
class KernelClient(object):

    DEAD_MSG_ID = 'deadbeefdeadbeefdeadbeefdeadbeef'
    POST_IDLE_TIMEOUT = 0.5
    DEFAULT_INTERRUPT_WAIT = 1

    def __init__(
            self,
            http_api_endpoint: Union[str, URL],
            ws_api_endpoint: Union[str, URL],
            kernel_id: str,
            session_id: Optional[str] = None,
            type: Literal["normal", "gw"] = "normal",
            timeout=REQUEST_TIMEOUT,
            logger=None,
            cookies: Union[httpx.Cookies, Dict] = {},
            headers: Union[httpx.Headers, Dict] = {},
            params: str = None,
            # session_info: Dict = None
            ):
        self.shutting_down = False
        self.restarting = False
        self.http_url = http_api_endpoint
        self.ws_url = ws_api_endpoint
        self.kernel_id = kernel_id
        self.server_type = type
        self.session_id = None
        if self.server_type == "normal":
            self.session_id = session_id
        self.cookies = httpx.Cookies(cookies)
        self.headers = httpx.Headers(headers)
        self.params = params
        self.timeout = timeout
        self.log = logging.getLogger('GatewayClient')
        self.log.setLevel(log_level)

        self.http_url_login = build_url(self.http_url, URLPATH_LOGIN)
        self.http_url_kernelspecs = build_url(self.http_url, URLPATH_KERNELSPECS)
        self.http_url_kernels = build_url(self.http_url, URLPATH_KERNELS)
        self.http_url_sessions = build_url(self.http_url, URLPATH_SESSIONS)
        if self.server_type == "normal":
            self.ws_url_sessions = build_url(self.ws_url, URLPATH_SESSIONS)
        else:
            self.ws_url_sessions = self.http_url_kernels
        self.http_url_contents = build_url(self.http_url, URLPATH_CONTENTS)

        self.http_api_endpoint = build_url(
            self.http_url,
            URLPATH_KERNELS,
            kernel_id,
        )
        self.ws_api_endpoint = build_url(
            self.ws_url,
            URLPATH_KERNELS,
            kernel_id,
            "channels",
            params={"session_id": session_id},
        )
        self.http_api_endpoint_interrupt = build_url(
            self.http_api_endpoint,
            "interrupt",
        )
        self.http_api_endpoint_restart = build_url(
            self.http_api_endpoint,
            "restart",
        )


        self.log.debug('Initializing kernel client ({}) to {}'.format(kernel_id, self.ws_api_endpoint))

        self.http_client = httpx.Client()
        # checked_session = self.http_client.get(
        #     build_url(self.http_url_sessions, session_id),
        #     cookies=self.cookies,
        #     headers=self.headers,
        # )

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
        self._cookie_header_str = "; ".join([f"{k}={v}" for k, v in cookies.items()])
        # session_info: Dict = checked_session.json()
        # headers.update(
        #     {
        #         "Accept": "*/*",
        #         "Cache-Control": "no-cache",
        #         "Pragma": "no-cache",
        #         "Cookie": self._cookie_header_str,
        #         "X-XSRFToken": self.cookies["_xsrf"],
        #         "Upgrade": "websocket",
        #         "Connection": "Upgrade",
        #         "Sec-Fetch-Dest": "empty",
        #         "Sec-Fetch-Mode": "cors",
        #         "Sec-Fetch-Site": "same-origin",
        #         "Sec-WebSocket-Key": generate_key(),
        #         "Sec-WebSocket-Version": "13",
        #         "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
        #     }
        # )
        # available_kernels = self.http_client.get(
        #     self.http_url_kernels,
        #     cookies=self.cookies,
        #     headers=self.headers,
        # )
        # available_kernels = available_kernels.json()
        self._create_ws_connection()


    def _create_ws_connection(self):
        self.websocket_extra_headers = {
            "X-XSRFToken": self.cookies.get("_xsrf", None),
            "Cookie": self._cookie_header_str,
        }

        try:
            self.kernel_socket = websocket.create_connection(
                str(self.ws_api_endpoint),
                timeout=self.timeout,
                enable_multithread=True,
                header=self.websocket_extra_headers,
            )
            self.log.debug(f'Kernel {self.kernel_id} connected')

        except websocket.WebSocketBadStatusException as e:
            self.kernel_socket = None
            self.log.debug(f'Kernel {self.kernel_id} cannot be connected')
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

    def execute(self, code, timeout=REQUEST_TIMEOUT) -> Tuple[Iterable[str], dt.timedelta]:
        """
        Executes the code provided and returns the result of that execution.
        """
        if not self.kernel_socket:
            self._create_ws_connection()

        start_dt = dt.datetime.now()
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
                        response.extend(
                            [
                                '{} : {}'.format(
                                    response_message['content']['ename'],
                                    response_message['content']['evalue'],
                                ),
                                response_message['content']['traceback'],
                            ]
                        )
                        # response.append('{}:{}:{}'.format(response_message['content']['ename'],
                        #                                   response_message['content']['evalue'],
                        #                                   response_message['content']['traceback']))
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

        
        end_dt = dt.datetime.now()
        elapsed_dt = end_dt - start_dt
        self.log.debug(f"ELAPSED TIME: {elapsed_dt}")
        return response, elapsed_dt


    async def execute_async(self, code, timeout=REQUEST_TIMEOUT) -> Iterable[str]:  # -> Tuple[Iterable[str], dt.timedelta]:
        """
        Executes the code provided and returns the result of that execution.
        """
        if not self.kernel_socket:
            self._create_ws_connection()

        ws = self.kernel_socket
        start_dt = dt.datetime.now()

        def format_msg(msg: List[Optional[str]], start_dt: dt.timedelta) -> Tuple[List[str], dt.timedelta]:
            return msg, dt.datetime.now() - start_dt
        # async def format_msg(msg: List[Optional[str]], start_dt: dt.timedelta) -> Tuple[List[str], dt.timedelta]:
        #     return msg, dt.datetime.now() - start_dt

        # msg_id = self._send_request(code)
        # self.response_queues[msg_id] = queue.Queue()
        # # msg_id = await ws.send(code)
        # msg_resp, elapsed = await ws.recv(), (dt.datetime.now() - start_dt)
        # print(msg_resp, elapsed)
        msg_resp = []

        try:
            msg_id = self._send_request(code)
            msg_resp.append(msg_id)
            # await asyncio.gather(format_msg(msg_resp, start_dt))
            # await msg_list, dt.datetime.now() - start_dt
            # yield asyncio.gather(format_msg(msg_resp, start_dt))
            yield format_msg(msg_resp, start_dt)

            post_idle = False
            while True:
                response_message = self._get_response(msg_id, timeout, post_idle)
                # response_message = await self._get_response_async(msg_id, timeout, post_idle)
                if response_message:
                    response_message_type = response_message['msg_type']

                    if response_message_type == 'error' or \
                            (response_message_type == 'execute_reply' and
                                response_message['content']['status'] == 'error'):
                        msg_list = [
                            '{} : {}'.format(
                                response_message['content']['ename'],
                                response_message['content']['evalue'],
                            ),
                            response_message['content']['traceback'],
                        ]
                        msg_resp.extend(msg_list)
                        # await asyncio.gather(format_msg(msg_resp, start_dt))
                        # yield asyncio.gather(format_msg(msg_resp, start_dt))
                        yield format_msg(msg_resp, start_dt)
                        # await msg_list, dt.datetime.now() - start_dt

                    elif response_message_type == 'stream':
                        msg_list = [
                            KernelClient._convert_raw_response(response_message['content']['text'])
                        ]
                        msg_resp.extend(msg_list)
                        # await asyncio.gather(format_msg(msg_resp, start_dt))
                        # yield asyncio.gather(format_msg(msg_resp, start_dt))
                        yield format_msg(msg_resp, start_dt)
                        # await msg_list, dt.datetime.now() - start_dt

                    elif response_message_type == 'execute_result' or response_message_type == 'display_data':
                        if 'text/plain' in response_message['content']['data']:
                            msg_list = [
                                KernelClient._convert_raw_response(response_message['content']['data']['text/plain'])
                            ]
                            msg_resp.extend(msg_list)
                            # await asyncio.gather(format_msg(msg_resp, start_dt))
                            # yield asyncio.gather(format_msg(msg_resp, start_dt))
                            yield format_msg(msg_resp, start_dt)
                            # await msg_list, dt.datetime.now() - start_dt

                        elif 'text/html' in response_message['content']['data']:
                            msg_list = [
                                KernelClient._convert_raw_response(response_message['content']['data']['text/html'])
                            ]
                            msg_resp.extend(msg_list)
                            # await asyncio.gather(format_msg(msg_resp, start_dt))
                            # yield asyncio.gather(format_msg(msg_resp, start_dt))
                            yield format_msg(msg_resp, start_dt)
                            # await msg_list, dt.datetime.now() - start_dt

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
                    # return await asyncio.gather(format_msg(msg_resp, start_dt))
                    # yield asyncio.gather(format_msg(msg_resp, start_dt))
                    yield format_msg(msg_resp, start_dt)
                    break
                    # return await msg_list, dt.datetime.now() - start_dt
                    # break

        except BaseException as b:
            self.log.debug(b)
            # return await asyncio.gather(format_msg(msg_resp, start_dt))
            # yield await asyncio.gather(format_msg(msg_resp, start_dt))
            yield format_msg(msg_resp, start_dt)
            raise StopAsyncIteration(b)
            # return await msg_list, dt.datetime.now() - start_dt

        
        # end_dt = dt.datetime.now()
        # elapsed_dt = end_dt - start_dt
        # self.log.debug(f"ELAPSED TIME: {elapsed_dt}")

        # self.websocket_extra_headers = {
        #     "X-XSRFToken": self.cookies.get("_xsrf", None),
        #     "Cookie": self._cookie_header_str,
        # }
        # async with websockets.connect(
        #     str(self.ws_api_endpoint),
        #     timeout=self.timeout,
        #     extra_headers=self.websocket_extra_headers,
        # ) as ws:
        #     start_dt = dt.datetime.now()
        #     msg_id = ws.send(code)
        #     # msg_id = await ws.send(code)
        #     msg_resp, elapsed = await ws.recv(), (dt.datetime.now() - start_dt)
        #     print(msg_resp, elapsed)

        # ws = websockets.connect(
        #     str(self.ws_api_endpoint),
        #     timeout=self.timeout,
        #     extra_headers=self.websocket_extra_headers,
        # )
        # start_dt = dt.datetime.now()
        # msg_id = ws.send(code)
        # # msg_id = await ws.send(code)
        # msg_resp, elapsed = await ws.recv(), (dt.datetime.now() - start_dt)
        # print(msg_resp, elapsed)

            # try:
            #     msg_id = await ws.send(code)
            # except websockets.ConnectionClosed:
            #     continue

        # try:
        #     self.kernel_socket = websocket.create_connection(
        #         str(self.ws_api_endpoint),
        #         timeout=self.timeout,
        #         enable_multithread=True,
        #         header=self.websocket_extra_headers,
        #     )
        #     self.log.debug(f'Kernel {self.kernel_id} connected')

        # except websocket.WebSocketBadStatusException as e:
        #     self.kernel_socket = None
        #     self.log.debug(f'Kernel {self.kernel_id} cannot be connected')
        #     raise e
            
        # start_dt = dt.datetime.now()
        # response = []
        # try:
        #     msg_id = self._send_request(code)

        #     post_idle = False
        #     while True:
        #         response_message = self._get_response(msg_id, timeout, post_idle)
        #         if response_message:
        #             response_message_type = response_message['msg_type']

        #             if response_message_type == 'error' or \
        #                     (response_message_type == 'execute_reply' and
        #                      response_message['content']['status'] == 'error'):
        #                 response.extend(
        #                     [
        #                         '{} : {}'.format(
        #                             response_message['content']['ename'],
        #                             response_message['content']['evalue'],
        #                         ),
        #                         response_message['content']['traceback'],
        #                     ]
        #                 )
        #                 # response.append('{}:{}:{}'.format(response_message['content']['ename'],
        #                 #                                   response_message['content']['evalue'],
        #                 #                                   response_message['content']['traceback']))
        #             elif response_message_type == 'stream':
        #                 response.append(KernelClient._convert_raw_response(response_message['content']['text']))

        #             elif response_message_type == 'execute_result' or response_message_type == 'display_data':
        #                 if 'text/plain' in response_message['content']['data']:
        #                     response.append(
        #                         KernelClient._convert_raw_response(response_message['content']['data']['text/plain']))
        #                 elif 'text/html' in response_message['content']['data']:
        #                     response.append(
        #                         KernelClient._convert_raw_response(response_message['content']['data']['text/html']))
        #             elif response_message_type == 'status':
        #                 if response_message['content']['execution_state'] == 'idle':
        #                     post_idle = True  # indicate we're at the logical end and timeout poll for next message
        #                     continue
        #             else:
        #                 self.log.debug("Unhandled response for msg_id: {} of msg_type: {}".
        #                                format(msg_id, response_message_type))

        #         if response_message is None:  # We timed out.  If post idle, its ok, else make mention of it
        #             if not post_idle:
        #                 self.log.warning("Unexpected timeout occurred for msg_id: {} - no 'idle' status received!".
        #                                  format(msg_id))
        #             break

        # except BaseException as b:
        #     self.log.debug(b)

        
        # end_dt = dt.datetime.now()
        # elapsed_dt = end_dt - start_dt
        # self.log.debug(f"ELAPSED TIME: {elapsed_dt}")
        # return response, elapsed_dt


    def interrupt(self):
        resp = self.http_client.post(
            self.http_api_endpoint_interrupt,
            cookies=self.cookies,
            headers=self.headers,
        )
        if resp.status_code == 204:
            self.log.debug('Kernel {} interrupted'.format(self.kernel_id))
            return True
        else:
            raise RuntimeError(
                'Unexpected response interrupting kernel {}: {}'.format(
                    self.kernel_id,
                    resp.content,
                )
            )

    def restart(self):
        self.restarting = True
        if self.kernel_socket:
            self.kernel_socket.close()
            self.kernel_socket = None

        resp = self.http_client.post(
            self.http_api_endpoint_restart,
            cookies=self.cookies,
            headers=self.headers,
        )
        if resp.status_code == 200:
            self.log.debug('Kernel {} restarted'.format(self.kernel_id))
            self._create_ws_connection()
            self.restarting = False
            return True
        else:
            self.restarting = False
            raise RuntimeError(
                'Unexpected response restarting kernel {}: {}'.format(
                    self.kernel_id,
                    resp.content
                )
            )

    def get_state(self):
        
        resp = self.http_client.get(
            self.http_api_endpoint,
            cookies=self.cookies,
            headers=self.headers,
        )
        if resp.status_code == 200:
            json = resp.json()
            self.log.debug('Kernel {} state: {}'.format(self.kernel_id, json))
            return json['execution_state']
        else:
            raise RuntimeError(
                'Unexpected response retrieving state for kernel {}: {}'.format(
                    self.kernel_id,
                    resp.content,
                )
            )

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

    async def _get_response_async(self, msg_id, timeout, post_idle):
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
    An experimental Gateway Client that is used for Enterprise Gateway
    integration tests and can be leveraged for micro service type of
    connections.
    """
    DEFAULT_USERNAME = os.getenv('KERNEL_USERNAME', 'jovyan')
    DEFAULT_GATEWAY_HOST = BASE_GATEWAY_URL = os.getenv('GATEWAY_HOST', 'http://localhost:8888')
    KERNEL_LAUNCH_TIMEOUT = os.getenv('KERNEL_LAUNCH_TIMEOUT', '60')
    DEFAULT_KERNEL_NAME = os.getenv("DEFAULT_KERNEL_NAME", "python3")
    K8S_KERNEL_NAMESPACE = os.getenv("KERNEL_NAMESPACE", "default")
    K8S_SERVICE_ACCOUNT_NAME = "default"

    
    # BASE_GATEWAY_HTTP_URL = f"http://{BASE_GATEWAY_URL}"
    # BASE_GATEWAY_WS_URL = f"ws://{BASE_GATEWAY_URL}"

    def __init__(self, host=DEFAULT_GATEWAY_HOST, type: Literal["normal", "gw"] = "normal", password: str = None):
        
        self._set_urls(host=host)

        self.log = logging.getLogger('GatewayClient')

        self.log.setLevel(log_level)
        self.http_client = httpx.Client()

        self.request_cookies = {}
        self.request_headers = {}
        self.auth_body = {}
        self.xsrf_cookie = ""

        self.server_type: Literal["normal", "gw"] = type
        if self.server_type == "normal":
            if password is not None:
                self.password = password
                self._get_login()
                # raise NotImplementedError("password must be given.")
        elif self.server_type == "gw":
            self.DEFAULT_KERNEL_NAME = "python_kubernetes"

        else:
            self.log.warn(f"client type is [{type}], not using the password...")
            self.password = None


    def _set_urls(self, host=DEFAULT_GATEWAY_HOST) -> None:
        self.http_url: URL = URL(host)
        http_scheme = self.http_url.scheme
        if http_scheme not in ["http", "https"]:
            raise InvalidURL(message="Scheme must be given: [http, https]") from None
        
        self.url_subpath = self.http_url.path
        self.url_domain = self.http_url.netloc.decode()
        self.origin = self.url_domain
        if http_scheme.endswith("s"):
            self.ws_url = URL(self.http_url, scheme="wss")
        else:
            self.ws_url = URL(self.http_url, scheme="ws")

        self.http_url_login = build_url(self.http_url, URLPATH_LOGIN)
        self.http_url_kernelspecs = build_url(self.http_url, URLPATH_KERNELSPECS)
        self.http_url_kernels = build_url(self.http_url, URLPATH_KERNELS)
        self.http_url_sessions = build_url(self.http_url, URLPATH_SESSIONS)
        self.ws_url_sessions = build_url(self.ws_url, URLPATH_SESSIONS)
        self.http_url_contents = build_url(self.http_url, URLPATH_CONTENTS)


    # def _get_login(self) -> Tuple[httpx.Cookies, httpx.Headers]:
    def _get_login(self) -> None:

        if self.password:
            client = self.http_client
            _login_request = client.build_request("GET", self.http_url)
            request_cookies = httpx.Cookies()
            while _login_request is not None:
                r = client.send(_login_request)
                request_cookies.update(r.cookies)
                _login_request = r.next_request

            self.xsrf_cookie = r.cookies["_xsrf"]
            self.auth_body = {
                "_xsrf": self.xsrf_cookie,
                "password": self.password,
            }

            before_logined = self.http_client.post(
                self.http_url_login,
                data=self.auth_body,
            )
            assert before_logined.status_code == 302
            request_cookies: httpx.Cookies = dict(
                r.cookies,
                **before_logined.cookies,
            )
            origin_headers = {
                "Host": str(self.url_domain),
                "Origin": str(URL(self.http_url, path=None)),
            }
            redirected_headers = dict(
                origin_headers,
                # **{
                #     "Content-Type": "application/x-www-form-urlencoded",
                #     "Referer": str(self.http_url_login),
                # }
            )
            after_logined = self.http_client.post(
                URL(self.http_url_login, params={"next": self.url_subpath}),
                cookies=request_cookies,
                headers=redirected_headers,
                data=self.auth_body,
            )
            assert after_logined.status_code == 302

            cookie_header_str = "; ".join(
                [f"{k}={v}" for k, v in request_cookies.items()]
            )
            self.request_cookies = request_cookies
            self.request_headers = httpx.Headers(
                dict(
                    origin_headers,
                    **{
                        "Cookie": cookie_header_str,
                        "X-XSRFToken": self.xsrf_cookie,
                        
                    }
                )
            )

    def get_kernelspecs(self) -> List[Dict]:
        resp = self.http_client.get(
            self.http_url_kernelspecs,
            cookies=self.request_cookies,
            headers=self.request_headers,
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            raise httpx.RequestError
    
    def get_kernels(self) -> List[Dict]:
        resp = self.http_client.get(
            self.http_url_kernels,
            cookies=self.request_cookies,
            headers=self.request_headers,
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            raise httpx.RequestError
    
    def get_kernel(self, kernel_id: str) -> Dict:
        resp = self.http_client.get(
            build_url(self.http_url_kernels, kernel_id),
            cookies=self.request_cookies,
            headers=self.request_headers,
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            raise httpx.RequestError
    
    def delete_kernel(self, kernel_id: str) -> Dict:
        resp = self.http_client.delete(
            build_url(self.http_url_kernels, kernel_id),
            cookies=self.request_cookies,
            headers=self.request_headers,
        )
        if resp.status_code == 204:
            return True
        else:
            raise httpx.RequestError(
                'Error shutting down kernel {}: {}'.format(
                    kernel_id,
                    resp.content
                )
            )
    
    def start_new_kernel(self, kernelspec_name: str = None) -> Dict:
        if not kernelspec_name:
            kernelspec_name = self.DEFAULT_KERNEL_NAME
        resp = self.http_client.post(
            self.http_url_kernels,
            cookies=self.request_cookies,
            headers=self.request_headers,
            data=json_encode({
                "name": kernelspec_name,
                "path": "",  # local notebook or lab, hub
                "env": {
                    "KERNEL_USERNAME": self.DEFAULT_USERNAME,
                    "KERNEL_LAUNCH_TIMEOUT": self.KERNEL_LAUNCH_TIMEOUT,
                    "KERNEL_NAMESPACE": self.K8S_KERNEL_NAMESPACE,
                    "KERNEL_SERVICE_ACCOUNT_NAME": self.K8S_SERVICE_ACCOUNT_NAME,
                }
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
            self.http_url_sessions,
            cookies=self.request_cookies,
            headers=self.request_headers,
        )
        if resp.status_code == 200:
            if kernelspec_name:
                return [k for k in resp.json() if k["kernel"]["name"] == kernelspec_name]
            else:
                return resp.json()
        else:
            raise httpx.RequestError


    def get_client(
            self,
            kernelspec_name: Optional[str] = None,
            ws_timeout: int = REQUEST_TIMEOUT,
            ) -> KernelClient:

        if kernelspec_name is None:
            kernelspec_name = self.DEFAULT_KERNEL_NAME
        self.kernelspecs = self.get_kernelspecs()
        self.DEFAULT_KERNEL_NAME = self.kernelspecs["default"]

        if kernelspec_name in self.kernelspecs["kernelspecs"]:
            self.DEFAULT_KERNEL_NAME = kernelspec_name
            self.log.warning(f"Use kernelspec name '{kernelspec_name}' as default...")
        else:
            self.log.warning(f"The given kernelspec name '{kernelspec_name}' does not exist. use system default '{self.DEFAULT_KERNEL_NAME}' instead...")

        # kernel_info = {
        #     'name': self.DEFAULT_KERNEL_NAME,
        #     # 'env': {
        #     #     'KERNEL_USERNAME': username,
        #     #     'KERNEL_LAUNCH_TIMEOUT': self.KERNEL_LAUNCH_TIMEOUT,
        #     # }
        # }

        kernels_opened: List[Dict] = self.get_kernels()
        try:
            kernel_info: Dict = kernels_opened[0]
        except IndexError:
            kernel_info: Dict = self.start_new_kernel(kernelspec_name=kernelspec_name)

        self.log.debug(f"kernel_info: {kernel_info}")
        kernel_id: str = kernel_info["id"]

        session_id = None
        if self.server_type == "normal":
            available_sessions: List[Dict] = self.get_sessions(
                kernelspec_name=kernelspec_name,
            )
            self.log.debug(f"available_sessions: {available_sessions}")
            if available_sessions:
                available_session = available_sessions[0]
                session_id = available_session.get("id")
            else:

                data_json = json_encode({
                    "kernel": kernel_info,
                    "name": f"session-{kernelspec_name}-{kernel_id}",
                    "type": "file",
                    "path": "",
                    "_xsrf": self.xsrf_cookie,
                })
                request_headers = self.request_headers.copy()
                request_headers["content-length"] = str(len(data_json))

                created_or_existing_session = self.http_client.post(
                    self.http_url_sessions,
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
            self.http_url,
            self.ws_url,
            kernel_id,
            session_id,
            type=self.server_type,
            timeout=ws_timeout,
            logger=self.log,
            cookies=self.request_cookies,
            headers=self.request_headers,
            params=self.auth_body,
        )


    def shutdown_client(self, kernel_client: KernelClient):
        self.log.debug(
            "Shutting down kernel : {} ....".format(
                kernel_client.kernel_id
            )
        )

        if not kernel_client:
            return False

        kernel_client.shutdown()

        try:
            self.delete_kernel(kernel_id=kernel_client.kernel_id)
            self.log.debug('Kernel {} shutdown'.format(kernel_client.kernel_id))
            return True
        except httpx.RequestError as e:
            raise e
