"""加载框"""
from typing import Optional
from PyQt5.QtWidgets import QSplashScreen, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QMovie

class MyQSplashScreen(QSplashScreen):
    def __init__(self, parent: Optional[QWidget]=None, img_path: str='gui/img/loading.png') -> None:
        super().__init__(parent, QPixmap(img_path))
        # self.img_path = img_path
    
    def __enter__(self) -> None:
        self.show()
        self.showMessage('')

    def __exit__(self, *_) -> None:
        self.close()
