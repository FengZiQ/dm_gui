# coding=utf-8
from gui_test_tool import *
from api_condition import *
from configuration_file import config_data

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
            config_data['server'] + 'customer/modify',
            json={
                "id": str(cus_info['id']),
                "treeId": str(cus_info['treeId']),
                "parentId": str(cus_info['treeId']),
                "name": 'test_customer1',
                "abb": 'test_customer1',
                "token": str(cus_info['treeId']),
                "userName": "test_cus1",
                "password": "test_cus1",
                "contact": "测试账户",
                "mobile": "15101043498",
                "mail": "1665987439@qq.com",
                "address": "北京海淀区上地西路六号",
                "sales_id": str(cus_info['salesId']),
                "enableStatus": "1",
                "roleIds": [54],
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
        By.ID,
        response_time=5
    )
    # 点击服务商名称下拉列表
    tool.click_action(
        '//button[@data-id="customerId"]',
        '服务商名称下拉列表'
    )
    # 断言:
    # 1.登录用户信息正确
    tool.equal_text_assert(
        '//*[@id="accountName"]',
        '登录用户名label',
        'test_cus1'
    )
    # 2.登录后打开的初始页面正确
    tool.equal_text_assert(
        '//div[1]/span[2]/a',
        '登录后当前页标题',
        '我的设备'
    )
    # 3.服务商名称为“test_customer1”
    tool.element_attribute(
        '//button[@data-id="customerId"]',
        '服务商下拉列表',
        'title',
        'test_customer1'
    )
    # 4.下拉列表中没有第二条数据
    tool.element_not_exist_assert(
        '//div[@id="myDeviceContainer"]/div[1]/div/div/ul/li[2]/a',
        '服务商下拉列表'
    )
    time.sleep(3)
    # 切换至商户管理平台
    tool.click_action(
        'seriveDropdownMenu',
        '切换平台下拉框',
        locator=By.ID
    )
    tool.click_action(
        '//ul[@id="seriveDropdownMenuContent"]/li[2]/a',
        '选择商户管理平台',
        response_time=5
    )
    # 断言
    # 1.登录用户身份信息
    tool.equal_text_assert(
        '//*[@id="accountName"]',
        '登录用户名label',
        'test_cus1'
    )
    # 2.商户树是服务商自己的
    tool.element_not_exist_assert(
        '//ul[@id="listTree"]/li[2]',
        '非服务商的商户树'
    )
    # 3.登录后打开的初始页面正确
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
