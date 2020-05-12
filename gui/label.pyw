from typing import Optional
from PyQt5.QtWidgets import QWidget, QLabel, QDialog, QVBoxLayout
from PyQt5.QtGui import QDragEnterEvent, QDropEvent, QDragMoveEvent, QMouseEvent, QPixmap
from PyQt5.QtCore import Qt


class MyLabel(QLabel):
    """可接收拖拽的Label"""
    def __init__(self, parent: Optional[QWidget]=None) -> None:
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e: QDragEnterEvent) -> None:
        e.setDropAction(Qt.MoveAction)
        e.accept()

    # def dragMoveEvent(self, e: QDragMoveEvent) -> None:
    #     e.setDropAction(Qt.MoveAction)
    #     e.accept()

    def dropEvent(self, e: QDropEvent) -> None:
        e.setDropAction(Qt.MoveAction)
        e.accept()

class CliLabel(QLabel):
    """单击放大图片的label"""
    def __init__(self, parent: Optional[QWidget]=None) -> None:
        super().__init__(parent)
        self.img_path = ''
    
    def mousePressEvent(self, e: QMouseEvent) -> None:
        if self.img_path:
            dialog = QDialog(self)
            dialog.setWindowTitle('详情')
            dialog.setWindowModality(Qt.ApplicationModal)   # 屏蔽主窗口
            layout = QVBoxLayout()
            label = QLabel()
            label.setPixmap(QPixmap(self.img_path))
            layout.addWidget(label)
            dialog.setLayout(layout)
            dialog.exec_()

