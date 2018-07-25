# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()

# 前置条件：创建一个服务商“测试自定义配置模板”，基于该服务商新增一个自定义配置
cus_id = new_customer('测试自定义配置模板')
self_config_id = add_self_config_mode(cus_id)


def self_config_query():
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
    # 断言
    tool.equal_text_assert(
        'fontbold',
        'list count',
        '1',
        end='@结束@',
        locator=By.CLASS_NAME
    )


def verbose_info():
    # 点击详情图标，进入详情页面
    tool.click_action(
        '//a[@title="详情"]',
        '详情图标'
    )
    # 断言
    tool.contained_text_assert(
        'definedTemplateForm',
        '自定义通用配置模板详情显示区域',
        expected_text=[
            '服务商', '模板名称',
            '参数简称', '参数名', '操作'
        ],
        end='@结束@',
        locator=By.ID
    )


if __name__ == "__main__":
    self_config_query()
    verbose_info()
    tool.mark_status()
    tool.finished()
    # 清理环境
    del_self_config_mode(self_config_id, cus_id)
    delete_customer(cus_id)
