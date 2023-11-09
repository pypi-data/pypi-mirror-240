# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import time
import asyncio
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._client import Finch, AsyncFinch


class SyncAPIResource:
    _client: Finch

    def __init__(self, client: Finch) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete
        self._get_api_list = client.get_api_list

    def _sleep(self, seconds: float) -> None:
        time.sleep(seconds)


class AsyncAPIResource:
    _client: AsyncFinch

    def __init__(self, client: AsyncFinch) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete
        self._get_api_list = client.get_api_list

    async def _sleep(self, seconds: float) -> None:
        await asyncio.sleep(seconds)
