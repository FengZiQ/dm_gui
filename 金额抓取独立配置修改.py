# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()


def sum_self_config_modify():
    # 前置条件：给设备“4113180400130999”添加金额抓取独立配置
    add_sum_self_config(get_device_info('4113180400130999'))
    # 进入金额抓取独立配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[3]',
        '金额抓取独立配置标签'
    )
    # 设备编号输入框输入：4113180400130999
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
    # 点击修改图标，进入修改页面
    tool.click_action(
        '//a[@title="修改"]',
        '修改图标'
    )
    # 点击返回按钮
    tool.click_action(
        'return',
        '返回按钮',
        locator=By.CLASS_NAME
    )
    # 断言
    tool.equal_text_assert(
        'searchBtn',
        '查询按钮',
        '查询',
        end='@结束@',
        locator=By.CLASS_NAME
    )
    # 点击修改图标，进入修改页面
    tool.click_action(
        '//a[@title="修改"]',
        '修改图标'
    )
    # 金额识别关键字输入框: 总金额,total
    tool.fill_action(
        'feeKeyword',
        '总金额,total',
        '金额识别关键字输入框',
        locator=By.ID
    )
    # 排除关键字输入框: 退款, refund
    tool.fill_action(
        'exclusionKeyword',
        '退款, refund',
        '排除关键字输入框',
        locator=By.ID
    )
    # 点击保存按钮
    tool.click_action(
        'saveBtn',
        '保存按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改成功',
        end='@结束@'
    )

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    sum_self_config_modify()
