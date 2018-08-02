# coding=utf-8
from gui_test_tool import *
from selenium.webdriver.common.keys import Keys

tool = GUITestTool()


def query_by_device_type():
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
    # 设备类型选择：加强版
    tool.click_action(
        '//select[@id="queryDeviceType"]/option[5]',
        '设备类型下拉框'
    )
    # 断言
    tool.no_text_assert(
        'devicesTable',
        '查询结果列表',
        ['RC', '基础版', '兼容版', '闪票小盒', '外设产品', '公交扫码设备'],
        end='@结束@',
        locator=By.ID
    )


def query_by_product_type():
    # 设备类型选择：Inspos系列
    tool.click_action(
        '//select[@id="productType"]/option[3]',
        '设备类型下拉框'
    )
    # 断言
    tool.no_text_assert(
        'devicesTable',
        '查询结果列表',
        ['条码扫描设备', '国际版', '专销产品', '配件'],
        end='@结束@',
        locator=By.ID
    )


def query_by_device_no():
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
    # 断言
    tool.equal_text_assert(
        'fontbold',
        'list count',
        '1',
        end='@结束@',
        locator=By.CLASS_NAME
    )

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    # 前置条件：设备“4113180400130999”绑定在测试账户下
    query_by_device_type()
    query_by_product_type()
    query_by_device_no()

