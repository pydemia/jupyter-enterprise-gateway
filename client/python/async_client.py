from typing import Dict, Optional, Union, Tuple
import httpx
from urllib.parse import parse_qs, urlparse
import json


async def request(
        *args,
        transport: Optional[httpx.AsyncBaseTransport] = httpx.AsyncHTTPTransport(retries=1),
        cookies: Optional[Union[Dict, httpx.Cookies]] = None,
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
        resp = await client.request(*args, **kwargs)
        return resp


async def get(
        *args,
        transport: Optional[httpx.AsyncBaseTransport] = httpx.AsyncHTTPTransport(retries=1),
        cookies: Optional[Union[Dict, httpx.Cookies]] = None,
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
        resp = await client.get(*args, **kwargs)
        return resp


async def post(
        *args,
        transport: Optional[httpx.AsyncBaseTransport] = httpx.AsyncHTTPTransport(retries=1),
        cookies: Optional[Union[Dict, httpx.Cookies]] = None,
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
        resp = await client.post(*args, **kwargs)
        return resp


async def put(
        *args,
        transport: Optional[httpx.AsyncBaseTransport] = httpx.AsyncHTTPTransport(retries=1),
        cookies: Optional[Union[Dict, httpx.Cookies]] = None,
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
        resp = await client.put(*args, **kwargs)
        return resp


async def delete(
        *args,
        transport: Optional[httpx.AsyncBaseTransport] = httpx.AsyncHTTPTransport(retries=1),
        cookies: Optional[Union[Dict, httpx.Cookies]] = None,
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
        resp = await client.delete(*args, **kwargs)
        return resp


async def head(
        *args,
        transport: Optional[httpx.AsyncBaseTransport] = httpx.AsyncHTTPTransport(retries=1),
        cookies: Optional[Union[Dict, httpx.Cookies]] = None,
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
        resp = await client.head(*args, **kwargs)
        return resp


async def patch(
        *args,
        transport: Optional[httpx.AsyncBaseTransport] = httpx.AsyncHTTPTransport(retries=1),
        cookies: Optional[Union[Dict, httpx.Cookies]] = None,
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
        resp = await client.patch(*args, **kwargs)
        return resp


async def options(
        *args,
        transport: Optional[httpx.AsyncBaseTransport] = httpx.AsyncHTTPTransport(retries=1),
        cookies: Optional[Union[Dict, httpx.Cookies]] = None,
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
        resp = await client.options(*args, **kwargs)
        return resp


async def stream(
        *args,
        transport: Optional[httpx.AsyncBaseTransport] = httpx.AsyncHTTPTransport(retries=1),
        cookies: Optional[Union[Dict, httpx.Cookies]] = None,
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
        resp = await client.stream(*args, **kwargs)
        return resp
