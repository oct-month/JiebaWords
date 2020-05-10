"""过滤path中无用路径，path中的dir被迭代替换成file"""
from typing import List
import os

from .base import Base

class FileInit(Base):
    def __init__(self, paths: List[str]) -> None:
        self.paths: List[str] = paths
        self.taps: List[str] = []
    
    def __get_dirfile(self, dirpath: str):
        """递归遍历目录"""
        for lists in os.listdir(dirpath):
            sub_path = os.path.join(dirpath, lists)
            if os.path.isfile(sub_path):
                if sub_path not in self.taps:
                    self.taps.append(sub_path)
            elif os.path.isdir(sub_path):
                self.__get_dirfile(sub_path)

    def init_paths(self) -> List[str]:
        for path in self.paths:
            if os.path.isfile(path):
                if path not in self.taps:
                    self.taps.append(path)
            elif os.path.isdir(path):
                self.__get_dirfile(path)
        return self.taps

