"""初步处理传入的path列"""
from typing import List

from .urlinit import UrlInit
from .fileinit import FileInit

__all__ = ['InitialModule', ]

# 初步处理要用的部件集
INIT_LIST = [UrlInit, FileInit, ]


class InitialModule:
    def __init__(self, paths: List[str]) -> None:
        self.paths = paths
    
    def init_paths(self) -> List[str]:
        for init in INIT_LIST:
            self.paths = init(self.paths).init_paths()
        return self.paths



