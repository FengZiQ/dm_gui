# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()


def ability_service_provider_login():
    # 创建一个有开发的服务商
    cus_id = new_customer('test_测试服务商有开发登录', 55, '4')

    # 注销
    tool.click_action(
        '/html/body/div[2]/div[1]/span[4]/span',
        '注销按钮'
    )
    # 录入登录信息
    tool.fill_action(
        'username',
        'for_test',
        '用户名输入框',
        By.ID
    )
    tool.fill_action(
        'password',
        '123456',
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
        'for_test'
    )
    tool.equal_text_assert(
        '//div[1]/span[2]/a',
        '登录后当前页标题',
        '我的设备',
        '@结束@'
    )

    tool.mark_status()
    tool.finished()
    # 清理环境
    delete_customer(cus_id)


if __name__ == "__main__":
    ability_service_provider_login()
