# coding=utf-8
from gui_test_tool import *
from selenium.webdriver.common.keys import Keys


def device_upgrade_query():

    tool = GUITestTool()

    # 进入设备升级页
    tool.click_action(
        '//*[@id="leftNav"]/li[3]',
        '设备管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[3]/ul/li[4]',
        '设备升级标签'
    )
    # 查询：选择测试账户服务商
    tool.click_action(
        '//button[@data-id="customerId"]',
        '服务商下拉列表'
    )
    # 搜索服务商测试账户
    tool.fill_action(
        '//input[@aria-label="Search"]',
        '测试账户',
        '服务商搜索输入框'
    )
    tool.fill_action(
        '//input[@aria-label="Search"]',
        Keys.ENTER,
        '服务商搜索输入框'
    )
    tool.click_action(
        '//select[@id="connectState"]/option[2]',
        '接状态选择已连接'
    )
    time.sleep(8)
    # 断言
    tool.no_text_assert(
        '//div[@id="tableBodyCount"]',
        '查询结果',
        ['北京意锐新创科技有限公司', '未连接']
    )
    # 连接状态选择“全部”
    tool.click_action(
        '//select[@id="connectState"]/option[1]',
        '接状态选择已连接'
    )
    # 查询
    tool.fill_action(
        'queryDeviceId',
        '4113180400130999',
        '设备编号输入框',
        locator=By.ID
    )
    tool.click_action(
        'searchBtn',
        '查询按钮',
        locator=By.CLASS_NAME
    )
    # 断言
    tool.equal_text_assert(
        'fontbold',
        'list count',
        '1',
        end="@结束@",
        locator=By.CLASS_NAME
    )

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    device_upgrade_query()
