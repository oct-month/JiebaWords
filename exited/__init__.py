"""程序退出时要执行的动作"""
import asyncio

from cache import CacheModule

def exit_do():
    CacheModule.clear_cache()
    loop = asyncio.get_event_loop()
    loop.close()

