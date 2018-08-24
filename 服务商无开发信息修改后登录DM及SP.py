# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()


def precondition():
    # 创建一个服务商
    new_customer('test_customer0')
    cus_info = customer_info('test_customer0')
    # 销售设备
    device_info = get_unsold_device_info()
    bind_device(
        cus_info['id'],
        cus_info['treeId'],
        [device_info[i]['id'] for i in range(len(device_info))]
    )
    try:
        session.post(
            'http://dm.preo.inspos.cn/customer/modify',
            json={
                "id": cus_info['id'],
                "treeId": cus_info['treeId'],
                "parentId": cus_info['treeId'],
                "name": 'test_customer1',
                "abb": 'test_customer1',
                "token": cus_info['treeId'],
                "userName": "test_cus1",
                "password": "test_cus1",
                "contact": "测试账户",
                "mobile": "15101043498",
                "mail": "1665987439@qq.com",
                "address": "北京海淀区上地西路六号",
                "sales_id": "595",
                "enableStatus": "1",
                "roleIds": [54, 151],
                "type": "1",
                "platform": "1"
            }
        )
    except Exception as e:
        print(e)
    return cus_info['id']


def lack_ability_service_provider_login():
    # 修改服务商信息
    test_data = precondition()

    tool.click_action(
        '/html/body/div[2]/div[1]/span[4]/span',
        '注销按钮'
    )
    # 录入登录信息
    tool.fill_action(
        'username',
        'test_cus1',
        '用户名输入框',
        By.ID
    )
    tool.fill_action(
        'password',
        'test_cus1',
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
        'test_cus1'
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
        'test_cus1'
    )
    tool.equal_text_assert(
        '//div[1]/span[2]/a',
        '登录后当前页标题',
        '商户管理',
        '@结束@'
    )

    tool.mark_status()
    tool.finished()
    # 清理环境
    delete_customer(test_data)


if __name__ == "__main__":
    lack_ability_service_provider_login()