"""pdf文件读取"""
from io import StringIO, open
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf

from .base import Base

class PdfReader(Base):
    def __init__(self, filepath: str) -> None:
        super().__init__(filepath)
    
    def read_all(self) -> str:
        if not self.content:
            with open(self.filepath, 'rb') as f:
                rsrcmgr = PDFResourceManager()
                retstr = StringIO()
                lapparams = LAParams()
                device = TextConverter(rsrcmgr, retstr, laparams=lapparams)
                process_pdf(rsrcmgr, device, f)
                self.content = retstr.getvalue() or ''
                device.close()
                retstr.close()
        return self.content


if __name__ == "__main__":
    f = PdfReader('test/test.pdf')
    print(f.read_all())
    
