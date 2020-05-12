import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from gui import MainWindow

from config import STOP_WORDS_INIT, TITLE_ICON
from gui import MyQSplashScreen
from exited import exit_do


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(TITLE_ICON))
    
    with MyQSplashScreen(img_path=TITLE_ICON):
        c = MainWindow()
        c.add_stop_list(*STOP_WORDS_INIT)
        c.show()
    
    app.exec_()
    exit_do()
