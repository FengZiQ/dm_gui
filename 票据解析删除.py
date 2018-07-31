# coding=utf-8
from gui_test_tool import *
from api_condition import *
from selenium.webdriver.common.keys import Keys

tool = GUITestTool()


def del_receipt_config_mode():
    # 前置条件：给测试账户添加一个票据解析模板“用于删除测试”，并将设备“4113180400130999”绑定在票据解析模板下
    add_receipt_config_mode('用于删除测试', '44')
    
    # 进入票据解析页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[9]',
        '票据解析标签'
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
    # 模板名称输入框：用于删除测试
    tool.fill_action(
        'templateName',
        '用于删除测试',
        '模板名称输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'searchBtn',
        '查询按钮',
        locator=By.CLASS_NAME
    )
    # 点击删除图标，进入删除页面
    tool.click_action(
        '//table/tbody/tr/td[4]/a[4]/i',
        '删除图标'
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
        '删除成功'
    )
    time.sleep(3)
    tool.equal_text_assert(
        '//table[@id="templateTable"]/tbody/tr/td',
        '查询结果列表',
        '查询不到数据！',
        '@结束@'
    )
    
    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    del_receipt_config_mode()

