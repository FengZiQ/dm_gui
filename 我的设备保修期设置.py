# coding=utf-8
from api_condition import *
from gui_test_tool import *
import time


def setting_w_p_by_api(device_no=list()):
    now_time = time.strftime('%Y-%m-%d')
    try:
        session.post(
            server + 'device/guarantee/edit',
            json={
                "serialNumList": device_no,
                "guarantee": None,
                "delayGuarantee": None,
                "startTime": now_time,
                "endTime": now_time
            }
        )
    except Exception as e:
        print(e)


def setting_warranty_period():
    # 前置条件：销售15台设备给测试账户
    device_info = get_unsold_device_info()
    bind_device('44', '0010025', [device_info[i]['id'] for i in range(len(device_info))])

    tool = GUITestTool()

    # 进入我的设备页
    tool.click_action(
        '//*[@id="leftNav"]/li[3]',
        '设备管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[3]/ul/li[2]',
        '我的设备标签',
    )
    # 查询需要设置保修期的设备
    tool.fill_action(
        '//*[@id="queryDeviceId"]',
        device_info[0]['serialNum'],
        '设备编号输入框'
    )
    tool.click_action(
        '//*[@class="searchBtn"]',
        '查询按钮'
    )
    # 断言
    tool.equal_text_assert(
        '//table/tbody/tr[1]/td[7]',
        '起始保修天数',
        '364'
    )
    # 通过接口测试日历设置保修期
    setting_w_p_by_api([device_info[0]['serialNum']])
    # 查询
    tool.fill_action(
        '//*[@id="queryDeviceId"]',
        device_info[0]['serialNum'],
        '设备编号输入框'
    )
    tool.click_action(
        '//*[@class="searchBtn"]',
        '查询按钮'
    )
    # 断言
    tool.equal_text_assert(
        '//table/tbody/tr[1]/td[7]',
        '修改后的保修天数',
        '0'
    )
    # 选择查询到的设备
    tool.click_action(
        '//table/tbody/tr[1]/td[1]',
        '选择框'
    )
    # 保修期设置按钮
    tool.click_action(
        '//button[@id="periodSet"]',
        '保修期设置按钮'
    )
    # 返回按钮
    tool.click_action(
        '//button[@class="cancelButton"]',
        '确认按钮'
    )
    # 保修期设置按钮
    tool.click_action(
        '//button[@id="periodSet"]',
        '保修期设置按钮'
    )
    # 输入保修期
    tool.fill_action(
        '//div[@class="deviceGuarantee"]/input',
        '1',
        '保修期输入框'
    )
    tool.fill_action(
        '//div[@class="deviceWarranty"]/input',
        '1',
        '延保期输入框'
    )
    # 保存按钮
    tool.click_action(
        '//button[@class="saveButton"]',
        '保存按钮',
        By.XPATH,
        1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '保修期设置成功'
    )
    # 查询
    tool.fill_action(
        '//*[@id="queryDeviceId"]',
        device_info[0]['serialNum'],
        '设备编号输入框'
    )
    tool.click_action(
        '//*[@class="searchBtn"]',
        '查询按钮'
    )
    # 断言
    tool.equal_text_assert(
        '//table/tbody/tr[1]/td[7]',
        '设置后的保修天数',
        '729'
    )
    # 通过表格中保修期天数设置
    tool.click_action(
        '//table/tbody/tr[1]/td[7]',
        '表格中的保修天数'
    )
    # 输入保修期
    tool.fill_action(
        '//div[@class="deviceGuarantee"]/input',
        '1',
        '保修期输入框'
    )
    tool.fill_action(
        '//div[@class="deviceWarranty"]/input',
        '0',
        '延保期输入框'
    )
    # 保存按钮
    tool.click_action(
        '//button[@class="saveButton"]',
        '保存按钮',
        By.XPATH,
        1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '保修期设置成功'
    )
    # 找到被修改保修期的设备
    tool.fill_action(
        '//*[@id="queryDeviceId"]',
        device_info[0]['serialNum'],
        '设备编号输入框'
    )
    tool.click_action(
        '//*[@class="searchBtn"]',
        '查询按钮'
    )
    # 断言
    tool.equal_text_assert(
        '//table/tbody/tr[1]/td[7]',
        '表格中的保修天数',
        '364',
        "@结束@"
    )
    tool.mark_status()
    tool.finished()
    # 清理环境
    unbind_device([device_info[i]['id'] for i in range(len(device_info))])


if __name__ == "__main__":
    setting_warranty_period()