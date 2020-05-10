from chardet import detect

class EncodeModule:
    def __init__(self, path: str) -> None:
        self.path = path
    
    def get_encoding(self) -> str:
        with open(self.path, 'rb') as f:
            data = f.read()
            encoding = detect(data).get('encoding', 'utf-8')
            if encoding == 'GB2312' or encoding == 'gb2312':
                encoding = 'gbk'
            else:
                encoding = 'utf-8'
            return encoding

