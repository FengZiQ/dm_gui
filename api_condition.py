# coding=utf-8
from login_dm import *
import json
import random
import xlwt

server = 'http://dm.preo.inspos.cn/'
session = login_api()


def get_unsold_device_info():
    try:
        res = session.get(
            server + 'device/pageList?pageIndex=1&pageSize=15&serialNum=&baseType=2&modelType=4&func=unbindDevices'
        )
        temp0 = json.loads(res.text)
        unsold_d_info = temp0['data']['list']
    except Exception as e:
        print(e)
        print('获取未销售设备号失败')
    else:
        return unsold_d_info


def customer_info(customer_name):
    cus_info = {}
    try:
        res = session.get(
            server + 'customer/pageList?name=' + customer_name + '&salesName=sadmin&pageIndex=1&pageSize=5'
        )
        temp0 = json.loads(res.text)
        temp1 = temp0['data']['list']
        cus_info = temp1[0]
    except Exception as e:
        print(e)
        print('获取服务商信息失败')

    return cus_info


def new_customer(customer_name):
    try:
        res = session.post(
            server + 'customer/add',
            json={
                "parentId": "-1",
                "name": customer_name,
                "abb": "for_testing" + str(random.randint(0, 100)),
                "token": "",
                "userName": "for_t" + str(random.randint(0, 100)),
                "password": "123456",
                "contact": "fzq",
                "mobile": "00000000",
                "mail": "00@00000",
                "address": "00",
                "sales_id": "1087",
                "type": "1",
                "platform": "1",
                "enableStatus": "1",
                "roleIds": [54, 153]
            }
        )
        temp = json.loads(res.text)
    except Exception as e:
        print(e)
        print('服务商信息新增失败')
    else:
        return temp['data']


def delete_customer(customer_id):
    try:
        session.post(
            server + 'customer/deletes',
            json=[int(customer_id)]
        )
    except Exception as e:
        print(e)
        print('删除服务商信息失败')


def bind_device(customer_id, tree_id, device_id_list=list()):
    try:
        session.post(
            server + 'device/modify',
            json={
                "deviceIdList": device_id_list,
                "customerId": customer_id,
                "treeId": tree_id,
                "operateType": "bindCustomer"
            }
        )
    except Exception as e:
        print(e)
        print('解绑设备失败')


def unbind_device(device_id_list=list()):
    try:
       session.post(
            server + 'device/modify',
            json={
                "deviceIdList": device_id_list,
                "operateType": "unbindCustomer"
            }
        )
    except Exception as e:
        print(e)
        print('解绑设备失败')


def upload_excel_file(device_info, file_name):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('Sheet1')
    for i in range(len(device_info)):
        worksheet.write(i + 1, 0, device_info[i]['serialNum'])
    workbook.save(file_name)


def del_upgrade_package(p_name, p_version):
    try:
        # 获取升级包信息
        res0 = session.get(
            server + 'upgradePackage/pageList?softName=' + p_name +
            '&subType=&type=&version=' + p_version + '&upgradeStatus=&status=&pageIndex=1&pageSize=15'
        )
        release_info = json.loads(res0.text)['data']['list'][0]
    except Exception as e:
        print(e)
    else:
        session.post(
            server + 'upgradePackage/deletes',
            json=[release_info['id']]
        )


def get_device_info(device_no):
    try:
        url_para = 'deviceSale/pageList?customerId=&pageIndex=1&pageSize=15&connectState=0&operateType=customer&baseType=&modelType=&'
        res = session.get(
            server + url_para + 'serialNum=' + device_no
        )
        temp = json.loads(res.text)
        device_info = temp['data']['list'][0]
        return device_info
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # print(get_unsold_device_info())
    # print(customer_info('测试账户'))
    # print(new_customer('test_customer'))
    # delete_customer(new_customer('test_customer'))
    # upload_excel_file(get_unsold_device_info())
    # unbind_device()
    # total_customer()
    # del_upgrade_package('')
    # del_upgrade_package('0000', '0000')
    print(get_device_info('4113180400130999'))