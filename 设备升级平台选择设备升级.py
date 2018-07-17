# coding=utf-8
from gui_test_tool import *
from selenium.webdriver.common.keys import Keys


def device_upgrade():

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
        '服务商搜索输入框',
        response_time=5
    )
    # 查询要升级的设备
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
    # 点击设备升级按钮
    tool.click_action(
        'addbtn',
        '设备升级按钮',
        locator=By.ID
    )
    # 点击取消按钮
    tool.click_action(
        'cancelButton',
        '设备升级按钮',
        locator=By.CLASS_NAME
    )
    # 点击设备升级按钮
    tool.click_action(
        'addbtn',
        '设备升级按钮',
        locator=By.ID
    )
    time.sleep(3)
    # 选择软件
    tool.click_action(
        '//table[@id="upgradeTbl"]/tbody/tr[1]/td[1]/div/ins',
        '选择BasePayDDB'
    )
    # 选择升级版本
    tool.click_action(
        '//table[@id="upgradeTbl"]/tbody/tr[1]/td[3]/select/option[2]',
        '选择版本1.4.13'
    )
    # 点击确认升级按钮
    tool.click_action(
        'saveButton',
        '确认升级按钮',
        locator=By.CLASS_NAME
    )
    # 点击取消按钮
    tool.click_action(
        'cancel',
        '取消按钮',
        locator=By.CLASS_NAME
    )
    # 点击确认升级按钮
    tool.click_action(
        'saveButton',
        '确认升级按钮',
        locator=By.CLASS_NAME
    )
    # 点击确定按钮
    tool.click_action(
        'ok',
        '确定按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '升级指令已下发到您指定的1台设备。'
    )

    # 点击推送升级时间下拉框
    tool.click_action(
        '//*[@id="searchDateRange"]',
        '推送升级时间下拉框'
    )
    time.sleep(3)
    # 点击自定义图标
    tool.click_action(
        '//div[@class="ranges"]/ul/li[4]',
        '自定义图标'
    )
    time.sleep(3)
    # 点击默认活动的日期
    tool.click_action(
        '//div[@class="calendar right"]/div/table/tbody/tr/td[@class="available active start-date end-date"]',
        '默认活动的日期'
    )
    tool.click_action(
        '//div[@class="calendar left"]/div/table/tbody/tr/td[@class="available active start-date end-date"]',
        '默认活动的日期'
    )
    # 点击确定按钮
    tool.click_action(
        '//div[@class="range_inputs"]/button[1]',
        '确定按钮'
    )
    # 断言
    tool.contained_text_assert(
        'tableBodyCount',
        '当天推送升级查询结果',
        ['44111608000052BA'],
        end='@结束@',
        locator=By.ID
    )
    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    device_upgrade()
