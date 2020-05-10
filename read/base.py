import os.path
import abc

class Base(metaclass=abc.ABCMeta):
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath        # 文件路径
        self.encoding = 'utf-8'         # 编码方式
        self.content = ''               # 文件内容
        if not self.is_file():
            raise RuntimeError('普通文件' + filepath + '不存在')

    def get_path(self) -> str:
        return self.filepath

    def is_file(self) -> bool:
        return os.path.isfile(self.filepath)

    @abc.abstractmethod
    def read_all(self) -> str:
        pass
