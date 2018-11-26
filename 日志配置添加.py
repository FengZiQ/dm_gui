# coding=utf-8
from gui_test_tool import *
from api_condition import *
from selenium.webdriver.common.keys import Keys

tool = GUITestTool()

# 前置条件：增加一个名为“日志配置添加测试服务商”的服务商
cus_id = new_customer('日志配置添加测试服务商')


def return_button():
    # 进入日志配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[11]',
        '日志配置标签'
    )
    # 点击添加日志按钮
    tool.click_action(
        'addbtn',
        '添加日志按钮',
        locator=By.ID
    )
    # 点击返回按钮
    tool.click_action(
        'return',
        '返回按钮',
        locator=By.CLASS_NAME
    )
    # 断言
    tool.equal_text_assert(
        'addbtn',
        '添加日志按钮',
        '添加日志',
        end='@结束@',
        locator=By.ID
    )


def add_global_config():
    # 点击添加日志按钮
    tool.click_action(
        'addbtn',
        '添加日志按钮',
        locator=By.ID
    )
    # 服务商选择：日志配置添加测试服务商
    tool.click_action(
        '//button[@data-id="customerId"]',
        '服务商选择下拉按钮'
    )
    # 搜索服务商
    tool.fill_action(
        '//input[@aria-label="Search"]',
        '日志配置添加测试服务商',
        '服务商搜索框'
    )
    # 回车选定
    tool.fill_action(
        '//input[@aria-label="Search"]',
        Keys.ENTER,
        '服务商搜索框',
        response_time=3
    )
    # 类型选择：https
    tool.click_action(
        '//div[@id="passage"]/div/div[2]/ins',
        'https radio'
    )
    # 推送地址输入框：http://test.test.cn.com/test/testing
    tool.fill_action(
        'notifyUrl',
        'http://test.test.cn.com/test/testing',
        '推送地址输入框',
        locator=By.ID
    )
    # 密钥输入框：密钥_sign_key
    tool.fill_action(
        'signKey',
        '密钥_sign_key',
        '密钥输入框',
        locator=By.ID
    )
    # 描述输入框：description_描述
    tool.fill_action(
        'description',
        'description_描述',
        '描述输入框',
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
        '添加日志配置成功',
        end='@结束@'
    )


if __name__ == "__main__":
    return_button()
    add_global_config()
    tool.mark_status()
    tool.finished()
    # 清理环境
    config_id = get_log_config_id(cus_id)
    del_log_config(config_id)
    delete_customer(cus_id)
