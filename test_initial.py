from initial import InitialModule


def test_initial():
    a = ['test', 'test.pdf', 'test.txt', 'test.py', 'http://baidu.com']
    tap = InitialModule(a).init_paths()
    print(tap)

if __name__ == "__main__":
    test_initial()

