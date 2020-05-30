"""将传入的path全部读取"""
import os.path
from typing import Dict, List

from cache import CacheModule
from .htmlreader import HtmlReader
from .pdfreader import PdfReader
from .txtreader import TxtReader
from .wordreader import WordReader

__all__ = ['ReadModule', ]

# 文件类型注册表
READ_TABLE = {
    'default': TxtReader,
    '.html': HtmlReader,
    '.pdf': PdfReader,
    '.doc': WordReader,
    'docx': WordReader,
}


class ReadModule:
    """对外接口（外观模式）"""
    def __init__(self, paths: List[str]) -> None:
        self.paths = paths
        self.content = ''
        
    def __get_content(self) -> None:
        for path in self.paths:
            exten_name = os.path.splitext(path)[1]
            mod = READ_TABLE.get(exten_name, None)    
            mod = mod or READ_TABLE.get('default')
            try:
                tap = mod(path).read_all()
            except Exception as e:
                tap = ''
                print(path + " 文件编码格式不明确")
            self.content += tap + '\r\n'

    def read_all(self) -> str:
        """获取所有文字"""
        self.__get_content()
        path = CacheModule.make_cache(self.content, 'txt')
        return path


