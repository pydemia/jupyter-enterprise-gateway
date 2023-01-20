from typing import Dict, Optional, Union, Tuple
import httpx
from urllib.parse import parse_qs, urlparse
import json


__all__ = [
    "request",
    "get",
    "post",
    "put",
    "delete",
    "head",
    "patch",
    "options",
    "stream",
]


def request(*args, **kwargs):
    with httpx.Client() as client:
        resp = client.request(*args, **kwargs)
    return resp


def get(*args, **kwargs):
    return request("get", *args, **kwargs)


def post(*args, **kwargs):
    return request("post", *args, **kwargs)


def put(*args, **kwargs):
    return request("put", *args, **kwargs)


def delete(*args, **kwargs):
    return request("delete", *args, **kwargs)


def head(*args, **kwargs):
    return request("head", *args, **kwargs)


def patch(*args, **kwargs):
    return request("patch", *args, **kwargs)


def options(*args, **kwargs):
    return request("options", *args, **kwargs)


def stream(*args, **kwargs):
    return request("stream", *args, **kwargs)
