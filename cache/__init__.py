"""cache模块"""
import os
from hashlib import md5

CACHE_PATH = 'cache' + os.path.sep + 'files' + os.path.sep
ENCODING = 'utf-8'

class CacheModule:
    name = CACHE_PATH
    
    @classmethod
    def __ensure_cache(cls) -> None:
        """确保cache目录存在"""
        if not os.path.exists(cls.name):
            if os.path.isfile(cls.name):
                os.remove(cls.name)
            os.mkdir(cls.name)

    @classmethod
    def make_cache(cls, content: str, typename: str) -> str:
        """建立cache，返回路径"""
        cls.__ensure_cache()
        filepath = cls.name + md5(content.encode()).hexdigest() + '.' + typename
        with open(filepath, 'w', encoding=ENCODING) as f:
            f.write(content)
        return filepath
