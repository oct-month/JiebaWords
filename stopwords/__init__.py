from typing import List

from config import STOP_WORDS, ENCODING
from encode import EncodeModule


class StopWords:
    """写入stopwords文件"""
    @classmethod
    def set_stopwords(cls, paths: List[str]) -> None:
        with open(STOP_WORDS,'w', encoding=ENCODING ) as f:
            for path in paths:
                with open(path, 'r', encoding=EncodeModule(path).get_encoding()) as t:
                    content = t.read()
                    f.write(content)

