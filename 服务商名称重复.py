# coding=utf-8
import json
from login_dm import login_api
from configuration_file import config_data
from business_assert import contained_text_assert


server = config_data['server']
session = login_api()


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


# 服务商名称重复
cus_info0 = new_customer('test服务商名称重复', '简称1t', 'user1t')
cus_info1 = new_customer('test服务商名称重复', '简称2t', 'user2t')
# 断言
contained_text_assert(
    str(cus_info1),
    ["'code': 201", "'success': False"],
    state='服务商名称重复测试'
)

# commons库数据同步问题验证
cus_info2 = new_customer('commons库数据同步服务商', '简称2t', 'user2t')
# 断言
contained_text_assert(
    str(cus_info2),
    ["code': 200", "'success': True"],
    state='commons库数据同步服务商'
)

# 清理环境
delete_customer(cus_info0.get('data', 'no data'))
delete_customer(cus_info2.get('data', 'no data'))
if str(cus_info1.get('data', 'no data')).isdigit():
    delete_customer(cus_info1.get('data', 'no data'))
