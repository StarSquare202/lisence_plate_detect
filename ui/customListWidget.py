import os
from PySide6.QtWidgets import QListWidget, QAbstractItemView
from PySide6.QtGui import QDropEvent, QDragEnterEvent, QDragMoveEvent

class CustomListWidget(QListWidget):
    def __init__(self, type, parent=None):
        super(CustomListWidget, self).__init__(parent)
        self.acceptDrops()
        self.DragDropMode(QAbstractItemView.DragDropMode.DropOnly)
    
    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        try:
            if event.mimeData().hasUrls():
                event.accept()
            else:
                event.ignore()
        except Exception as e:
            event.ignore()

    def dragMoveEvent(self, event: QDragMoveEvent) -> None:
        try:
            if event.mimeData().hasUrls():
                event.accept()
            else:
                event.ignore()
        except Exception as e:
            event.ignore()

    def dropEvent(self, event: QDropEvent) -> None:
        try:
            if event.mimeData().hasUrls():
                event.accept()
                for url in [x.toString().replace('file:///', '') for x in event.mimeData().urls() if x.toString().lower().endswith(('.jpg','.jpeg','.png'))]:
                    self.addItem(url)
            else:
                event.ignore()
        except Exception as e:
            event.ignore()

    def get_items(self) -> list[str]:
        return [self.item(i).text() for i in range(self.count())]
            