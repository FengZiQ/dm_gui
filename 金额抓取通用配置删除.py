# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()


def del_sum_common_config():
    # 前置条件
    add_sum_catch_common_config('44', 'selenium_测试')
    # 进入金额抓取通用配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[2]',
        '金额抓取通用配置标签'
    )
    # 配置名称输入框输入：selenium_test_sum
    tool.fill_action(
        'configName',
        'selenium_测试',
        '配置名称输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 点击删除图标
    tool.click_action(
        '//a[@title="删除"]',
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
        '删除金额抓取通用配置成功！'
    )
    tool.equal_text_assert(
        'fontbold',
        'list count',
        '0',
        '@结束@',
        By.CLASS_NAME
    )

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    del_sum_common_config()
