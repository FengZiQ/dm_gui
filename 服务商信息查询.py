# coding=utf-8
from gui_test_tool import *

tool = GUITestTool()


def query_provider_service():

    tool.click_action(
        '/html/body/div[1]/div[2]/ul/li[2]/a',
        '服务商管理'
    )
    tool.fill_action(
        'customerName',
        '测试账户有开发',
        '服务商名称框',
        By.ID
    )
    tool.click_action(
        'salesName',
        '销售员下拉框',
        By.ID
    )
    tool.click_action(
        '//option[@value="sadmin"]',
        '选择sadmin'
    )
    tool.click_action(
        'querybtn',
        '查询按钮',
        By.ID
    )

    # 断言
    tool.equal_text_assert(
        '//table/tbody/tr/td[1]',
        '服务商名称',
        '测试账户有开发'
    )
    tool.equal_text_assert(
        'fontbold',
        'list count',
        '1',
        '',
        By.CLASS_NAME
    )
    tool.equal_text_assert(
        '//table/tbody/tr/td[6]',
        '销售员',
        'sadmin'
    )
    tool.equal_text_assert(
        '//table/tbody/tr/td[7]',
        '服务商类型',
        '有开发能力',
        '@结束@'
    )

    # cases执行结果
    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    query_provider_service()