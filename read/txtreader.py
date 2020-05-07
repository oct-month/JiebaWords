from reader import Reader

class TxtReader(Reader):
    def __init__(self, filepath: str, encoding: str='utf-8') -> None:
        super().__init__(filepath)
        self.encoding = encoding

    def read_all(self) -> str:
        with open(self.filepath, 'r', encoding=self.encoding) as f:
            return f.read()


if __name__ == "__main__":
    a = TxtReader('test/test.txt')
    print(a.read_all())
