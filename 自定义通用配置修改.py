# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()

# 前置条件：创建一个服务商“测试自定义配置模板”，基于该服务商新增一个自定义配置
cus_id = new_customer('测试自定义配置模板')
self_config_id = add_self_config_mode(cus_id)


def old_modify():
    # 进入自定义配置模板页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[4]',
        '金额抓取独立配置标签'
    )
    # 模板名称输入框输入：selenium_测试自定义配置模板
    tool.fill_action(
        'templateName',
        'selenium_测试自定义配置模板',
        '模板名称输入框',
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
    # 模板名称输入框输入：test_modify
    tool.fill_action(
        'templateName',
        'test_modify',
        '模板名称输入框',
        locator=By.ID
    )
    # 点击修改图标
    tool.click_action(
        '//tbody[@id="tbodyTemplateContent"]/tr[1]/td[4]/i[2]',
        '修改图标',
    )
    # 修改第一行参数简称输入：修改1
    tool.fill_action(
        '//tbody[@id="tbodyTemplateContent"]/tr[1]/td[2]/input',
        '修改1',
        '第一行参数简称'
    )
    # 修改第一行参数名称输入：modify1
    tool.fill_action(
        '//tbody[@id="tbodyTemplateContent"]/tr[1]/td[3]/input',
        'modify1',
        '第一行参数简称'
    )
    # 点击确认图标
    tool.click_action(
        '//tbody[@id="tbodyTemplateContent"]/tr[1]/td[4]/i[1]',
        '确认图标',
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改自定义通用配置模板成功',
        end='@结束@'
    )


def remove_modify():
    # 点击删除图标
    tool.click_action(
        '//tbody[@id="tbodyTemplateContent"]/tr[1]/td[4]/i[3]',
        '删除图标',
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
        '删除自定义通用配置模板成功！',
        end='@结束@'
    )


def new_modify():
    # 点击增加字段图标
    tool.click_action(
        'keyAdd',
        '增加字段',
        locator=By.CLASS_NAME
    )
    # 第二行参数简称输入：测试3
    tool.fill_action(
        '//tbody[@id="tbodyTemplateContent"]/tr[2]/td[2]/input',
        '测试3',
        '第二行参数简称'
    )
    # 第二行参数名称输入：test3
    tool.fill_action(
        '//tbody[@id="tbodyTemplateContent"]/tr[2]/td[3]/input',
        'test3',
        '第二行参数简称'
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
        '修改自定义通用配置模板信息成功',
        end='@结束@'
    )


if __name__ == "__main__":
    old_modify()
    remove_modify()
    new_modify()
    tool.mark_status()
    tool.finished()
    # 清理环境
    del_self_config_mode(self_config_id, cus_id)
    delete_customer(cus_id)
