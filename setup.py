from setuptools import setup

setup(name='idcard_pillowdream',  
      version='1',  # 版本为1
      description='idcard_pillowdream',  
      author='PillowDreamManagementGroup',  
      # author_email='airobot@airobot.link'
      license='GPL-3.0',
      packages=['idcard_pillowdream'],  
      include_package_data=True,
      install_requires=['numpy==2.2.6', 'pillow==11.3.0', 'opencv-python==4.12.0.88']
      )
