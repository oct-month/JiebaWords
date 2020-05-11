import os

from read import ReadModule
from initial import InitialModule
from analysis import AnalysisModule
from cache import CacheModule

def test_read():
    a = ['ttt', 'http://www.chinadaily.com.cn/']
    a = InitialModule(a).init_paths()
    content = ReadModule(a).get_result()
    print(content)
    result = AnalysisModule(content).analyse()
    print(result)
    n = 0
    for i in result.values():
        n += i
    print(n)

if __name__ == "__main__":
    a = ['http://www.chinadaily.com.cn/', 'https://www.androiddevtools.cn/', 'https://www.dytt8.net/html/gndy/index.html']
    a = InitialModule(a).init_paths()
    path = ReadModule(a).read_all()
    stoppaths = ['stopwords/'+i for i in os.listdir('stopwords')]
    result = AnalysisModule(path, 30).analyse()
    print(result)
    CacheModule.clear_cache()


