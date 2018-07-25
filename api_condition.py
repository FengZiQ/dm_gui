# coding=utf-8
from login_dm import *
import json
import random
import xlwt

server = 'http://dm.preo.inspos.cn/'
session = login_api()


# 在设备未销售列表中获得15台设备
def get_unsold_device_info():
    try:
        res = session.get(
            server + 'device/pageList?baseType=2&modelType=4&func=unbindDevices'
        )
        temp0 = json.loads(res.text)
        unsold_d_info = temp0['data']['list']
        return unsold_d_info
    except Exception as e:
        print(e)
        print('获取未销售设备号失败')


# 传一个服务商的全称获取服务商的信息
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


# 创建一个服务商
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


# 绑定设备，传服务商ID，服务商tree id，设备id组成的数组
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


# 解绑设备
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


# 生成一个用于批量上传的Excel文件
def upload_excel_file(device_no, file_name):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('Sheet1')
    for i in range(len(device_no)):
        worksheet.write(i + 1, 0, device_no[i])
    workbook.save(file_name)


# 删除升级包
def del_upgrade_package(p_name, p_version):
    try:
        # 获取升级包信息
        res0 = session.get(
            server + 'upgradePackage/pageList?softName=' + p_name + '&version=' + p_version
        )
        release_info = json.loads(res0.text)['data']['list'][0]
    except Exception as e:
        print(e)
    else:
        session.post(
            server + 'upgradePackage/deletes',
            json=[release_info['id']]
        )


# 获取设备信息
def get_device_info(device_no):
    try:
        res = session.get(
            server + 'deviceSale/pageList?connectState=0&operateType=customer&serialNum=' + device_no
        )
        temp = json.loads(res.text)
        device_info = temp['data']['list'][0]
        return device_info
    except:
        pass


# 新增参数配置
def add_para_config(cus_id, is_default):
    try:
        res = session.post(
                server + 'payChannelConfig/add',
                json={
                    "description": "selenium_test"+is_default,
                    "customerId": cus_id,
                    "channelType": "1",
                    "fixationMoney": "",
                    "signKey": "123456",
                    "queryOrderUrl": "",
                    "refundUrl": "",
                    "cancelUrl": "",
                    "queryBillUrl": "",
                    "couponUrl": "",
                    "scannedPayUrl": "",
                    "generateOrderUrl": "",
                    "timeOut": "",
                    "isDefault": is_default
                }
            )

        temp = json.loads(res.text)
    except Exception as e:
        print(e)
    else:
        return temp['data']


# 给非默认参数配置绑定设备
def bind_device_for_para_config(pay_channel_id, device_id, device_no):
    try:
        session.post(
            server + 'editDeviceBindChannel/modify',
            json={"payChannelId": pay_channel_id, "deviceIds": [device_id], "deviceNos": [device_no]}
        )
    except Exception as e:
        print(e)


# 新增金额抓取通用配置
def add_sum_catch_common_config(customer_id, config_name):
    try:
        res = session.post(
            server + 'customerConfig/add',
            json={
                "customerId": customer_id,
                "configName": config_name,
                "feeKeyword": "识别关键字",
                "exclusionKeyword": "排除关键字",
                "logStatus": "1",
                "receiptStatus": "1"
            }
        )
        temp = json.loads(res.text)
    except Exception as e:
        print(e)
    else:
        return temp['data']


# 获取金额抓取通用配置信息
def get_sum_catch_common_config_info(config_name):
    try:
        res = session.get(
            server + 'customerConfig/pageList?configName=' + config_name
        )
        temp = json.loads(res.text)
        device_info = temp['data']['list'][0]
        return device_info
    except:
        pass


# 删除金额抓取通用配置
def del_sum_catch_common_config(config_id):
    try:
        session.post(
            server + 'customerConfig/deletes',
            json=[config_id]
        )
    except:
        pass


# 新增金额抓取独立配置
def add_sum_self_config(device_info):
    try:
        res = session.post(
            server + 'deviceConfig/add',
            json={
                "id": device_info['id'],
                "serialNum": device_info['serialNum'],
                "feeKeyword": "test",
                "exclusionKeyword": "测试",
                "logStatus": "1",
                "receiptStatus": "1",
                "modelType": device_info['modelType'],
                "modelId": device_info['modelId']
            }
        )
        temp = json.loads(res.text)
        return temp['data']
    except:
        pass


# 获取金额抓取独立配置信息
def get_sum_self_config_info(device_no):
    try:
        res = session.get(
            server + 'deviceConfig/pageList?serialNum=' + device_no
        )
        temp = json.loads(res.text)
        device_info = temp['data']['list'][0]
        return device_info
    except:
        pass


# 删除金额抓取独立配置
def del_sum_self_config(config_id):
    try:
        session.post(
            server + 'deviceConfig/deletes',
            json=[config_id]
        )
    except:
        pass


# 新增自定义配置模板
def add_self_config_mode(customer_id):
    try:
        res = session.post(
            server + 'paramListTemplate/add',
            json={
                "customerId": customer_id,
                "templateName": "selenium_测试自定义配置模板",
                "paramNameValue": [
                    {"paramShortName": "测试1", "paramName": "test1"},
                    {"paramShortName": "测试2", "paramName": "test2"}
                ]
            }
        )
        temp = json.loads(res.text)
        return temp['data']
    except:
        pass


# 删除自定义配置模板
def del_self_config_mode(template_id, customer_id):
    try:
        session.post(
            server + 'paramListTemplate/deletes',
            json={"id": template_id,"customerId": customer_id}
        )
    except:
        pass


if __name__ == "__main__":
    # print(get_unsold_device_info())
    # print(customer_info('测试账户'))
    # print(new_customer('test_customer'))
    # delete_customer(new_customer('test_customer'))
    # upload_excel_file(get_unsold_device_info())
    # unbind_device()
    # total_customer()
    # del_upgrade_package('')
    # del_upgrade_package('test_ces', '1.000.000')
    # print(get_device_info('4113180400130999'))
    # print(add_para_config('44', '0'))
    # print(get_sum_catch_common_config_info('payplus商户'))
    # print(get_sum_self_config_info('4113180400130999'))
    # del_sum_self_config('')
    # print(add_sum_self_config(get_device_info('4113180400130999')))
    print(add_self_config_mode('8'))
