"""自己写的引擎分析英文单词"""
from typing import Dict, List
from collections import defaultdict
import re

from .base import Base


class EnglishAnaly(Base):
    def __init__(self, path: str, stopwords_path: str) -> None:
        self.path: str = path
        self.stopwords: List[str] = ['']
        self.result: Dict[str, float] = defaultdict(int)
        self.set_stopwords(stopwords_path)

    def set_stopwords(self, stopwords_path: str) -> None:
        with open(stopwords_path, 'r', encoding='utf-8') as f:
            self.stopwords.extend(f.readlines())

    def analyse(self, num: int=20) -> Dict[str, float]:
        with open(self.path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                tap = re.split(r'[\W\s]+', line, flags=re.I)
                for i in tap:
                    if i not in self.stopwords:
                        self.result[i] += 1
        words = list(self.result.items())
        words = sorted(words, key=lambda x: x[-1], reverse=True)
        return dict(words[:num])

