import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

from gui.win import Ui_MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('gui/icon.jpg'))
    main_win = QMainWindow()
    ui = Ui_MainWindow()
    
    ui.setupUi(main_win)
    main_win.show()
    sys.exit(app.exec_())
