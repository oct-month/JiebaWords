import os
from pyecharts.charts import Pie
from pyecharts.options import TitleOpts, InitOpts
from pyecharts.globals import ThemeType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

from initial import InitialModule
from read import ReadModule
from analysis import AnalysisModule

if __name__ == "__main__":
    a = ['cache\\files']
    a = InitialModule(a).init_paths()
    path = ReadModule(a).read_all()
    result = AnalysisModule(path, 30).analyse()
    print(result)
    pie = Pie(init_opts=InitOpts(theme=ThemeType.LIGHT))
    pie.add('奥里给', result.items())
    pie.set_global_opts(title_opts=TitleOpts(title='主标题', subtitle='附标题'))
    
    pie.render('echarts/charts.html')

    os.environ['PATH'] = './drive/win32/'
    make_snapshot(snapshot, 'echarts/charts.html', 'test/test.png')

