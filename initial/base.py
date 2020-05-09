import abc
from typing import List

class Base(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, paths: List[str]) -> None:
        pass

    @abc.abstractmethod
    def init_paths(self) -> List[str]:
        pass

