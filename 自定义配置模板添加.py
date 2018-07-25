# coding=utf-8
from gui_test_tool import *
from api_condition import *
from selenium.webdriver.common.keys import Keys

tool = GUITestTool()

# 前置条件：创建一个服务商：测试自定义配置模板
cus_id = new_customer('测试自定义配置模板')


def add_self_config_mode():
    # 进入自定义配置模板页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[4]',
        '金额抓取独立配置标签'
    )
    # 点击添加配置模板按钮
    tool.click_action(
        'addbtn',
        '添加配置模板按钮',
        locator=By.ID
    )
    # 选择服务商：测试账户
    tool.click_action(
        '//button[@data-id="customerId"]',
        '服务商选择下拉按钮'
    )
    # 搜索服务商
    tool.fill_action(
        '//input[@aria-label="Search"]',
        '测试自定义配置模板',
        '服务商搜索框'
    )
    # 回车选定
    tool.fill_action(
        '//input[@aria-label="Search"]',
        Keys.ENTER,
        '服务商搜索框'
    )
    # 模板名称输入框输入：
    tool.fill_action(
        'templateName',
        'test_for_测试',
        '模板名称输入框',
        locator=By.ID
    )
    # 第一行参数简称输入：测试1
    tool.fill_action(
        '//tbody[@id="tbodyTemplateContent"]/tr/td[1]/input',
        '测试1',
        '第一行参数简称'
    )
    # 第一行参数名称输入：test1
    tool.fill_action(
        '//tbody[@id="tbodyTemplateContent"]/tr/td[2]/input',
        'test1',
        '第一行参数简称'
    )
    # 点击增加字段图标
    tool.click_action(
        'keyAdd',
        '增加字段',
        locator=By.CLASS_NAME
    )
    # 第二行参数简称输入：测试1
    tool.fill_action(
        '//tbody[@id="tbodyTemplateContent"]/tr[2]/td[1]/input',
        '测试2',
        '第二行参数简称'
    )
    # 第一行参数名称输入：test1
    tool.fill_action(
        '//tbody[@id="tbodyTemplateContent"]/tr[2]/td[2]/input',
        'test2',
        '第二行参数简称'
    )
    # 点击保存按钮
    tool.click_action(
        'saveBtn',
        '保存按钮',
        locator=By.CLASS_NAME
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '新增金额抓取通用配置信息成功',
        end='@结束@'
    )


if __name__ == "__main__":
    add_self_config_mode()
    tool.mark_status()
    tool.finished()
    # 清理环境
    delete_customer(cus_id)