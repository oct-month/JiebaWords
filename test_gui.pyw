import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

from gui import MainWindow
from config import STOP_WORDS_INIT

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('gui/img/icon.jpg'))
    c = MainWindow()
    c.add_source_list(*['http://www.chinadaily.com.cn/', 'https://www.androiddevtools.cn/', 'https://www.dytt8.net/html/gndy/index.html'])
    c.add_stop_list(*STOP_WORDS_INIT)
    c.show()
    
    sys.exit(app.exec_())
