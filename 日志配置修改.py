# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()

# 前置条件：增加一个名为“日志配置修改测试服务商”的服务商，并给该服务商添加一个日志配置
cus_id = new_customer('日志配置修改测试服务商')
add_log_config(cus_id)
config_id = get_log_config_id('日志配置修改测试服务商')


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
    # 服务商名称输入框：日志配置修改测试服务商
    tool.fill_action(
        'customer_input',
        '日志配置修改测试服务商',
        '服务商名称输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
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
        'addbtn',
        '添加日志按钮',
        '添加日志',
        end='@结束@',
        locator=By.ID
    )


def modify_info():
    # 点击修改图标，进入修改页面
    tool.click_action(
        '//a[@title="修改"]',
        '修改图标'
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
        '修改日志配置成功',
        end='@结束@'
    )


if __name__ == "__main__":
    return_button()
    modify_info()
    tool.mark_status()
    tool.finished()
    # 清理环境
    del_log_config(config_id)
    delete_customer(cus_id)