from setuptools import setup

setup(name='idcard_pillowdream',
      version='1',
      description='idcard_pillowdream',
      author='PillowDreamManagementGroup',
      author_email='op@pillowdream.cn',
      license='GPL-3.0',
      packages=['idcard_pillowdream'],
      # data_files=['idcard_pillowdream/asserts/empty.png', 'idcard_pillowdream/asserts/fzhei.ttf', 'idcard_pillowdream/asserts/hei.ttf', 'idcard_pillowdream/asserts/ico.icns', 'idcard_pillowdream/asserts/ocrb10bt.ttf'],
      include_package_data=True,
      install_requires=['numpy==2.2.6', 'pillow==11.3.0', 'opencv-python==4.12.0.88']
      )
