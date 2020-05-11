from typing import Dict
import os
import sys
from pyecharts.charts import Pie
from pyecharts.options import TitleOpts, InitOpts
from pyecharts.globals import ThemeType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

from cache import CacheModule

class EchartsMake:
    def __init__(self, result: Dict[str, float]) -> None:
        self.result = result
        self.htmlpath = ''
    
    def render_img(self) -> str:
        """渲染图片"""
        # 不同系统不同处理
        if sys.platform == 'linux':
            os.environ['PATH'] = '/usr/bin:./drive/linux/'
        elif sys.platform == 'win32':
            os.environ['PATH'] = './drive/win32'
        else:
            os.environ['PATH'] = '/usr/bin:./drive/mac'
        img = CacheModule.create_cache_path('png')
        if self.htmlpath == '':
            self.render_html()
        make_snapshot(snapshot, self.htmlpath, img)
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



