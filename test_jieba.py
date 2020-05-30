from jieba.analyse import extract_tags
from encode import EncodeModule

path = 'test/test.txt'

with open(path, 'r', encoding=EncodeModule(path).get_encoding()) as f:
    content = f.read()
    result = extract_tags(content, topK=0, withWeight=True)
    print(result[:10])
    print(result[-10:])


