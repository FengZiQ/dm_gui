# coding=utf-8
from gui_test_tool import *

tool = GUITestTool()


def lack_ability_service_provider_login():
    tool.click_action(
        '/html/body/div[2]/div[1]/span[4]/span',
        '注销按钮'
    )
    # 录入登录信息
    tool.fill_action(
        'username',
        'inspos',
        '用户名输入框',
        By.ID
    )
    tool.fill_action(
        'password',
        'inspos',
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
        'inspos'
    )
    tool.equal_text_assert(
        '//div[1]/span[2]/a',
        '登录后当前页标题',
        '我的设备'
    )
    time.sleep(3)
    # 切换至商户管理平台
    tool.click_action(
        '//*[@id="seriveDropdownMenu"]',
        '切换平台下拉框'
    )
    tool.click_action(
        '//*[@id="seriveDropdownMenuContent"]/li[2]/a',
        '选择商户管理平台'
    )
    # 断言
    tool.equal_text_assert(
        '//*[@id="accountName"]',
        '登录用户名label',
        'inspos'
    )
    tool.equal_text_assert(
        '//div[1]/span[2]/a',
        '登录后当前页标题',
        '商户管理',
        '@结束@'
    )

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    lack_ability_service_provider_login()