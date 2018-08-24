# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()


def precondition(device_no):
    try:
        sum_self_config_id = get_sum_self_config_info(device_no)
        del_sum_self_config(sum_self_config_id['id'])
    except:
        pass


def add_sum_self_config():
    # 前置条件：删除设备"4113180400130999"的金额抓取独立配置
    precondition('4113180400130999')
    # 进入金额抓取独立配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[3]',
        '金额抓取独立配置标签'
    )
    # 点击新增按钮
    tool.click_action(
        'addbtn',
        '新增按钮',
        By.ID,
        response_time=10
    )
    # 点击确认按钮
    tool.click_action(
        'addDeviceBtn',
        '确认按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '请先选择要新增的设备',
        end='@结束@'
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
        locator=By.CLASS_NAME,
        response_time=5
    )
    # 选定设备
    tool.click_action(
        '//table/tbody/tr/td[1]/div/ins',
        '选择复选框'
    )
    # 点击确认按钮
    tool.click_action(
        'addDeviceBtn',
        '确认按钮',
        locator=By.CLASS_NAME
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
    # 日志上传开关：开
    tool.click_action(
        '//form[@id="deviceConfigForm"]/div[4]/div/div[1]/ins',
        '开radio'
    )
    # 票据上传开关：开
    tool.click_action(
        '//form[@id="deviceConfigForm"]/div[5]/div/div[1]/ins',
        '开radio'
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
        '添加成功',
        end='@结束@'
    )
    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    add_sum_self_config()
