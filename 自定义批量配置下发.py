# coding=utf-8
from gui_test_tool import *
from api_condition import *
from selenium.webdriver.common.keys import Keys
from view_log import view_log

tool = GUITestTool()


def issue():
    # 前置条件：设备“4113180400130999”绑定在测试账户下，并给设备“4113180400130999”添加商户号"test_add"
    add_self_batch_config('4113180400130999', customer_id='44')
    config_id = get_self_batch_config_id('4113180400130999')

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
    # 点击下发图标，进入下发页面
    tool.click_action(
        '//a[@title="下发"]',
        '下发图标'
    )
    # 点击确定按钮
    tool.click_action(
        'ok',
        '确定按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言提示消息
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '下发配置成功'
    )
    # 断言log是否触发
    cmd = 'tail -n 500 /data/log/inspos-dm-ppcp2.log | grep "4113180400130999"'
    log_content = {'text': view_log(config_data['log_server1'], cmd)}
    if len(log_content['text']) <= len(cmd):
        log_content['text'] = view_log(config_data['log_server2'], cmd)
    tool.log_assert(
        log_content['text'],
        ['IndependentConfigMsgHandler', 'msg={"deviceNoList":', '"paramName"', '"paramValue"'],
        end='@结束@'
    )
    tool.mark_status()
    tool.finished()
    # 清理环境
    del_self_batch_config(config_id)


if __name__ == "__main__":
    issue()

