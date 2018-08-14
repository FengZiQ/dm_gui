# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()


def query_provider_service():
    cus_id = new_customer('test_测试服务商查询')

    tool.click_action(
        '/html/body/div[1]/div[2]/ul/li[2]/a',
        '服务商管理'
    )
    # 服务商名称输入框：test_测试服务商查询
    tool.fill_action(
        'customerName',
        'test_测试服务商查询',
        '服务商名称输入框',
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
        'fontbold',
        'list count',
        '1',
        locator=By.CLASS_NAME,
        end='@结束@'
    )

    # cases执行结果
    tool.mark_status()
    tool.finished()
    # 清理环境
    delete_customer(cus_id)


if __name__ == "__main__":
    query_provider_service()