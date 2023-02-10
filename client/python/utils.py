from typing import Dict, Union, List
import ast
from pathlib import Path

from httpx import URL


__all__ = [
    "joinpaths",
    "build_url",
    "decode_cellmsg",
]


def joinpaths(*paths: str) -> str:
    path0, *subpaths = paths
    return Path(path0).joinpath(*[p.lstrip("/") for p in subpaths]).as_posix()

def build_url(url: URL, *paths: str, **kwargs) -> URL:
    # scheme = url.scheme
    # domain = url.netloc.decode()
    # default_path = url.path
    # return URL(
    #     url=domain,
    #     scheme=scheme,
    #     path=joinpaths(default_path, *paths),
    # )
    return URL(
        url,
        path=joinpaths(url.path, *paths),
        **kwargs,
    )


def decode_cellmsg(res: Union[str, List[str]]):
    if isinstance(res, str):
        res = [res]
    msg = ["\n".join(m) if isinstance(m, list) else m for m in res]
    # msg = [ast.literal_eval(f"b'''{m}'''").decode() for m in res]
    return '\n'.join(msg)
    # return msg