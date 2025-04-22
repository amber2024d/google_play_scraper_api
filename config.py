# coding=utf-8
import os

from dotenv import load_dotenv

load_dotenv(override=True)

port: int = int(os.getenv('PORT', default=8081))

request_proxy: str = os.getenv('REQUEST_PROXY', default=None)
