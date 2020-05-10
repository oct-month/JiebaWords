from jieba import set_dictionary
from jieba.analyse import extract_tags, set_stop_words

STOP_WORDS = 'stopwords/all_stopwords.txt'

class JiebAnaly:
    def __init__(self, path: str) -> None:
        self.path = path
        set_stop_words(STOP_WORDS)

    def analyse(self, num: int=20) -> dict:
        with open(self.path) as f:
            content = f.read()
            result = extract_tags(content, topK=num, withWeight=True)
            return dict(result)

