# coding=utf-8
import json
from login_dm import login_api
from configuration_file import config_data
from business_assert import BusinessAssert

server = config_data['server']
session = login_api()
b_assert = BusinessAssert()


# 创建DM平台用户
def add_user_account(username):
    try:
        res = session.post(
            server + 'user/add',
            json={
                "username": username,
                "customerId": 1,
                "password": "123456",
                "passwordRepeat": "123456",
                "locale": "ALL",
                "enableStatus": "1",
                "roleIds": [52]
            }
        )
        temp = json.loads(res.text)
        return temp
    except Exception as e:
        print(e)
        print('创建DM平台用户失败')


# 获取DM平台用户信息
def get_account_info(username):
    try:
        res = session.get(
            server + 'user/pageList?loginUserId=1&operateType=customer&userName=' + username
        )
        temp = json.loads(res.text)
        return temp['data']['list'][0]
    except Exception as e:
        print(e)
        print('获取DM平台用户信息失败')


# 删除DM平台用户
def del_user_account(user_id):
    try:
        session.post(
            server + 'user/deletes',
            json=[int(user_id)]
        )
    except Exception as e:
        print(e)
        print('删除DM平台用户信息失败')


# 创建服务商
def new_customer(name, abb, username):
    try:
        res = session.post(
            server + 'customer/add',
            json={
                "parentId": "-1",
                "name": name,
                "abb": abb,
                "token": "",
                "userName": username,
                "password": "123456",
                "contact": "测试账户",
                "mobile": "15731659260",
                "mail": "1665987439@qq.com",
                "address": "北京海淀",
                "sales_id": "1087",
                "type": '1',
                "platform": '1',
                "enableStatus": "1",
                "roleIds": [54]
            }
        )
        temp = json.loads(res.text)
        return temp
    except Exception as e:
        print(e)
        print('服务商信息新增失败')


# 删除一个服务商
def delete_customer(customer_id):
    try:
        session.post(
            server + 'customer/deletes',
            json=[int(customer_id)]
        )
    except Exception as e:
        print(e)
        print('删除服务商信息失败')


# 创建管理员账户：t_user1
add_user_account('t_user1')
cus_info1 = new_customer('commons库数据同步服务商', '简称1t', 't_user1')
# 断言
b_assert.contained_text_assert(
    str(cus_info1),
    ["'code': 500", "'success': False"],
    end='@结束@',
    state='服务商用户名重复测试'
)

# commons库数据同步问题验证
cus_info2 = new_customer('commons库数据同步服务商', '简称1t', 'user1t')
# 断言
b_assert.contained_text_assert(
    str(cus_info2),
    ["code': 200", "'success': True"],
    state='commons库数据同步服务商',
    end='@结束@'
)
# 标记cases执行状态
b_assert.mark_status()

# 清理环境
del_user_account(get_account_info('t_user1').get('id', 'no data'))
delete_customer(cus_info2.get('data', 'no data'))
if str(cus_info1.get('data', 'no data')).isdigit():
    delete_customer(cus_info1['data'])
