# -*- coding: utf-8 -*-
# @Time    : 2023/10/11 下午3:34
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from typing import Optional

from loguru import logger

from .schema import Chain
from ...sdk.cache.redis import cache
from ...task import TaskHeader


class AuthReloader(object):
    """
    任务链条认证
    """

    def __init__(self, uid: str = None):
        self.uid = uid

    @classmethod
    def from_meta(cls, platform: str, user_id: str):
        _c = cls()
        _c.uid = f"{platform}:{user_id}"
        return _c

    async def add_auth(self, chain: Chain):
        _cache = await cache.set_data(key=f"auth:{chain.uuid}", value=chain.model_dump_json(), timeout=60 * 60 * 24 * 7)
        return chain.uuid

    async def get_auth(self, uuid: str) -> Optional[Chain]:
        _cache = await cache.read_data(key=f"auth:{uuid}")
        logger.debug(f"[x] Auth \n--data {_cache}")
        if not _cache:
            logger.debug(f"[x] Auth \n--empty {uuid}")
            return None
        chain = Chain().from_redis(_cache)
        if chain.is_expire:
            logger.debug(f"[x] Auth \n--expire {uuid}")
            return None
        chain = chain.format_arg(arg=TaskHeader)
        if chain.uid != self.uid:
            logger.debug(f"[x] Auth \n--not found user {uuid}")
            return None
        return chain


class ChainReloader(object):

    def __init__(self, uid: str):
        self.uid = uid

    async def add_task(self, chain: Chain):
        _cache = await cache.lpush_data(key=f"chain:{self.uid}", value=chain.model_dump_json())
        return chain.uuid

    async def get_task(self) -> Optional[Chain]:
        _data = await cache.lpop_data(key=f"chain:{self.uid}")
        if not _data:
            return None
        chain = Chain.from_redis(_data)
        if chain.is_expire:
            return None
        chain = chain.format_arg(arg=TaskHeader)
        return chain
