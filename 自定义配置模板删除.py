# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()

# 前置条件：创建一个服务商“测试自定义配置模板”，基于该服务商新增一个自定义配置
cus_id = new_customer('测试自定义配置模板')
self_config_id = add_self_config_mode(cus_id)


def self_config_del():
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
    # 点击删除图标，进入删除页面
    tool.click_action(
        '//a[@title="删除"]',
        '删除图标'
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
        '删除自定义通用配置成功',
        end='@结束@'
    )


if __name__ == "__main__":
    self_config_del()
    tool.mark_status()
    tool.finished()
    # 清理环境
    delete_customer(cus_id)
