# coding=utf-8
import json
from login_dm import login_api
from configuration_file import config_data
from conn_mysql_db import testing_connect_db
from execute_sql import select_action
from business_assert import BusinessAssert

server = config_data['server']
session = login_api()
b_assert = BusinessAssert()


# 创建服务商
def new_customer(platform, locale):
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
                "platform": str(platform),
                "locale": str(locale),
                "enableStatus": "1",
                "roleIds": [54]
            }
        )
        temp = json.loads(res.text)
        return temp['data']
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


def global_sp_platform_dana():
    # 创建全平台服务商
    cus_id = new_customer('3', 'DANA')
    # 查询dm_inspos库中数据同步
    dm_customer = select_action(
        testing_connect_db('dm_inspos'),
        'select * from dm_customer where name="服务商平台类型测试"'
    )
    dm_user = select_action(
        testing_connect_db('dm_inspos'),
        'select * from dm_user where user_name="for_test_user"'
    )
    # 查询commons-dana库中数据同步
    commons_dana_customer = select_action(
        testing_connect_db('commons-dana'),
        'select * from common_customer where name="服务商平台类型测试"'
    )
    commons_dana_user = select_action(
        testing_connect_db('commons-dana'),
        'select * from common_user where user_name="for_test_user"'
    )
    # 查询sp_global_DANA库中数据同步
    dana_customer = select_action(
        testing_connect_db('sp_global_DANA'),
        'select * from spg_customer where name="服务商平台类型测试"'
    )
    dana_user = select_action(
        testing_connect_db('sp_global_DANA'),
        'select * from spg_user where user_name="for_test_user"'
    )
    # 断言所有相关数据库数据同步
    b_assert.contained_text_assert(
        dm_customer,
        ['服务商平台类型测试'],
        end='@结束@',
        state='dm_inspos库dm_customer表中包含服务商“服务商平台类型测试”'
    )
    b_assert.contained_text_assert(
        dm_user,
        ['for_test_user'],
        end='@结束@',
        state='dm_inspos库dm_user表中包含用户“for_test_user”'
    )
    b_assert.contained_text_assert(
        commons_dana_customer,
        ['服务商平台类型测试'],
        end='@结束@',
        state='commons-dana库commons_customer表中包含服务商“服务商平台类型测试”'
    )
    b_assert.contained_text_assert(
        commons_dana_user,
        ['for_test_user'],
        end='@结束@',
        state='commons-dana库commons_user表中包含用户“for_test_user”'
    )
    b_assert.contained_text_assert(
        dana_customer,
        ['服务商平台类型测试'],
        end='@结束@',
        state='sp_global_DANA库spg_customer表中包含服务商“服务商平台类型测试”'
    )
    b_assert.contained_text_assert(
        dana_user,
        ['for_test_user'],
        end='@结束@',
        state='sp_global_DANA库spg_user表中包含用户“for_test_user”'
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
    # 查询commons-dana库中数据同步
    commons_dana_customer = select_action(
        testing_connect_db('commons-dana'),
        'select * from common_customer where name="服务商平台类型测试"'
    )
    commons_dana_user = select_action(
        testing_connect_db('commons-dana'),
        'select * from common_user where user_name="for_test_user"'
    )
    # 查询sp_global_DANA库中数据同步
    dana_customer = select_action(
        testing_connect_db('sp_global_DANA'),
        'select * from spg_customer where name="服务商平台类型测试"'
    )
    dana_user = select_action(
        testing_connect_db('sp_global_DANA'),
        'select * from spg_user where user_name="for_test_user"'
    )
    # 断言所有相关数据库数据同步
    b_assert.no_data_assert(
        dm_customer,
        end='@结束@',
        state='dm_inspos库dm_customer表中不包含服务商“服务商平台类型测试”'
    )
    b_assert.no_data_assert(
        dm_user,
        end='@结束@',
        state='dm_inspos库dm_user表中不包含用户“for_test_user”'
    )
    b_assert.no_data_assert(
        commons_dana_customer,
        end='@结束@',
        state='commons-dana库commons_customer表中不包含服务商“服务商平台类型测试”'
    )
    b_assert.no_data_assert(
        commons_dana_user,
        end='@结束@',
        state='commons-dana库commons_user表中不包含用户“for_test_user”'
    )
    b_assert.no_data_assert(
        dana_customer,
        end='@结束@',
        state='sp_global_DANA库spg_customer表中不包含服务商“服务商平台类型测试”'
    )
    b_assert.no_data_assert(
        dana_user,
        end='@结束@',
        state='sp_global_DANA库spg_user表中不包含用户“for_test_user”'
    )
    # 标记cases状态
    b_assert.mark_status()

    # 清理环境
    delete_customer(cus_id)


if __name__ == "__main__":
    global_sp_platform_dana()
