# coding=utf-8
from gui_test_tool import *
from api_condition import *
from selenium.webdriver.common.keys import Keys

tool = GUITestTool()


def query_provider_service():
    cus_id = new_customer('test_测试服务商查询')
    # 点击服务商管理标签
    tool.click_action(
        '/html/body/div[1]/div[2]/ul/li[2]/a',
        '服务商管理'
    )
    # 点击服务商名称下拉框
    tool.click_action(
        '//button[@data-id="customerId"]',
        '服务商选择下拉按钮'
    )
    # 搜索服务商
    tool.fill_action(
        '//input[@aria-label="Search"]',
        'test_测试服务商查询',
        '服务商搜索框'
    )
    # 回车选定
    tool.fill_action(
        '//input[@aria-label="Search"]',
        Keys.ENTER,
        '服务商搜索框',
        response_time=3
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