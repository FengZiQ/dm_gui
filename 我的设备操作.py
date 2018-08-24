# coding=utf-8
import time
from gui_test_tool import *


def my_device_operation():
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
    # 查找要操作的设备
    tool.fill_action(
        '//*[@id="queryDeviceId"]',
        '4113180400130999',
        '设备编号输入框'
    )
    tool.click_action(
        '//*[@class="searchBtn"]',
        '查询按钮'
    )
    # 点击设备详情刷新图标
    tool.click_action(
        '//a[@title="设备详情刷新"]',
        '设备详情刷新图标',
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '刷新状态成功'
    )

    # 点击详情图标
    tool.click_action(
        '//a[@title="详情"]',
        '详情图标'
    )
    # 断言
    expected_refresh_time = time.strftime('%Y-%m-%d %H-%M')
    tool.contained_text_assert(
        '//div[@id="mainInformation"]',
        '设备所有信息显示区域',
        ['4113180400130999', expected_refresh_time],
    )

    # 返回设备列表
    tool.click_action(
        '//*[@id="leftNav"]/li[3]/ul/li[2]',
        '我的设备标签',
    )
    # 点击设备号，进入设备详情
    tool.click_action(
        '//table/tbody/tr[1]/td[2]/a',
        '设备号(设备详情链接)'
    )
    # 断言：设备版本信息包含['设备编号', '销售日期', '激活日期', '保修期', '延保期']
    tool.contained_text_assert(
        'detailDeviceId',
        '设备版本信息显示区域',
        ['设备编号', '销售日期', '激活日期', '保修期', '延保期'],
        locator=By.ID
    )

    # 断言：设备版本信息包含['app', 'kernel', 'rootfs', 'uboot']
    tool.contained_text_assert(
        'versionTBody',
        '设备版本信息显示区域',
        ['app', 'kernel', 'rootfs', 'uboot'],
        locator=By.ID
    )

    # 断言：设备连接历史列表
    time_c = time.strftime('%Y-%m')
    tool.contained_text_assert(
        'historyTbody',
        '设备连接历史列表',
        [time_c],
        locator=By.ID
    )

    # 断言：设位置信息包含 ['设备所在地址', ' IP地址']
    tool.contained_text_assert(
        'ipLocation',
        '位置信息显示区域',
        ['设备所在地址', ' IP地址'],
        end='@结束@',
        locator=By.ID
    )

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    my_device_operation()
