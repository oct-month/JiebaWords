from read import ReadModule
from initial import InitialModule
from analysis import AnalysisModule

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
    a = ['test', 'http://www.chinadaily.com.cn/', 'https://www.androiddevtools.cn/', 'https://www.dytt8.net/html/gndy/index.html']
    a = InitialModule(a).init_paths()
    path = ReadModule(a).read_all()
    result = AnalysisModule(path, 30).analyse()
    print(result)
