# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()


def return_button():
    # 进入全局配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[10]',
        '全局配置标签'
    )
    # 点击新增配置按钮
    tool.click_action(
        'addbtn',
        '新增配置按钮',
        locator=By.ID
    )
    # 点击返回按钮
    tool.click_action(
        'return',
        '返回按钮',
        locator=By.CLASS_NAME
    )
    # 断言
    tool.equal_text_assert(
        'addbtn',
        '新增配置按钮',
        '新增配置',
        end='@结束@',
        locator=By.ID
    )


def add_global_config():
    # 点击新增配置按钮
    tool.click_action(
        'addbtn',
        '新增配置按钮',
        locator=By.ID
    )
    # 配置名称输入框：add_全局配置测试
    tool.fill_action(
        'configName',
        'add_全局配置测试',
        '配置名称输入框',
        locator=By.ID
    )
    # 日志上传地址输入框：http://test.test.cn.com/test
    tool.fill_action(
        'logUrl',
        'http://test.test.cn.com/test',
        '日志上传地址输入框',
        locator=By.ID
    )
    # 票据上传地址输入框：http://test.test.cn.com/test
    tool.fill_action(
        'receiptUrl',
        'http://test.test.cn.com/test',
        '票据上传地址输入框',
        locator=By.ID
    )
    # ping地址输入框：http://test.test.cn.com/test
    tool.fill_action(
        'pingUrl',
        'http://test.test.cn.com/test',
        'ping地址输入框',
        locator=By.ID
    )
    # 点击保存按钮
    tool.click_action(
        'saveBtn',
        '保存按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '新增全局配置信息成功',
        end='@结束@'
    )


if __name__ == "__main__":
    return_button()
    add_global_config()
    tool.mark_status()
    tool.finished()
    # 清理环境
    config_id = get_global_config_id('add_全局配置测试')
    del_global_config(config_id)
