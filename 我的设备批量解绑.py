# coding=utf-8
from api_condition import *
from gui_test_tool import *


def precondition():
    # 销售设备
    unsold_d = get_unsold_device_info()
    bind_device('44', '0010025', [unsold_d[i]['id'] for i in range(len(unsold_d))])
    upload_excel_file(
        [unsold_d[i]['serialNum'] for i in range(len(unsold_d))],
        config_data['file_path'] + '批量解绑测试.xls'
    )
    return unsold_d


def my_device_batch_unbind():
    # 测试数据
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
    # 解绑按钮
    tool.click_action(
        '//button[@id="unwrap"]',
        '解绑按钮'
    )
    # 选择批量文件
    tool.driver.find_element(By.ID, 'unbindFile').send_keys(config_data['file_path'] + '批量解绑测试.xls')
    # 点击一键解绑按钮
    tool.click_action(
        '//form[@id="mybindFile"]/div[2]/input',
        '一键解绑按钮',
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '批量解绑成功'
    )
    # 我的设备列表查询结果
    tool.fill_action(
        '//*[@id="queryDeviceId"]',
        device_info[0]['serialNum'],
        '设备编号输入框'
    )
    tool.click_action(
        '//*[@class="searchBtn"]',
        '查询按钮'
    )
    # 断言：查询结果列表
    tool.equal_text_assert(
        'devicesTable',
        '查询结果列表',
        '查询不到数据!',
        locator=By.ID
    )
    # 未销售列表查询
    tool.click_action(
        '//*[@id="leftNav"]/li[3]/ul/li[1]',
        '未销售列表标签',
    )
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
        'fontbold',
        '未销售列表中list count',
        '1',
        end='@结束@',
        locator=By.CLASS_NAME
    )
    tool.mark_status()
    tool.finished()
    # 清理环境
    unbind_device([device_info[i]['id'] for i in range(len(device_info))])


if __name__ == "__main__":
    my_device_batch_unbind()
