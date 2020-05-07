import asyncio
import aiohttp
import os
from hashlib import md5

from reader import Reader
from htmlreader import HtmlReader

class UrlReader(Reader):
    def __init__(self, url: str, session: aiohttp.ClientSession) -> None:
        super().__init__(url, check=False)
        self.url = url
        self.session = session
    
    async def __fetch_html(self) -> None:
        """发起get请求"""
        async with asyncio.Semaphore(20):
            async with self.session.get(self.url) as resp:
                if resp.status in (200, 201):
                    self.content = await resp.text()

    def __ensure_cache(self) -> None:
        """确保cache目录存在"""
        name = 'cache'
        if not os.path.exists(name):
            if os.path.isfile(name):
                os.remove(name)
            os.mkdir(name)

    async def __get_conent(self) -> None:
        """建立cache缓存文件"""
        await self.__fetch_html()
        self.__ensure_cache()
        filepath = 'cache' + os.path.sep + md5(self.url.encode()).hexdigest() + '.html'
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(self.content)
            self.filepath = filepath

    async def read_all(self) -> str:
        await self.__get_conent()
        tap = HtmlReader(self.filepath)
        return tap.read_all()


if __name__ == "__main__":
    async def main():
        async with aiohttp.ClientSession() as session:
            u = UrlReader('https://www.runoob.com/regexp/regexp-syntax.html', session)
            print(await u.read_all())

    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(main())
    tasks = [task, ]
    loop.run_until_complete(asyncio.wait(tasks))

    

