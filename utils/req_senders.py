import asyncio
import functools
from asyncio import sleep
from random import choice
import aiohttp
import anyio
import httpx
from aiohttp import client_exceptions


async def send_req(req_obj: functools.partial, num_tries: int = 5) -> \
        httpx.Response | aiohttp.ClientResponse | None:
    """
    Central Request Handler. All requests should go through this.
    :param num_tries:
    :param req_obj:
    :return:
    """
    for _ in range(num_tries):
        try:
            item = await req_obj()
            return item
        except (
                # httpx errors
                httpx.ConnectTimeout, httpx.ProxyError, httpx.ConnectError,
                httpx.ReadError, httpx.ReadTimeout, httpx.WriteTimeout, httpx.RemoteProtocolError,

                # aiohttp errors
                asyncio.exceptions.TimeoutError, client_exceptions.ClientHttpProxyError,
                client_exceptions.ClientProxyConnectionError,
                client_exceptions.ClientOSError,
                client_exceptions.ServerDisconnectedError,

                # any io errors
                anyio.ClosedResourceError
                ) as e:
            print(e)
            await sleep(2)
    return
