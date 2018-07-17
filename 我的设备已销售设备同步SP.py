# coding=utf-8
from api_condition import *
from gui_test_tool import *


def precondition():
    # 创建一个无开发能力服务商并销售15台设备
    new_customer('test_customer0')
    cus_info = customer_info('test_customer0')
    # 销售设备
    device_info = get_unsold_device_info()
    bind_device(
        cus_info['id'],
        cus_info['treeId'],
        [device_info[i]['id'] for i in range(len(device_info))]
    )
    return cus_info, device_info


def sold_device_sync_sp():
    # 前置条件
    cus_info, device_info = precondition()

    tool = GUITestTool()
    tool.click_action(
        '/html/body/div[2]/div[1]/span[4]/span',
        '注销按钮'
    )
    # 录入登录信息
    tool.fill_action(
        'username',
        cus_info['userName'],
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
    # 切至商户管理平台
    tool.click_action(
        '//*[@id="seriveDropdownMenu"]',
        '切换平台下拉框'
    )
    tool.click_action(
        '//*[@id="seriveDropdownMenuContent"]/li[2]/a',
        '选择商户管理平台'
    )
    # 进入设备管理，查询设备
    tool.click_action(
        '/html/body/div/div[2]/ul/li[2]/a',
        '设备管理标签'
    )
    tool.click_action(
        '/html/body/div/div[2]/ul/li[2]/ul/li[2]/a',
        '已销售设备标签'
    )
    # 断言
    tool.equal_text_assert(
        'fontbold',
        'list count',
        '15',
        end='@结束@',
        locator=By.CLASS_NAME
    )

    tool.mark_status()
    tool.finished()
    # 清理环境
    unbind_device([device_info[i]['id'] for i in range(len(device_info))])
    delete_customer(cus_info['id'])


if __name__ == "__main__":
    sold_device_sync_sp()
