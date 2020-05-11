from typing import Optional
from PyQt5.QtWidgets import QListWidget, QWidget, QAbstractItemView, QApplication
from PyQt5.QtGui import QDragEnterEvent, QDropEvent, QDragMoveEvent, QMouseEvent
from PyQt5.QtCore import Qt

class MyQListWidget(QListWidget):
    """支持拖拽的QListWidget"""
    def __init__(self, parent: Optional[QWidget]=None) -> None:
        super().__init__(parent)
        self.last_pos = None
        self.mouse_item = None

        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropOverwriteMode(False)
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setDefaultDropAction(Qt.MoveAction)

    def dragEnterEvent(self, e: QDragEnterEvent) -> None:
        if e.mimeData().hasText():
            if e.mimeData().text().startswith('file:///'):
                e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e: QDragMoveEvent) -> None:
        e.accept()

    def dropEvent(self, e: QDropEvent) -> None:
        self.addItem(e.mimeData().text()[8:])
