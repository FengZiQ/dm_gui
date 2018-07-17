# coding=utf-8
from api_condition import *
from gui_test_tool import *


def precondition():
    # 销售15台设备给测试账户，并将设备号保存在Excel中
    unsold_d = get_unsold_device_info()
    try:
        upload_excel_file(unsold_d, config_data['file_path'] + '批量设置保修期.xls')
    except Exception as e:
        print(e)
    bind_device(
        '44',
        '0010025',
        [unsold_d[i]['id'] for i in range(len(unsold_d))]
    )
    return unsold_d


def batch_setting_warranty_period():
    # 前置条件：销售15台设备给测试账户，并将设备号保存在Excel中
    device_info = precondition()

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
    # 保修期设置按钮
    tool.click_action(
        '//button[@id="periodSet"]',
        '保修期设置按钮'
    )
    # 选择批量文件
    tool.driver.find_element_by_id('deviceFile').send_keys(config_data['file_path'] + '批量设置保修期.xls')
    # 输入保修期与延保期
    tool.fill_action(
        'guarantee',
        '1',
        '保修期输入框',
        By.NAME
    )
    tool.fill_action(
        'delayGuarantee',
        '1',
        '延保期输入框',
        By.NAME
    )
    # 保存按钮
    tool.click_action(
        '/html/body/div/div/div/div/div/div/div/div[2]/button[1]',
        '保存按钮',
        By.XPATH,
        1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '保修期批量设置成功'
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
        '表格中的保修天数',
        '729'
    )
    # 查询
    tool.fill_action(
        '//*[@id="queryDeviceId"]',
        device_info[1]['serialNum'],
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
        '729',
        end='@结束@'
    )
    tool.mark_status()
    tool.finished()
    # 清理环境
    unbind_device([device_info[i]['id'] for i in range(len(device_info))])


if __name__ == "__main__":
    batch_setting_warranty_period()