# coding=utf-8
from gui_test_tool import *
from selenium.webdriver.common.keys import Keys


def client_upgrade():
    tool = GUITestTool()

    # 进入设备升级页
    tool.click_action(
        '//*[@id="leftNav"]/li[3]',
        '设备管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[3]/ul/li[4]',
        '设备升级标签',
        response_time=5
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
        '服务商搜索输入框',
        response_time=5
    )
    # 查询
    tool.fill_action(
        'queryDeviceId',
        '44111608000052BA',
        '设备编号输入框',
        locator=By.ID
    )
    tool.click_action(
        'searchBtn',
        '查询按钮',
        locator=By.CLASS_NAME
    )
    # 选择设备
    tool.click_action(
        '//table/tbody/tr/td[1]',
        '选择设备复选框'
    )
    # 点击客户端升级
    tool.click_action(
        'client',
        '客户端升级按钮',
        locator=By.ID,
        response_time=5
    )
    # 点击取消按钮
    tool.click_action(
        '//div[@id="softwareUpgrade"]/div/div/div[4]/button[2]',
        '取消按钮'
    )
    # 点击客户端升级
    tool.click_action(
        'client',
        '客户端升级按钮',
        locator=By.ID,
        response_time=5
    )
    # 选择版本类型：BasePay
    tool.click_action(
        '//select[@id="subType"]/option[2]',
        '版本类型下拉框'
    )
    # 输入版本号：2.0.20
    tool.fill_action(
        'version',
        '2.0.20',
        '版本号输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        '//div[@id="softwareUpgrade"]/div/div/div[2]/button',
        '查询按钮'
    )
    # 选择复选框
    tool.click_action(
        '//table[@id="upgradeCount"]/tbody/tr/td[1]/div/ins',
        '选择复选框'
    )
    # 点击确认升级按钮
    tool.click_action(
        '//div[@id="softwareUpgrade"]/div/div/div[4]/button[1]',
        '确认升级按钮'
    )
    # 点击确认按钮
    tool.click_action(
        'cancel',
        '取消按钮',
        locator=By.CLASS_NAME
    )
    # 点击确认升级按钮
    tool.click_action(
        '//div[@id="softwareUpgrade"]/div/div/div[4]/button[1]',
        '确认升级按钮'
    )
    # 点击确认按钮
    tool.click_action(
        'ok',
        '确认按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '升级指令已下发到您指定的1台设备。',
        end='@结束@'
    )

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    client_upgrade()