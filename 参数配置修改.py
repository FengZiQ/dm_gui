# coding=utf-8
from gui_test_tool import *

tool = GUITestTool()


def modify_page_return():
    # 参数配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[1]',
        '参数配置标签'
    )
    # 进入修改页面
    tool.click_action(
        '//a[@title="修改"]',
        '修改图标'
    )
    # 点击返回按钮
    tool.click_action(
        '//div[@id="saveDiv"]/div',
        '返回按钮'
    )
    # 断言
    tool.equal_text_assert(
        'addbtn',
        '参数配置界面的按钮',
        '添加',
        end='@结束@',
        locator=By.ID
    )


def para_config_modify():
    # 查询修改的参数配置
    tool.fill_action(
        'channelName',
        'fengziqi',
        '参数配置名称输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 进入修改页面
    tool.click_action(
        '//a[@title="修改"]',
        '修改图标'
    )
    tool.click_action(
        '//div[@id="saveDiv"]/button',
        '保存按钮',
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改参数配置信息成功',
        end='@结束@'
    )
    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    modify_page_return()
    para_config_modify()
