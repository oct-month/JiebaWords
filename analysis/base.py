import abc
from typing import Dict

class Base(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, path: str) -> None:
        pass

    @abc.abstractmethod
    def analyse(self, num: int) -> Dict[str, float]:
        pass

    @abc.abstractmethod
    def set_stopwords(self, stopwords_path: str) -> None:
        pass
