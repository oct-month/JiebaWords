"""读文件模块"""
import os.path
from typing import Dict, List

from .htmlreader import HtmlReader
from .pdfreader import PdfReader
from .txtreader import TxtReader

__all__ = ['ReadModule', ]

# 文件类型注册表
READ_TABLE = {
    '.html': HtmlReader,
    '.pdf': PdfReader,
    'default': TxtReader,
}


class ReadModule:
    """对外接口（外观模式）"""
    def __init__(self, paths: List[str]):
        self.paths = paths
        self.content = ''
        
    def __get_content(self):
        for path in self.paths:
            exten_name = os.path.splitext(path)[1]
            mod = READ_TABLE.get(exten_name, None)    
            mod = mod or READ_TABLE.get('default')
            self.content += mod(path).read_all() + '\r\n'

    def get_result(self):
        """获取所有文字"""
        self.__get_content()
        return self.content

    