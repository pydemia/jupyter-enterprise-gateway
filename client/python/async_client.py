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


async def request(
        *args,
        transport: Optional[httpx.AsyncBaseTransport] = httpx.AsyncHTTPTransport(retries=1),
        cookies: Optional[Union[Dict, httpx.Cookies]] = None,
        timeout=300.0,
        **kwargs
        ):
    if "hooks" in kwargs:
        hooks: Optional[Dict] = kwargs.pop("hooks")
    else:
        hooks: Optional[Dict] = None
        transport = None
    async with httpx.AsyncClient(
            event_hooks=hooks,
            transport=transport,
            cookies=cookies,
            ) as client:
        resp = await client.request(*args, timeout=timeout, **kwargs)
        return resp


async def get(
        *args,
        transport: Optional[httpx.AsyncBaseTransport] = httpx.AsyncHTTPTransport(retries=1),
        cookies: Optional[Union[Dict, httpx.Cookies]] = None,
        timeout=300.0,
        **kwargs
        ):
    if "hooks" in kwargs:
        hooks: Optional[Dict] = kwargs.pop("hooks")
    else:
        hooks: Optional[Dict] = None
        transport = None
    async with httpx.AsyncClient(
            event_hooks=hooks,
            transport=transport,
            cookies=cookies,
            ) as client:
        resp = await client.get(*args, timeout=timeout, **kwargs)
        return resp


async def post(
        *args,
        transport: Optional[httpx.AsyncBaseTransport] = httpx.AsyncHTTPTransport(retries=1),
        cookies: Optional[Union[Dict, httpx.Cookies]] = None,
        timeout=300.0,
        **kwargs
        ):
    if "hooks" in kwargs:
        hooks: Optional[Dict] = kwargs.pop("hooks")
    else:
        hooks: Optional[Dict] = None
        transport = None
    async with httpx.AsyncClient(
            event_hooks=hooks,
            transport=transport,
            cookies=cookies,
            ) as client:
        resp = await client.post(*args, timeout=timeout, **kwargs)
        return resp


async def put(
        *args,
        transport: Optional[httpx.AsyncBaseTransport] = httpx.AsyncHTTPTransport(retries=1),
        cookies: Optional[Union[Dict, httpx.Cookies]] = None,
        timeout=300.0,
        **kwargs
        ):
    if "hooks" in kwargs:
        hooks: Optional[Dict] = kwargs.pop("hooks")
    else:
        hooks: Optional[Dict] = None
        transport = None
    async with httpx.AsyncClient(
            event_hooks=hooks,
            transport=transport,
            cookies=cookies,
            ) as client:
        resp = await client.put(*args, timeout=timeout, **kwargs)
        return resp


async def delete(
        *args,
        transport: Optional[httpx.AsyncBaseTransport] = httpx.AsyncHTTPTransport(retries=1),
        cookies: Optional[Union[Dict, httpx.Cookies]] = None,
        timeout=300.0,
        **kwargs
        ):
    if "hooks" in kwargs:
        hooks: Optional[Dict] = kwargs.pop("hooks")
    else:
        hooks: Optional[Dict] = None
        transport = None
    async with httpx.AsyncClient(
            event_hooks=hooks,
            transport=transport,
            cookies=cookies,
            ) as client:
        resp = await client.delete(*args, timeout=timeout, **kwargs)
        return resp


async def head(
        *args,
        transport: Optional[httpx.AsyncBaseTransport] = httpx.AsyncHTTPTransport(retries=1),
        cookies: Optional[Union[Dict, httpx.Cookies]] = None,
        timeout=300.0,
        **kwargs
        ):
    if "hooks" in kwargs:
        hooks: Optional[Dict] = kwargs.pop("hooks")
    else:
        hooks: Optional[Dict] = None
        transport = None
    async with httpx.AsyncClient(
            event_hooks=hooks,
            transport=transport,
            cookies=cookies,
            ) as client:
        resp = await client.head(*args, timeout=timeout, **kwargs)
        return resp


async def patch(
        *args,
        transport: Optional[httpx.AsyncBaseTransport] = httpx.AsyncHTTPTransport(retries=1),
        cookies: Optional[Union[Dict, httpx.Cookies]] = None,
        timeout=300.0,
        **kwargs
        ):
    if "hooks" in kwargs:
        hooks: Optional[Dict] = kwargs.pop("hooks")
    else:
        hooks: Optional[Dict] = None
        transport = None
    async with httpx.AsyncClient(
            event_hooks=hooks,
            transport=transport,
            cookies=cookies,
            ) as client:
        resp = await client.patch(*args, timeout=timeout, **kwargs)
        return resp


async def options(
        *args,
        transport: Optional[httpx.AsyncBaseTransport] = httpx.AsyncHTTPTransport(retries=1),
        cookies: Optional[Union[Dict, httpx.Cookies]] = None,
        timeout=300.0,
        **kwargs
        ):
    if "hooks" in kwargs:
        hooks: Optional[Dict] = kwargs.pop("hooks")
    else:
        hooks: Optional[Dict] = None
        transport = None
    async with httpx.AsyncClient(
            event_hooks=hooks,
            transport=transport,
            cookies=cookies,
    ) as client:
        resp = await client.options(*args, timeout=timeout, **kwargs)
        return resp


async def stream(
        *args,
        transport: Optional[httpx.AsyncBaseTransport] = httpx.AsyncHTTPTransport(retries=1),
        cookies: Optional[Union[Dict, httpx.Cookies]] = None,
        timeout=300.0,
        **kwargs
        ):
    if "hooks" in kwargs:
        hooks: Optional[Dict] = kwargs.pop("hooks")
    else:
        hooks: Optional[Dict] = None
        transport = None
    async with httpx.AsyncClient(
            event_hooks=hooks,
            transport=transport,
            cookies=cookies,
            ) as client:
        resp = await client.stream(*args, timeout=timeout, **kwargs)
        return resp
