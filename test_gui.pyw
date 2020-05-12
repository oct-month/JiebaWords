import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

from gui import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('gui/icon.jpg'))
    c = MainWindow()
    c.add_source_list(*['http://www.chinadaily.com.cn/', 'https://www.androiddevtools.cn/', 'https://www.dytt8.net/html/gndy/index.html'])
    c.add_stop_list(*['stopwords/cn_stopwords.txt', 'stopwords/en_stopwords.txt'])
    c.show()
    sys.exit(app.exec_())
