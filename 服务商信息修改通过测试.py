# coding=utf-8
from gui_test_tool import *
from api_condition import *


def modify():
    # 前置条件：新增一个服务商
    cus_id = new_customer('test_测试服务商#')
    tool = GUITestTool()

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
        'querybtn',
        '查询按钮',
        By.ID
    )
    # 点击修改按钮
    tool.click_action(
        '//table/tbody/tr[1]/td[8]/a[3]/i',
        '修改按钮'
    )
    tool.fill_action(
        'name',
        '服务商_name@$'*4,
        '服务商名称',
        By.ID
    )
    tool.fill_action(
        'abb',
        '服务商_name@$',
        '服务商简称',
        By.ID
    )
    tool.fill_action(
        'userName',
        'username_for_service',
        '服务商用户名',
        By.ID
    )

    # click_action(
    #     '//form/div/div/div',
    #     '展开角色下拉框'
    # )
    # click_action(
    #     '//form/div/div/div/div/ul/li/a',
    #     '选择小票管理角色'
    # )

    tool.fill_action(
        'password',
        'te1t_'*3,
        '登录密码',
        By.ID
    )
    tool.fill_action(
        'contact',
        '联系人12'*4,
        '联系人',
        By.ID
    )
    tool.fill_action(
        'mobile',
        '12'*4,
        '电话',
        By.ID
    )
    tool.fill_action(
        'mail',
        '1@100.com',
        '邮箱',
        By.ID
    )
    tool.fill_action(
        'address',
        '中e1@_'*10,
        '地址',
        By.ID
    )
    # 点击保存后，如果睡眠时间过长将导致提示信息丢失
    tool.click_action(
        '//form/div/button[@class="saveBtn"]',
        '保存',
        By.XPATH,
        1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改服务商信息成功',
        '@结束@'
    )

    # cases执行结果
    tool.mark_status()
    tool.finished()

    # 清理环境：删除test_测试服务商# 服务商
    delete_customer(cus_id)


if __name__ == "__main__":
    modify()
