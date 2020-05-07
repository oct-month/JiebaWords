from bs4 import BeautifulSoup
import re

from reader import Reader

class HtmlReader(Reader):
    def __init__(self, filepath: str) -> None:
        super().__init__(filepath)
    
    def read_all(self) -> str:
        with open(self.filepath, 'r') as f:
            tap = BeautifulSoup(f, 'lxml')
            self.content = tap.prettify()
            return self.do_filter()
            
    def do_filter(self) -> str:
        """过滤html中无用的部分"""
        self.content = re.sub(r'<script.*?>.*?</script>', '', self.content, flags=re.S | re.I)
        self.content = re.sub(r'<style>.*?</style>', '', self.content, flags=re.S | re.I)
        self.content = re.sub(r'<.*?>', '', self.content, flags=re.S | re.I)
        self.content = re.sub(r'(\s){2,}', r'\1', self.content, flags=re.S | re.I)
        return self.content


if __name__ == "__main__":
    a = HtmlReader('test/test.html')
    print(a.read_all())
