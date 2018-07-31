# coding=utf-8
from gui_test_tool import *

tool = GUITestTool()


def custom_independent_config():
    # 进入自定义独立配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[6]',
        '自定义独立配置标签',
        response_time=2
    )
    # 断言
    tool.element_not_exist_assert(
        '/html/body/div/div/span/p',
        '提示消息'
    )
    # 设备编号输入框输入：4113180400130999
    tool.fill_action(
        'queryDeviceId',
        '4113180400130999',
        '设备编号输入框',
        locator=By.ID
    )
    # 服务商名称输入框输入：测试账户
    tool.fill_action(
        'customerName',
        '测试账户',
        '服务商名称输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'searchBtn',
        '查询按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.element_not_exist_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        end='@结束@'
    )

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    custom_independent_config()