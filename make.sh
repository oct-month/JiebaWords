# # 环境准备
# pip3 install pipenv -U
# pipenv install --skip-lock
# pipenv shell
# pip install pypiwin32 -U

# # -w 不显示终端  -F 打包所有库 -c 显示终端
# pyinstaller -w -i files/img/title.ico app.pyw
# # 提供必要文件

cp -r files dist/app/
cp -r jieba dist/app/
cp -r pyecharts dist/app/
cp files/drive/win32/chromedriver.exe dist/app/
rm -r dist/app/files/drive
rm app.spec