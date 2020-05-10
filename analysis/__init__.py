from typing import Dict

from .englishanaly import EnglishAnaly
from .jiebanaly import JiebAnaly


ANALY_TABLE = {
    'jieba': JiebAnaly,
    'english': EnglishAnaly,
    'default': JiebAnaly
}

class AnalysisModule:
    def __init__(self, path: str, num: int=20, analys: str='default') -> None:
        self.path = path
        self.num = num
        self.analy_mod = ANALY_TABLE.get(analys) or ANALY_TABLE.get('default')

    def analyse(self) -> Dict[str, float]:
        return self.analy_mod(self.path).analyse(self.num)
