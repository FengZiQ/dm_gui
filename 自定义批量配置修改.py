# coding=utf-8
from gui_test_tool import *
from api_condition import *
from selenium.webdriver.common.keys import Keys

tool = GUITestTool()


def modify():
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
    # 点击修改图标，进入修改页面
    tool.click_action(
        '//a[@title="修改"]',
        '修改图标'
    )
    # 点击取消按钮
    tool.click_action(
        'cancelButton',
        '取消按钮',
        locator=By.CLASS_NAME
    )
    # 点击修改图标，进入修改页面
    tool.click_action(
        '//a[@title="修改"]',
        '修改图标'
    )
    # 商户号输入框: 修改_test
    tool.fill_action(
        'merchantNumInput',
        '修改_test',
        '商户号输入框',
        locator=By.NAME
    )
    # 点击保存按钮
    tool.click_action(
        'saveButton',
        '保存按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改配置商户号成功',
        end='@结束@'
    )
    tool.mark_status()
    tool.finished()
    # 清理环境
    del_self_batch_config(config_id)


if __name__ == "__main__":
    modify()

