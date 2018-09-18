# coding=utf-8
import json
import time
from login_dm import login_api
from login_sg import login_sg_api
from configuration_file import config_data
from business_assert import contained_text_assert


dm_server = config_data['server']
sg_server = config_data['sgServer']
dm_session = login_api()
sg_session = login_sg_api()


# 创建服务商
def new_customer(name, abb, username):
    try:
        res = dm_session.post(
            dm_server + 'customer/add',
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
                "platform": '3',
                "locale": 'CN',
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
        dm_session.post(
            dm_server + 'customer/deletes',
            json=[int(customer_id)]
        )
    except Exception as e:
        print(e)
        print('删除服务商信息失败')


# 获取商户信息
def get_merchant_info(cus_name, p_id='', t_id=''):
    try:
        res = sg_session.get(
            sg_server + 'customer/pageList?operateType=sp&name='+cus_name+'&parentId='+str(p_id)+'&treeId'+str(t_id)
        )
        temp = json.loads(res.text)
        m_info = temp['data']['list']
    except Exception as e:
        print(e)
        print('获取服务商信息失败')
    else:
        return m_info


# 新增商户：t_uName_sh
def add_merchant(p_id):
    try:
        res = sg_session.post(
                sg_server + 'customer/add',
                json={
                    "parentId": str(p_id),
                    "abb": 't_uName_sh',
                    "name": 't_uName_sh',
                    "type": '2',
                    "contact": "测试账户",
                    "mobile": "0"*8,
                    "mail": "test@cn.com",
                    "address": "北京海淀",
                    "enableStatus": "1"
                }
            )
        temp = json.loads(res.text)
        return temp['data']
    except Exception as e:
        print(e)


# 删除商户
def del_merchant(m_id):
    try:
        sg_session.post(
            sg_server + 'customer/deletes',
            json=[int(m_id)]
        )
    except Exception as e:
        print(e)
        print('删除商户失败')


# 新增SP商户用户
def add_sg_user(c_id, name):
    try:
        res = sg_session.post(
                sg_server + 'user/add?operateType=customer',
                json={
                    "username": name,
                    "password": "123456",
                    "passwordRepeat": "123456",
                    "enableStatus": "1",
                    "customerId": int(c_id),
                    "roleIds": [60]
                }
            )
        temp = json.loads(res.text)
        return temp['data']
    except Exception as e:
        print(e)


# 删除SP用户
def del_sg_user(u_id):
    try:
        sg_session.post(
            sg_server + 'user/deletes',
            json=[int(u_id)]
        )
    except Exception as e:
        print(e)


# 前置条件：创建一个服务商，给该服务商创建一个商户及商户用户
cus_info0 = new_customer('test服务商用户名重复SG用户', '简称t1', 't_sg_user')
time.sleep(5)
mer_info = get_merchant_info('test服务商用户名重复SG用户')
sh_id = add_merchant(mer_info[0].get('id', 'no data'))
time.sleep(3)
user_id = add_sg_user(sh_id, 'tsg_user1')

# 创建与SG平台用户重名的服务商
cus_info1 = new_customer('commons库数据同步服务商', '简称t2', 'tsg_user1')
# 断言
contained_text_assert(
    str(cus_info1),
    ["'code': 500", "'success': False"],
    state='服务商用户名与SG平台用户名重复测试'
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
del_sg_user(user_id)
del_merchant(sh_id)
delete_customer(cus_info0.get('data', 'no data'))
delete_customer(cus_info2.get('data', 'no data'))
if str(cus_info1.get('data', 'no data')).isdigit():
    delete_customer(cus_info1.get('data', 'no data'))
