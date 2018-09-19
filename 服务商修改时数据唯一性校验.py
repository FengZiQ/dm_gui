# coding=utf-8
import json
import time
from login_dm import login_api
from configuration_file import config_data
from business_assert import BusinessAssert

server = config_data['server']
session = login_api()
b_assert = BusinessAssert()


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


# 获取服务商信息
def customer_info(customer_name):
    cus_info = {}
    try:
        res = session.get(
            server + 'customer/pageList?salesName=sadmin&pageIndex=1&pageSize=5&name=' + customer_name
        )
        temp0 = json.loads(res.text)
        temp1 = temp0['data']['list']
        cus_info = temp1[0]
    except Exception as e:
        print(e)
        print('获取服务商信息失败')

    return cus_info


# 服务商信息修改
def modify_customer(name, abb, username, cus_info):
    try:
        res = session.post(
            config_data['server'] + 'customer/modify',
            json={
                "id": str(cus_info['id']),
                "treeId": str(cus_info['treeId']),
                "parentId": str(cus_info['treeId']),
                "name": name,
                "abb": abb,
                "token": str(cus_info['treeId']),
                "userName": username,
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
        temp = json.loads(res.text)
        return temp
    except Exception as e:
        print(e)


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


# 分别创建服务商“数据唯一性校验test1”与“数据唯一性校验test2”
c1 = new_customer('数据唯一性校验test1', '简称1t', 'user1t')
c2 = new_customer('数据唯一性校验test2', '简称2t', 'user2t')
c_info = customer_info('数据唯一性校验test1')

time.sleep(5)
# 服务商信息修改时，名称唯一性校验
m1 = modify_customer('数据唯一性校验test2', '简称1t', 'user1t', c_info)
# 断言
b_assert.contained_text_assert(
    str(m1),
    ["code': 201", "'success': False"],
    state='commons库数据同步服务商',
    end='@结束@'
)

# 服务商信息修改时，简称唯一性校验
m2 = modify_customer('数据唯一性校验test1', '简称2t', 'user1t', c_info)
# 断言
b_assert.contained_text_assert(
    str(m2),
    ["code': 201", "'success': False"],
    state='commons库数据同步服务商',
    end='@结束@'
)

# 服务商信息修改时，用户名唯一性校验
m3 = modify_customer('数据唯一性校验test1', '简称1t', 'user2t', c_info)
# 断言
b_assert.contained_text_assert(
    str(m3),
    ["code': 500", "'success': False"],
    state='commons库数据同步服务商',
    end='@结束@'
)

# 标记cases执行状态
b_assert.mark_status()

# 清理环境
delete_customer(c1.get('data', 'no data'))
delete_customer(c2.get('data', 'no data'))

