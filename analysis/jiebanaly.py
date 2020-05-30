"""使用jieba引擎分析词频"""
from typing import Dict
from jieba.analyse import extract_tags, set_stop_words

from config import ENCODING
from .base import Base


class JiebAnaly(Base):
    def __init__(self, path: str, stopwords_path: str) -> None:
        self.path = path
        self.set_stopwords(stopwords_path)

    def set_stopwords(self, stopwords_path: str) -> None:
        set_stop_words(stopwords_path)

    def analyse(self, num: int=20) -> Dict[str, float]:
        with open(self.path, 'r', encoding=ENCODING) as f:
            content = f.read()
            if num > 0:
                result = extract_tags(content, topK=num, withWeight=True)
            else:
                result = extract_tags(content, topK=None, withWeight=True)[num:]
            return dict(result)

