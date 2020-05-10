from read import ReadModule
from initial import InitialModule
from analysis.jiebanaly import JiebAnaly

def test_read():
    a = ['test', 'http://www.chinadaily.com.cn/']
    a = InitialModule(a).init_paths()
    content = ReadModule(a).get_result()
    print(content)
    result = JiebAnaly(content).analyse()
    print(result)
    n = 0
    for i in result.values():
        n += i
    print(n)

if __name__ == "__main__":
    test_read()

