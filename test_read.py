from read import ReadModule
from initial import InitialModule

def test_read():
    a = ['test/test.html', 'test/test.pdf', 'test/test.py', 'http://www.chinadaily.com.cn/']
    a = InitialModule(a).init_paths()
    content = ReadModule(a).get_result()
    print(content)


if __name__ == "__main__":
    test_read()

