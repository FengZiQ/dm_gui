# coding=utf-8
from gui_test_tool import *

tool = GUITestTool()


def sum_common_config_query_by_provider_name():
    # 进入金额抓取通用配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[2]',
        '金额抓取通用配置标签'
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
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 断言
    tool.contained_text_assert(
        'customerConfigTable',
        '查询结果显示区域',
        ['测试账户'],
        end='@结束@',
        locator=By.ID
    )


def sum_common_config_query_by_config_name():
    try:
        tool.driver.find_element_by_id('customerName').clear()
    except Exception as e:
        print(e)
    # 配置名称输入框输入：测试_fengziqi
    tool.fill_action(
        'configName',
        '测试_fengziqi',
        '配置名称输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 断言
    tool.equal_text_assert(
        'fontbold',
        'list count',
        '1',
        locator=By.CLASS_NAME
    )
    tool.contained_text_assert(
        'customerConfigTable',
        '查询结果显示区域',
        ['测试账户', 'fengziqi'],
        end='@结束@',
        locator=By.ID
    )


if __name__ == "__main__":
    sum_common_config_query_by_provider_name()
    sum_common_config_query_by_config_name()
    tool.mark_status()
    tool.finished()
