# coding=utf-8
from gui_test_tool import *

tool = GUITestTool()


def provider_service_verbose_info():

    tool.click_action(
        '/html/body/div[1]/div[2]/ul/li[2]/a',
        '服务商管理'
    )
    tool.click_action(
        '//table/tbody/tr[1]/td[8]/a[1]/i',
        '详情按钮'
    )
    # 断言
    tool.equal_text_assert(
        '//form/div[1]/label/span[1]',
        '服务商名称label',
        '服务商名称:'
    )
    tool.equal_text_assert(
        '//form/div[2]/label/span[1]',
        '服务商简称label',
        '服务商简称:'
    )
    tool.equal_text_assert(
        '//form/div[3]/label/span[1]',
        '服务商密钥label',
        '服务商密钥:'
    )
    tool.equal_text_assert(
        '//form/div[4]/label/span[1]',
        '服务商用户名label',
        '服务商用户名:'
    )
    tool.equal_text_assert(
        '//form/div[5]/label/span[1]',
        '角色label',
        '角色:'
    )
    tool.equal_text_assert(
        '//form/div[6]/label/span[1]',
        '登录密码label',
        '登录密码:'
    )
    tool.equal_text_assert(
        '//form/div[7]/label/span[1]',
        '联系人label',
        '联系人:'
    )
    tool.equal_text_assert(
        '//form/div[8]/label/span[1]',
        '电话label',
        '电话:'
    )
    tool.equal_text_assert(
        '//form/div[9]/label/span[1]',
        '邮箱label',
        '邮箱:'
    )
    tool.equal_text_assert(
        '//form/div[10]/label/span[1]',
        '地址label',
        '地址:'
    )
    tool.equal_text_assert(
        '//form/div[11]/label/span[1]',
        '销售员label',
        '销售员:',
        '@结束@'
    )

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    provider_service_verbose_info()