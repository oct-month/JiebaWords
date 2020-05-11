from typing import Dict, List

from config.common import STOP_WORDS
from .englishanaly import EnglishAnaly
from .jiebanaly import JiebAnaly


ANALY_TABLE = {
    'default': JiebAnaly,
    'jieba': JiebAnaly,
    'english': EnglishAnaly,
}


class AnalysisModule:
    def __init__(self, path: str, num: int=20, analys: str='default') -> None:
        self.path = path
        self.num = num
        tap = ANALY_TABLE.get(analys) or ANALY_TABLE.get('default')
        self.analy_mod = tap(self.path, STOP_WORDS)

    def analyse(self) -> Dict[str, float]:
        return self.analy_mod.analyse(self.num)
