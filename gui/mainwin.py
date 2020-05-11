from typing import List
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap

from analysis import ANALY_TABLE, AnalysisModule
from initial import InitialModule
from read import ReadModule
from stopwords import StopWords
from .win import Ui_MainWindow
from .echart import EchartsMake

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.source_list: List[str] = []    # source列表
        self.stop_list: List[str] = []      # stop列表
        self.analy_set = 'default'          # 引擎选择
        self.num_set = 20                   # 选词数量
        self.graphics_path = ''             # 图片路径
    
        self.ui.setupUi(self)
        self.ui.analy_set.addItems(ANALY_TABLE.keys())          # 添加引擎项
        self.ui.action_btn.clicked.connect(self.action)
        self.ui.export_txt.clicked.connect(self.export_txt)
        self.ui.export_png.clicked.connect(self.export_png)
        self.ui.export_html.clicked.connect(self.export_html)
        self.ui.graphics_view.setScaledContents(True)           # 设置图片自适应
        

    def add_source_list(self, *item: str) -> None:
        """向source列表中添加项"""
        self.ui.source_list.addItems(item)
        self.source_list.extend(item)
    
    def get_source_list(self) -> List[str]:
        return self.source_list
    
    def add_stop_list(self, *item: str) -> None:
        """向stop列表中添加项"""
        self.ui.stop_list.addItems(item)
        self.stop_list.extend(item)
    
    def get_stop_list(self) -> List[str]:
        return self.stop_list

    def get_analy_set(self) -> str:
        return self.ui.analy_set.currentText()

    def get_num_set(self) -> int:
        return int(self.ui.num_set.value())

    def action(self) -> None:
        source_list = self.get_source_list()
        stop_list = self.get_stop_list()
        analy_set = self.get_analy_set()
        num_set = self.get_num_set()

        source_list = InitialModule(source_list).init_paths()
        path = ReadModule(source_list).read_all()
        stop_list = InitialModule(stop_list).init_paths()
        StopWords.set_stopwords(stop_list)
        result = AnalysisModule(path, num_set, analy_set).analyse()

        echart = EchartsMake(result)
        img_path = echart.render_img()
        self.set_graphics_path(img_path)

    def set_graphics_path(self, path: str) -> None:
        """更新图片"""
        self.graphics_path = path
        self.ui.graphics_view.setPixmap(QPixmap(path))

    def export_txt(self) -> None:
        pass

    def export_png(self) -> None:
        pass

    def export_html(self) -> None:
        pass



# ui = Ui_MainWindow()
# # 输入
# ui.source_list
# ui.stop_list
# # 设定
# ui.analy_set
# ui.num_set

# # 操作
# ui.export_txt
# ui.export_png
# ui.export_html

# # 图像展示
# ui.graphics_view
# ui.action
