# coding=utf-8
from gui_test_tool import *
from api_condition import *
from selenium.webdriver.common.keys import Keys

tool = GUITestTool()

# 前置条件: 创建服务商“test_自定义通用配置”，基于该服务商创建一个自定义配置模板“test_通用配置模板”
cus_id = new_customer('test_自定义通用配置')
mode_id = add_self_config_mode(cus_id, 'test_通用配置模板')


def return_button():
    # 进入自定义通用配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[5]',
        '自定义通用配置标签'
    )
    # 点击添加按钮
    tool.click_action(
        'addbtn',
        '添加按钮',
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
        '添加按钮',
        '添加',
        locator=By.ID,
        end='@结束@'
    )


def delete_mark():
    # 在自定义通用配置页点击添加按钮
    tool.click_action(
        'addbtn',
        '添加按钮',
        locator=By.ID
    )
    # 服务商选择：test_自定义通用配置
    tool.click_action(
        '//button[@data-id="customerId"]',
        '服务商选择下拉按钮'
    )
    # 搜索服务商
    tool.fill_action(
        '//input[@aria-label="Search"]',
        'test_自定义通用配置',
        '服务商搜索框'
    )
    # 回车选定
    tool.fill_action(
        '//input[@aria-label="Search"]',
        Keys.ENTER,
        '服务商搜索框',
        response_time=3
    )
    # 点击删除图标
    tool.click_action(
        '//tbody[@id="tbodyContent"]/tr/td[5]/i',
        '删除图标'
    )
    # 断言
    tool.element_not_exist_assert(
        '//tbody[@id="tbodyContent"]/tr/td[5]/i',
        '删除图标',
        end='@结束@'
    )


def self_common_config_add():
    # 在新增自定义配置页配置名称输入框输入：test_自定义通用配置
    tool.fill_action(
        'name',
        'test_自定义通用配置',
        '配置名称输入框',
        locator=By.ID
    )
    # 服务商选择：test_自定义通用配置
    tool.click_action(
        '//button[@data-id="customerId"]',
        '服务商选择下拉按钮'
    )
    # 搜索服务商
    tool.fill_action(
        '//input[@aria-label="Search"]',
        'test_自定义通用配置',
        '服务商搜索框'
    )
    # 回车选定
    tool.fill_action(
        '//input[@aria-label="Search"]',
        Keys.ENTER,
        '服务商搜索框',
        response_time=3
    )
    # 点击增加字段图标
    tool.click_action(
        'keyAdd',
        '增加字段图标',
        locator=By.CLASS_NAME
    )
    # 第一行参数简称下拉框：选择测试2
    tool.click_action(
        '//tbody[@id="tbodyContent"]/tr/td[1]/select/option[2]',
        '参数简称下拉框'
    )
    # 第一行参数值输入框输入：参数值1
    tool.fill_action(
        '//tbody[@id="tbodyContent"]/tr/td[2]/input',
        '参数值1',
        '参数值输入框'
    )
    # 点击增加字段图标
    tool.click_action(
        'keyAdd',
        '增加字段图标',
        locator=By.CLASS_NAME
    )
    # 第二行参数简称下拉框：选择测试1
    tool.click_action(
        '//tbody[@id="tbodyContent"]/tr[2]/td[1]/select/option[1]',
        '参数简称下拉框'
    )
    # 第二行参数值输入框输入：参数值2
    tool.fill_action(
        '//tbody[@id="tbodyContent"]/tr[2]/td[2]/input',
        '参数值2',
        '参数值输入框'
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
        '新增自定义配置信息成功',
        end='@结束@'
    )


if __name__ == "__main__":
    return_button()
    delete_mark()
    self_common_config_add()
    tool.mark_status()
    tool.finished()
    # 清理环境
    del_self_common_config(get_self_common_config_id('test_自定义通用配置'))
    time.sleep(3)
    del_self_config_mode(mode_id, cus_id)
    delete_customer(cus_id)
