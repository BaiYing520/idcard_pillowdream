# 枕梦成员身份证图片构造器 idcard_pillowdream
【仅做研究使用，请遵守当地法律法规，法律后果自负】

枕梦成员身份证图片生成工具,填入信息，选择一张头像图片,即可生成黑白和彩色身份证图片。

可以选择是否自动抠图，自动抠图目前仅支持纯色背景，对自动抠图效果不满意可以手动抠图。

在线抠图地址: (https://burner.bonanza.com/) (https://www.gaoding.com/koutu)

## 软件环境

- numpy
- pillow
- opencv

## 打包程序

- 安装pyinstaller

`pip install pyinstaller`

- Windows打包

`pyinstaller -i asserts/ico.ico --windowed --clean --noconfirm --onefile --add-data "asserts;asserts" main.py`

- Windows打包(控制台输出日志)

`pyinstaller -i asserts/ico.ico -c --clean --noconfirm --onefile --add-data "asserts;asserts" main.py`
