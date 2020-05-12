# # 进入虚环境
.venv/Scripts/activate.bat
# # 安装依赖
# pip install -r requirements.txt
# # -w 不显示终端  -F 打包所有库
pyinstaller app.pyw -c
# # 提供必要文件

cp -r files dist/app/
cp -r jieba dist/app/
cp -r pyecharts dist/app/
cp files/drive/win32/chromedriver.exe dist/app/
rm -r dist/app/files/drive
