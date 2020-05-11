from typing import Dict, List

from .englishanaly import EnglishAnaly
from .jiebanaly import JiebAnaly


ANALY_TABLE = {
    'jieba': JiebAnaly,
    'english': EnglishAnaly,
    'default': JiebAnaly
}

STOP_WORDS = 'stopwords/use.txt'

class AnalysisModule:
    def __init__(self, path: str, num: int=20, analys: str='default') -> None:
        self.path = path
        self.num = num
        self.analy_mod = ANALY_TABLE.get(analys) or ANALY_TABLE.get('default')

    def analyse(self) -> Dict[str, float]:
        return self.analy_mod(self.path, STOP_WORDS).analyse(self.num)
