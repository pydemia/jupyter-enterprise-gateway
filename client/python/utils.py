from typing import Dict
from httpx import URL
from pathlib import Path


__all__ = [
    "joinpaths",
    "build_url",
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