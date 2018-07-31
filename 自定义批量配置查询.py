# coding=utf-8
from gui_test_tool import *
from api_condition import *
from selenium.webdriver.common.keys import Keys

tool = GUITestTool()

# 前置条件：设备“4113180400130999”绑定在测试账户下，并给设备“4113180400130999”添加商户号"test_add"
add_self_batch_config('4113180400130999', customer_id='44')
config_id = get_self_batch_config_id('4113180400130999')


def query_by_provider_name():
    # 进入自定义批量配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[7]',
        '自定义批量配置标签'
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
    # 断言
    tool.contained_text_assert(
        'batchConfigTable',
        '查询结果列表',
        ['4113180400130999', 'test_add'],
        end='@结束@',
        locator=By.ID
    )


def query_by_all_option():
    # 商户号输入框：test_add
    tool.fill_action(
        'merchantNo',
        'test_add',
        '服务商搜索框',
        locator=By.ID
    )
    # 设备编号输入框：4113180400130999
    tool.fill_action(
        'serialNum',
        '4113180400130999',
        '服务商搜索框',
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


if __name__ == "__main__":
    query_by_provider_name()
    query_by_all_option()
    tool.mark_status()
    tool.finished()
    # 清理环境
    del_self_batch_config(config_id)
