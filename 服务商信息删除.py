# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()


def delete():
    # 前置条件：新增一个服务商
    cus_id = new_customer('test_测试服务商#')

    # 点击服务商管理
    tool.click_action(
        '/html/body/div[1]/div[2]/ul/li[2]/a',
        '服务商管理'
    )
    # 查询得到新增的服务商作为修改对象
    tool.fill_action(
        'customerName',
        'test_测试服务商#',
        '服务商名称框',
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
    # 点击删除按钮
    tool.click_action(
        '//table/tbody/tr[1]/td[8]/a[4]/i',
        '删除按钮'
    )
    # 点击确定按钮
    tool.click_action(
        '//button[@class="ok"]',
        '确定按钮',
        By.XPATH,
        1
    )

    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '删除服务商信息成功'
    )
    tool.equal_text_assert(
        'fontbold',
        'list count',
        '0',
        '@结束@',
        By.CLASS_NAME
    )

    # cases执行结果
    tool.mark_status()
    tool.finished()
    # 清理环境
    delete_customer(cus_id)


if __name__ == "__main__":
    delete()