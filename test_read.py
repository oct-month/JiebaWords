from read import ReadModule
from initial import InitialModule

def test_read():
    a = ['test/', 'http://www.chinadaily.com.cn/']
    a = InitialModule(a).init_paths()
    content = ReadModule(a).get_result()
    print(content)


if __name__ == "__main__":
    test_read()

