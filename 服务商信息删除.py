# coding=utf-8
from gui_test_tool import *
from api_condition import *
from selenium.webdriver.common.keys import Keys

tool = GUITestTool()


def delete():
    # 前置条件：新增一个服务商
    cus_id = new_customer('test_测试服务商删除')

    # 点击服务商管理
    tool.click_action(
        '/html/body/div[1]/div[2]/ul/li[2]/a',
        '服务商管理'
    )
    # 服务商名称输入框输入：test_测试服务商删除
    # 点击服务商名称下拉框
    tool.click_action(
        '//button[@data-id="customerId"]',
        '服务商选择下拉按钮'
    )
    # 搜索服务商
    tool.fill_action(
        '//input[@aria-label="Search"]',
        'test_测试服务商删除',
        '服务商搜索框'
    )
    # 回车选定
    tool.fill_action(
        '//input[@aria-label="Search"]',
        Keys.ENTER,
        '服务商搜索框',
        response_time=3
    )
    # 点击删除按钮
    tool.click_action(
        '//table/tbody/tr[1]/td[8]/a[4]/i',
        '删除按钮',
        response_time=8
    )
    # 点击确定按钮
    tool.click_action(
        'ok',
        '确定按钮',
        locator=By.CLASS_NAME,
        response_time=3
    )
    # 断言
    # tool.equal_text_assert(
    #     '//p[@class="msValue"]',
    #     '提示消息',
    #     '删除服务商信息成功！'
    # )
    # time.sleep(3)
    tool.equal_text_assert(
        'fontbold',
        'list count',
        '0',
        end='@结束@',
        locator=By.CLASS_NAME
    )

    # cases执行结果
    tool.mark_status()
    tool.finished()
    # 清理环境
    delete_customer(cus_id)


if __name__ == "__main__":
    delete()
