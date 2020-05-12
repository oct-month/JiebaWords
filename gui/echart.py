"""echarts模块"""
from typing import Dict
import os
import sys
from pyecharts.charts import Pie
from pyecharts.options import TitleOpts, InitOpts
from pyecharts.globals import ThemeType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

from cache import CacheModule
# from config import LINUX_PATH, WIN32_PATH, MAC_PATH

class EchartsMake:
    def __init__(self, result: Dict[str, float]) -> None:
        self.result = result
        self.htmlpath = ''
        self.imgpath = ''
    
    def render_img(self) -> str:
        """渲染图片"""
        # if sys.platform == 'linux':
        #     os.environ['PATH'] = LINUX_PATH
        # elif sys.platform == 'win32':
        #     os.environ['PATH'] = WIN32_PATH
        # else:
        #     os.environ['PATH'] = MAC_PATH
        img = CacheModule.create_cache_path('png')
        if self.htmlpath == '':
            self.render_html()
        make_snapshot(snapshot, self.htmlpath, img)
        self.imgpath = img
        return img

    def render_html(self) -> str:
        """渲染html"""
        pie = Pie(init_opts=InitOpts(theme=ThemeType.LIGHT))
        pie.add('KeyWords', self.result.items())
        # pie.set_global_opts(title_opts=TitleOpts(title='主标题', subtitle='附标题'))
        html = CacheModule.create_cache_path('html')
        pie.render(html)
        self.htmlpath = html
        return html



