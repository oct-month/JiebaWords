from typing import Optional
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QDragEnterEvent, QDropEvent, QDragMoveEvent
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
