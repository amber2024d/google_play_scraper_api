import ssl
from typing import Union
from urllib.error import HTTPError
from urllib.request import ProxyHandler, build_opener, install_opener
from urllib.request import Request, urlopen

import config
from google_play_scraper.exceptions import ExtraHTTPError, NotFoundError

ssl._create_default_https_context = ssl._create_unverified_context

if config.request_proxy:
    proxy_support = ProxyHandler(
        {
            'http': config.request_proxy,
            'https': config.request_proxy
        }
    )
    opener = build_opener(proxy_support)
    install_opener(opener)


def _urlopen(obj):
    try:
        resp = urlopen(obj)
    except HTTPError as e:
        if e.code == 404:
            raise NotFoundError("App not found(404).")
        else:
            raise ExtraHTTPError(
                "App not found. Status code {} returned.".format(e.code)
            )

    return resp.read().decode("UTF-8")


def post(url: str, data: Union[str, bytes], headers: dict) -> str:
    return _urlopen(Request(url, data=data, headers=headers))


def get(url: str) -> str:
    return _urlopen(url)
