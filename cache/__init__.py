"""cache模块"""
import os
import shutil
from hashlib import md5

from config.common import CACHE_PATH, ENCODING


class CacheModule:
    
    @classmethod
    def __ensure_cache(cls) -> None:
        """确保cache目录存在"""
        if not os.path.exists(CACHE_PATH):
            if os.path.isfile(CACHE_PATH):
                os.remove(CACHE_PATH)
            os.mkdir(CACHE_PATH)

    @classmethod
    def make_cache(cls, content: str, typename: str) -> str:
        """建立cache，返回路径"""
        cls.__ensure_cache()
        filepath = CACHE_PATH + md5(content.encode()).hexdigest() + '.' + typename
        with open(filepath, 'w', encoding=ENCODING) as f:
            f.write(content)
        return filepath

    @classmethod
    def clear_cache(cls) -> None:
        if os.path.exists(CACHE_PATH):
            shutil.rmtree(CACHE_PATH)
