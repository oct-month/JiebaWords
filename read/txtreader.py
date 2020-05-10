"""文本文件读取"""
from encode import EncodeModule
from .base import Base

class TxtReader(Base):
    def __init__(self, filepath: str) -> None:
        super().__init__(filepath)
        self.encoding = EncodeModule(filepath).get_encoding()

    def read_all(self) -> str:
        with open(self.filepath, 'r', encoding=self.encoding) as f:
            return f.read()


if __name__ == "__main__":
    a = TxtReader('test/test.txt')
    print(a.read_all())
