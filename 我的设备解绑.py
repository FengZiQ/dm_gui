# coding=utf-8
from api_condition import *
from gui_test_tool import *


def my_device_unbind():
    # 前置条件：销售15台设备给测试账户
    device_info = get_unsold_device_info()
    bind_device('44', '0010025', [device_info[i]['id'] for i in range(len(device_info))])

    tool = GUITestTool()

    # 进入我的设备页
    tool.click_action(
        '//*[@id="leftNav"]/li[3]',
        '设备管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[3]/ul/li[2]',
        '我的设备标签',
    )
    # 查询要解绑的设备号
    tool.fill_action(
        '//*[@id="queryDeviceId"]',
        device_info[0]['serialNum'],
        '设备编号输入框'
    )
    tool.click_action(
        '//*[@class="searchBtn"]',
        '查询按钮'
    )
    # 选择查询到的设备
    tool.click_action(
        '//table/tbody/tr[1]/td[1]',
        '选择框'
    )
    # 解绑按钮
    tool.click_action(
        '//button[@id="unwrap"]',
        '解绑按钮'
    )
    # 取消按钮
    tool.click_action(
        '//button[@class="cancel"]',
        '确认按钮'
    )
    # 解绑按钮
    tool.click_action(
        '//button[@id="unwrap"]',
        '解绑按钮'
    )
    # 确认按钮
    tool.click_action(
        '//button[@class="ok"]',
        '确认按钮'
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '设备解绑成功'
    )
    # 我的设备列表查询
    tool.fill_action(
        '//*[@id="queryDeviceId"]',
        device_info[0]['serialNum'],
        '设备编号输入框'
    )
    tool.click_action(
        '//*[@class="searchBtn"]',
        '查询按钮'
    )
    # 断言
    tool.contained_text_assert(
        '/html/body/div/div/div/div/div/div/span',
        '我的设备中list count',
        ['0']
    )
    # 未销售列表查询
    tool.click_action(
        '/html/body/div/div/ul/li/ul/li[1]/a',
        '未销售列表标签'
    )
    tool.fill_action(
        '//*[@id="queryDeviceId"]',
        device_info[0]['serialNum'],
        '设备编号输入框'
    )
    tool.click_action(
        '//*[@class="searchBtn"]',
        '查询按钮'
    )
    # 断言
    tool.equal_text_assert(
        'fontbold',
        '未销售列表中list count',
        '1',
        end='@结束@',
        locator=By.CLASS_NAME
    )
    tool.mark_status()
    tool.finished()
    # 清理环境
    unbind_device([device_info[i]['id'] for i in range(len(device_info))])


if __name__ == "__main__":
    my_device_unbind()
