import os
from idcard_pillowdream import id_card_utils, name_utils

def test_generate_id_card():
    """测试身份证号生成功能"""
    id_card = id_card_utils.generate_id_card()
    assert len(id_card) == 18, "身份证号应为18位"

def test_generate_name():
    """测试姓名生成功能"""
    name = name_utils.generate_name()
    assert len(name) >= 2, "姓名长度应至少为2位"

def test_resource_files():
    """检查资源文件是否存在"""
    from idcard_pillowdream.id_card_gui import asserts_dir
    assert os.path.exists(os.path.join(asserts_dir, "ico.ico")), "图标文件不存在"
    assert os.path.exists(os.path.join(asserts_dir, "empty.png")), "模板图片不存在"
