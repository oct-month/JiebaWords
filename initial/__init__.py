"""初步处理传入的path列"""
from typing import List

from .urlinit import UrlInit

__all__ = ['InitialModule', ]

# 初步处理要用的部件集
INIT_LIST = [UrlInit, ]


class InitialModule:
    def __init__(self, *paths: str) -> None:
        self.paths = paths
    
    def init_paths(self):
        for init in INIT_LIST:
            self.paths = init(self.paths).init_paths()
        return self.paths

