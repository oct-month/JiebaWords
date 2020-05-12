import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtCore import Qt
from time import sleep

from gui.splash import MyQSplashScreen

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('gui/img/icon.jpg'))
    
    main = QMainWindow()
    with MyQSplashScreen():
        sleep(10)
    main.show()

    sys.exit(app.exec_())
