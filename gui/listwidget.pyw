from typing import Optional
from PyQt5.QtWidgets import QListWidget, QWidget, QAbstractItemView, QListWidgetItem
from PyQt5.QtGui import QDragEnterEvent, QDropEvent, QDragMoveEvent
from PyQt5.QtCore import Qt, QModelIndex

class MyQListWidget(QListWidget):
    """支持拖拽的QListWidget"""
    def __init__(self, parent: Optional[QWidget]=None) -> None:
        super().__init__(parent)
        # 拖拽设置
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setDefaultDropAction(Qt.MoveAction)
        # 双击可编辑
        self.edited_item = self.currentItem()
        self.doubleClicked.connect(self.item_double_clicked)
        self.currentItemChanged.connect(self.close_edit)
    
    
    def item_double_clicked(self, modelindex: QModelIndex) -> None:
        item = self.item(modelindex.row())
        self.edited_item = item
        self.openPersistentEditor(item)
        self.editItem(item)
    
    def close_edit(self, item: QListWidgetItem) -> None:
        if self.edited_item and self.isPersistentEditorOpen(self.edited_item):
            self.closePersistentEditor(self.edited_item)

    def dragEnterEvent(self, e: QDragEnterEvent) -> None:
        # print(e.mimeData().text())
        if e.mimeData().hasText():
            if e.mimeData().text().startswith('file:///'):
                e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e: QDragMoveEvent) -> None:
        e.accept()

    def dropEvent(self, e: QDropEvent) -> None:
        paths = e.mimeData().text().split('\n')
        for path in paths:
            path = path.strip()
            if len(path) > 8:
                self.addItem(path.strip()[8:])

