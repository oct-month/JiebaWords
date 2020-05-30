""".doc .docx 文件读取"""
from docx import Document

from .base import Base

class WordReader(Base):
    def __init__(self, filepath: str) -> None:
        super().__init__(filepath)
    
    def read_all(self) -> str:
        doc = Document(self.filepath)
        return '\n'.join([p.text for p in doc.paragraphs])
        

if __name__ == "__main__":
    print(WordReader('test/test.docx').read_all())
