"""把path中的url换成cache目录的路径"""
import asyncio
import aiohttp
from typing import List

from .base import Base
from cache import CacheModule

__all__ = ['UrlInit', ]


class UrlGet:
    def __init__(self, url: str, session: aiohttp.ClientSession) -> None:
        self.url = url
        self.session = session
    
    async def __fetch_html(self) -> None:
        """发起get请求"""
        async with asyncio.Semaphore(20):
            async with self.session.get(self.url) as resp:
                if resp.status in (200, 201):
                    self.content = await resp.text()

    async def __get_conent(self) -> None:
        """建立cache缓存文件"""
        await self.__fetch_html()
        self.filepath = CacheModule.make_cache(self.content, 'html')

    async def get_path(self) -> str:
        await self.__get_conent()
        return self.filepath


class UrlInit(Base):
    def __init__(self, paths: List[str]) -> None:
        self.paths = paths
    
    def __is_url(self, path: str) -> bool:
        """判断字符串是否是url"""
        if not path.startswith(('http://', 'https://', 'www.')):
            return False
        return True

    async def __get_paths(self) -> None:
        """更新paths中的url为cache文件位置"""
        async with aiohttp.ClientSession() as session:
            for i, url in enumerate(self.paths):
                if self.__is_url(url):
                    self.paths[i] = await UrlGet(url, session).get_path()
    
    def init_paths(self) -> List[str]:
        loop = asyncio.get_event_loop()
        task = asyncio.ensure_future(self.__get_paths())
        loop.run_until_complete(task)
        return self.paths

