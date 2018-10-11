# coding=utf-8
from login_dm import *
import json
import random
import xlwt

server = config_data['server']
session = login_api()


# 在设备未销售列表中获得15台设备
def get_unsold_device_info():
    try:
        res = session.get(
            server + 'device/pageList?pageSize=15&baseType=2&modelType=4&func=unbindDevices'
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
def new_customer(customer_name, role_id=54, tp='1'):
    try:
        res = session.post(
            server + 'customer/add',
            json={
                "parentId": "-1",
                "name": customer_name,
                "abb": "for_testing" + str(random.randint(0, 100)),
                "token": "",
                "userName": "for_test",
                "password": "123456",
                "contact": "测试账户",
                "mobile": "15731659260",
                "mail": "1665987439@qq.com",
                "address": "北京海淀",
                "sales_id": "1087",
                "type": tp,
                "platform": "1",
                "locale": "CN",
                "enableStatus": "1",
                "roleIds": [role_id]
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


# 获取参数配置信息
def get_para_config(c_name, cus_id):
    try:
        res = session.get(
            server + 'payChannelConfig/pageList?description=' + c_name + '&customerId=' + cus_id
        )
        temp = json.loads(res.text)
        config_info = temp['data']['list'][0]
        return config_info
    except:
        pass


# 删除参数配置
def del_para_config(p_c_id):
    try:
        res = session.post(
            server + 'payChannelConfig/deletes',
            json=[int(p_c_id)]
        )
        return res.text
    except Exception as e:
        print(e)
        print('删除服务商信息失败')


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
        res = session.post(
            server + 'customerConfig/deletes',
            json=[config_id]
        )
        return res.text
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
            json=[int(config_id)]
        )
    except:
        pass


# 新增自定义配置模板
def add_self_config_mode(customer_id, config_name):
    try:
        res = session.post(
            server + 'paramListTemplate/add',
            json={
                "customerId": str(customer_id),
                "templateName": config_name,
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


# 获取自定义配置模板信息
def get_self_config_mode_info(mode_name):
    try:
        res = session.get(
            server + 'paramListTemplate/pageList?templateName=' + mode_name
        )
        temp = json.loads(res.text)
        mode_info = temp['data']['list'][0]
        return mode_info
    except:
        pass


# 删除自定义配置模板
def del_self_config_mode(template_id, customer_id):
    try:
        session.post(
            server + 'paramListTemplate/deletes',
            json={"id": str(template_id), "customerId": str(customer_id)}
        )
    except:
        pass


# 新增自定义通用配置
def add_self_common_config(self_name, customer_id, mode_id):
    try:
        temp = session.get(
            server + 'paramListTemplate/paramTemplateQuery/query?customerId=' + str(customer_id)
        )
        mode_info = json.loads(temp.text)['data']
        res = session.post(
            server + 'paramListConfig/add',
            json={
                "name": self_name,
                "customerId": str(customer_id),
                "paramListParametersList": [
                    {
                        "paramShortname": mode_info[0]['paramShortname'],
                        "paramValue": "test_通用配置1",
                        "paramName": mode_info[0]['paramName'],
                        "templateParametersId": str(mode_info[0]['id'])
                    },
                    {
                        "paramShortname": mode_info[1]['paramShortname'],
                        "paramValue": "test_通用配置2",
                        "paramName": mode_info[1]['paramName'],
                        "templateParametersId": str(mode_info[0]['id'])
                    }
                ],
                "templateName": mode_info[0]['templateName'],
                "paramTemplateId": int(mode_id)
            }
        )
        temp = json.loads(res.text)
        return temp['data']
    except:
        pass


# 自定义通用配置绑定解绑设备: action_type=1为绑定，=0为解绑
def device_and_self_common_config(self_cc_id, action_type, device_id=list(), device_no=list()):
    try:
        session.post(
            server + 'deviceIsBindParamList/modify',
            json={
                "paramListId": self_cc_id,
                "deviceIds": device_id,
                "serialNums": device_no,
                "type": action_type
            }
        )
    except:
        pass


# 获取自定义通用配置信息
def get_self_common_config_id(config_name):
    try:
        res = session.get(
            server + 'paramListConfig/pageList?name=' + config_name
        )
        temp = json.loads(res.text)
        config_id = temp['data']['list'][0]['id']
        return config_id
    except:
        pass


# 删除自定义通用配置
def del_self_common_config(config_id):
    try:
        session.post(
            server + 'paramListConfig/deletes',
            json={"id": int(config_id)}
        )
    except:
        pass


# 获取自定义批量配置信息
def get_self_batch_config_id(device_no, customer_id='44'):
    try:
        res = session.get(
            server + 'definedBatchConfig/pageList?customerId=' + customer_id + '&type=1&serialNum=' + device_no
        )
        temp = json.loads(res.text)
        config_id = temp['data']['list'][0]['id']
        return config_id
    except:
        pass


# 添加自定义批量配置
def add_self_batch_config(device_no, customer_id='44'):
    try:
        session.post(
            server + 'definedBatchConfig/add',
            json={
                "customerId": customer_id,
                "definedBatchConfigInfoList": [{
                    "merchantNum": "test_add",
                    "serialNum": device_no
                }]
            }
        )
    except:
        pass


# 删除自定义批量配置
def del_self_batch_config(config_id):
    try:
        session.post(
            server + 'definedBatchConfig/deletes',
            json=[int(config_id)]
        )
    except:
        pass


# 获取票据解析配置id
def get_receipt_config_id(mode_name, customer_id='44'):
    try:
        res = session.get(
            server + 'receiptTemplate/pageList?customer_id=' + customer_id + '&name=' + mode_name
        )
        temp = json.loads(res.text)
        config_id = temp['data']['list'][0]['id']
        return config_id
    except:
        pass


# 增加票据解析模板
def add_receipt_config_mode(config_name, customer_id):
    try:
        session.post(
            server + 'receiptTemplate/add',
            json={
                "name": config_name,
                "description": "mode描述",
                "exclusiveKeys": ["排除Word"],
                "customerId": customer_id,
                "notifyUrl": "通知url",
                "fields": [{
                    "endType": "1",
                    "fetchType": "1",
                    "key": "关键字",
                    "keywords": ["候选字"],
                    "urlParam": "参数名parameter",
                    "fetchNextLine": "0"
                }],
                "enabled": "1",
                "key": "密钥key",
                "enableStore": "1",
                "securityPush": "1"
            }
        )
    except:
        pass


# 票据解析配置绑定设备
def receipt_config_bind_device(device_id, device_no, mode_id):
    try:
        session.post(
            server + 'receiptTemplateConfig/add',
            json={
                "associateDevice": [{
                    "key": device_id,
                    "value": device_no
                }],
                "id": mode_id
            }
        )
    except:
        pass


# 票据解析配置解绑设备
def receipt_config_unbind_device(mode_id, device_no=list()):
    try:
        session.post(
            server + 'receiptTemplateConfig/deletes',
            json={
                "templateId": mode_id,
                "deviceNos": device_no
            }
        )
    except:
        pass


# 删除票据解析配置
def del_receipt_config_mode(mode_id):
    try:
        res = session.post(
            server + 'receiptTemplate/deletes',
            json=[int(mode_id)]
        )
        return res.text
    except:
        pass


# 新增全局配置
def add_global_config(config_name):
    try:
        res = session.post(
            server + 'commonConfig/add',
            json={
                "configName": config_name,
                "logUrl": "http://test.test",
                "receiptUrl": "http://test.test",
                "pingUrl": "http://test.test"
            }
        )
        temp = json.loads(res.text)
        return temp['data']
    except:
        pass


# 获取全局配置id
def get_global_config_id(config_name):
    try:
        res = session.get(
            server + 'commonConfig/pageList?configName=' + config_name
        )
        temp = json.loads(res.text)
        config_id = temp['data']['list'][0]['id']
        return config_id
    except:
        pass


# 删除全局配置
def del_global_config(config_id):
    try:
        session.post(
            server + 'commonConfig/deletes',
            json=[int(config_id)]
        )
    except:
        pass


# 新增日志配置
def add_log_config(customer_id):
    try:
        res = session.post(
            server + 'logConfig/add',
            json={
                "customerId": customer_id,
                "type": "0",
                "notifyUrl": "http://test.cn.com/customer/notify",
                "signKey": "密钥",
                "description": "描述",
                "status": "1"
            }
        )
        temp = json.loads(res.text)
        return temp['data']
    except:
        pass


# 获取日志配置id
def get_log_config_id(customer_name):
    try:
        res = session.get(
            server + 'logConfig/pageList?customerName=' + customer_name
        )
        temp = json.loads(res.text)
        config_id = temp['data']['list'][0]['id']
        return config_id
    except:
        pass


# 删除日志配置
def del_log_config(config_id):
    try:
        res = session.post(
            server + 'logConfig/deletes',
            json=[int(config_id)]
        )
        return res.text
    except:
        pass


# 新增自定义语音模板
def add_self_voice_template(file_name, config_name, customer_id):
    try:
        files = {'file': open(config_data['file_path'] + file_name, 'rb')}
        res = session.post(
                server + 'voiceTemplateConfig/uploadOss',
                data={
                    'name': config_name,
                    'customerId': str(customer_id),
                    'check': '1',
                    'name1': '支付成功',
                    '1': 'voice.wav',
                    'Content-Type': 'audio/wav',
                    'id': ''
                },
                files=files
            )
        temp = json.loads(res.text)
    except Exception as e:
        print(e)
    else:
        return temp['data']


# 获取自定义语音模板id
def get_self_voice_template_id(config_name):
    try:
        res = session.get(
            server + 'voiceTemplateConfig/pageList?name=' + config_name
        )
        temp = json.loads(res.text)
        config_id = temp['data']['list'][0]['id']
        return config_id
    except:
        pass


# 删除自定义语音模板
def del_self_voice_template(config_id):
    try:
        session.post(
            server + 'voiceTemplateConfig/deletes',
            json={"id": str(config_id)}
        )
    except:
        pass


# 新增自定义壁纸
def add_self_wallpaper(file_name, config_name, customer_id):
    try:
        files = {'file': open(config_data['file_path'] + file_name, 'rb')}
        res = session.post(
                server + 'scanConfig/addWithFile',
                data={
                    'name': config_name,
                    'customerId': str(customer_id),
                    'logoFile': file_name,
                    'operateType': 'modify',
                    'Content-Type': 'image/bmp',
                    'id': ''
                },
                files=files
            )
        temp = json.loads(res.text)
    except Exception as e:
        print(e)
    else:
        return temp['data']


# 获取自定义壁纸id
def get_self_wallpaper_id(config_name):
    try:
        res = session.get(
            server + 'scanConfig/pageList?name=' + config_name
        )
        temp = json.loads(res.text)
        config_id = temp['data']['list'][0]['id']
        return config_id
    except:
        pass


# 删除自定义语音模板
def del_self_wallpaper(config_id):
    try:
        session.post(
            server + 'scanConfig/deletes',
            json=[int(config_id)]
        )
    except:
        pass


if __name__ == "__main__":
    a=get_para_config('fakjfadjfasfja',1)
    print(a)
