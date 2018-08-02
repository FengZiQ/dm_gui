# coding=utf-8
from gui_test_tool import *
from selenium.webdriver.common.keys import Keys

tool = GUITestTool()


def cancel_button():
    # 进入票据管理页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[8]',
        '票据管理标签'
    )
    # 服务商选择：测试账户
    tool.click_action(
        '//button[@data-id="customerId"]',
        '服务商选择下拉按钮'
    )
    # 搜索服务商
    tool.fill_action(
        '//input[@aria-label="Search"]',
        '测试账户',
        '服务商搜索框'
    )
    # 回车选定
    tool.fill_action(
        '//input[@aria-label="Search"]',
        Keys.ENTER,
        '服务商搜索框',
        response_time=3
    )
    # 设备编号输入框：4113180400130999
    tool.fill_action(
        'queryDeviceId',
        '4113180400130999',
        '设备编号输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'searchBtn',
        '查询按钮',
        locator=By.CLASS_NAME
    )
    # 点击设备编号"4113180400130999", 进入票据配置信息页
    tool.click_action(
        '//table/tbody/tr/td[1]/a',
        '设备编号"4113180400130999"'
    )
    # 点击该设备票据配置信息按钮
    tool.click_action(
        'addbtn',
        '该设备票据配置信息按钮',
        locator=By.ID
    )
    # 点击添加配置按钮
    tool.click_action(
        'addbtn',
        '添加配置按钮',
        locator=By.ID,
        response_time=5
    )
    # 点击取消按钮
    tool.click_action(
        'cancelButton',
        '取消按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        'addbtn',
        '添加配置按钮',
        '添加配置',
        end='@结束@',
        locator=By.ID
    )


def del_config():
    # 点击删除配置按钮
    tool.click_action(
        'batchDel',
        '删除配置按钮',
        locator=By.CLASS_NAME,
        response_time=2
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '请先选择要删除的票据配置',
        end='@结束@'
    )


def add_config():
    # 点击添加配置按钮
    tool.click_action(
        'addbtn',
        '添加配置按钮',
        locator=By.ID,
        response_time=5
    )
    # 点击票据复选框
    tool.click_action(
        '//table[@id="addReceipTable"]/tbody/tr[1]/td[1]/div/ins',
        '票据复选框'
    )
    # 点击确定按钮
    tool.click_action(
        'saveButton',
        '确定按钮',
        locator=By.CLASS_NAME
    )
    # 点击弹窗中的确定按钮
    tool.click_action(
        'ok',
        '确定按钮',
        locator=By.CLASS_NAME,
        response_time=5
    )
    # 断言
    tool.equal_text_assert(
        'addParserItem',
        '添加解析区域按钮',
        '添加解析区域',
        end='@结束@',
        locator=By.CLASS_NAME
    )


if __name__ == "__main__":
    # 前置条件：设备“4113180400130999”绑定在测试账户下
    cancel_button()
    del_config()
    add_config()
    tool.mark_status()
    tool.finished()
