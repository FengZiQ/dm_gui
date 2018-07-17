# coding=utf-8
from gui_test_tool import *

tool = GUITestTool()


def ability_service_provider_login():
    tool.click_action(
        '/html/body/div[2]/div[1]/span[3]/span',
        '注销按钮'
    )
    # 录入登录信息
    tool.fill_action(
        'username',
        'inspos2',
        '用户名输入框',
        By.ID
    )
    tool.fill_action(
        'password',
        'inspos2',
        '密码输入框',
        By.ID
    )
    tool.click_action(
        'loginSubmit',
        '登录按钮',
        By.ID
    )
    # 断言
    tool.equal_text_assert(
        '//*[@id="accountName"]',
        '登录用户名label',
        'inspos2'
    )
    tool.equal_text_assert(
        '//div[1]/span[2]/a',
        '登录后当前页标题',
        '我的设备',
        '@结束@'
    )

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    ability_service_provider_login()
