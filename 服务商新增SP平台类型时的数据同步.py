# coding=utf-8
import json
from login_dm import login_api
from configuration_file import config_data
from conn_mysql_db import testing_connect_db
from execute_sql import select_action
from business_assert import contained_text_assert, no_data_assert


server = config_data['server']
session = login_api()


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


def sp_platform():
    cus_id = None
    # 创建全平台服务商
    try:
        res = session.post(
            server + 'customer/add',
            json={
                "parentId": "-1",
                "name": '服务商平台类型测试',
                "abb": "平台类型测试",
                "token": "",
                "userName": 'for_test_user',
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
    except Exception as e:
        print(e)
        print('服务商信息新增失败')
    else:
        cus_id = temp['data']
    # 查询dm_inspos库中数据同步
    dm_customer = select_action(
        testing_connect_db('dm_inspos'),
        'select * from dm_customer where name="服务商平台类型测试"'
    )
    dm_user = select_action(
        testing_connect_db('dm_inspos'),
        'select * from dm_user where user_name="for_test_user"'
    )
    # 查询commons库中数据同步
    commons_customer = select_action(
        testing_connect_db('commons'),
        'select * from common_customer where name="服务商平台类型测试"'
    )
    commons_user = select_action(
        testing_connect_db('commons'),
        'select * from common_user where user_name="for_test_user"'
    )
    # 查询pay库中数据同步
    pay_customer = select_action(
        testing_connect_db('pay'),
        'select * from sp_customer where name="服务商平台类型测试"'
    )
    pay_user = select_action(
        testing_connect_db('pay'),
        'select * from sp_user where user_name="for_test_user"'
    )
    # 断言所有相关数据库数据同步
    contained_text_assert(
        dm_customer,
        ['服务商平台类型测试'],
        state='dm_inspos库dm_customer表中包含服务商“服务商平台类型测试”'
    )
    contained_text_assert(
        dm_user,
        ['for_test_user'],
        state='dm_inspos库dm_user表中包含用户“for_test_user”'
    )
    contained_text_assert(
        commons_customer,
        ['服务商平台类型测试'],
        state='commons库commons_customer表中包含服务商“服务商平台类型测试”'
    )
    contained_text_assert(
        commons_user,
        ['for_test_user'],
        state='commons库commons_user表中包含用户“for_test_user”'
    )
    contained_text_assert(
        pay_customer,
        ['服务商平台类型测试'],
        state='pay库pay_customer表中包含服务商“服务商平台类型测试”'
    )
    contained_text_assert(
        pay_user,
        ['for_test_user'],
        state='pay库pay_user表中包含用户“for_test_user”'
    )
    # 删除服务商
    delete_customer(cus_id)
    # 查询dm_inspos库中数据同步
    dm_customer = select_action(
        testing_connect_db('dm_inspos'),
        'select * from dm_customer where name="服务商平台类型测试"'
    )
    dm_user = select_action(
        testing_connect_db('dm_inspos'),
        'select * from dm_user where user_name="for_test_user"'
    )
    # 查询commons库中数据同步
    commons_customer = select_action(
        testing_connect_db('commons'),
        'select * from common_customer where name="服务商平台类型测试"'
    )
    commons_user = select_action(
        testing_connect_db('commons'),
        'select * from common_user where user_name="for_test_user"'
    )
    # 查询pay库中数据同步
    pay_customer = select_action(
        testing_connect_db('pay'),
        'select * from sp_customer where name="服务商平台类型测试"'
    )
    pay_user = select_action(
        testing_connect_db('pay'),
        'select * from sp_user where user_name="for_test_user"'
    )
    # 断言所有相关数据库数据同步
    no_data_assert(
        dm_customer,
        state='dm_inspos库dm_customer表中不包含服务商“服务商平台类型测试”'
    )
    no_data_assert(
        dm_user,
        state='dm_inspos库dm_user表中不包含用户“for_test_user”'
    )
    no_data_assert(
        commons_customer,
        state='commons库commons_customer表中不包含服务商“服务商平台类型测试”'
    )
    no_data_assert(
        commons_user,
        state='commons库commons_user表中不包含用户“for_test_user”'
    )
    no_data_assert(
        pay_customer,
        state='pay库pay_customer表中不包含服务商“服务商平台类型测试”'
    )
    no_data_assert(
        pay_user,
        end='@结束@',
        state='pay库pay_user表中不包含用户“for_test_user”'
    )
    # 清理环境
    delete_customer(cus_id)


if __name__ == "__main__":
    sp_platform()
