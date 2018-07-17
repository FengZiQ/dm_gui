# coding=utf-8
from gui_test_tool import *
from api_condition import *


def sell_device():
    tool = GUITestTool()
    # 测试数据
    test_data = get_unsold_device_info()
    tool.click_action(
        '/html/body/div/div/ul/li[3]/a',
        '设备管理标签'
    )
    tool.click_action(
        '/html/body/div/div/ul/li/ul/li[1]/a',
        '未销售列表标签'
    )
    tool.fill_action(
        '//*[@id="queryDeviceId"]',
        test_data[0]['serialNum'],
        '设备编号输入框'
    )
    tool.click_action(
        '//*[@class="searchBtn"]',
        '查询按钮'
    )
    tool.click_action(
        '//table/tbody/tr/th/div',
        '全选框'
    )
    tool.click_action(
        'salebtn',
        '销售按钮',
        By.ID
    )
    tool.click_action(
        '/html/body/div/div/div/div/div/div/div/div/div/button',
        '点击服务商下拉列表'
    )
    tool.click_action(
        '/html/body/div/div/div/div/div/div/div/div/div/div/ul/li[21]/a',
        '选择测试账户服务商'
    )
    tool.click_action(
        '/html/body/div/div/div/div/div/div/div/div[3]/button',
        '确定按钮',
        By.XPATH,
        1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '设备已成功销售！',
        '@结束@'
    )
    tool.mark_status()
    tool.finished()
    # 清理环境
    unbind_device([test_data[0]['id']])


if __name__ == "__main__":
    sell_device()
