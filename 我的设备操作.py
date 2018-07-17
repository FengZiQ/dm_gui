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
        '//table/tbody/tr/td[8]/a[2]/i',
        '设备详情刷新图标',
        By.XPATH,
        1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '刷新状态成功'
    )
    # 点击详情图标
    tool.click_action(
        '//table/tbody/tr/td[8]/a[1]/i',
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
        '/html/body/div[2]/div[2]/div[1]/span[2]/div/a[1]',
        '设备列表返回链接'
    )
    # 点击设备号，进入设备详情
    tool.click_action(
        '//table/tbody/tr[1]/td[2]/a',
        '设备号(设备详情链接)'
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/div/div/div/div/div/div[1]/div[1]/b',
        '设备版本显示区域',
        '设备版本'
    )
    tool.contained_text_assert(
        '/html/body/div/div/div/div/div/div/div/div[1]/div[2]/span[2]',
        '销售日期显示区域',
        ['销售日期:']
    )
    tool.contained_text_assert(
        '/html/body/div/div/div/div/div/div/div/div[1]/div[2]/span[3]',
        '激活日期显示区域',
        ['激活日期:']
    )
    tool.contained_text_assert(
        '/html/body/div/div/div/div/div/div/div/div[1]/div[2]/span[4]',
        '保修期显示区域',
        ['保修期:']
    )
    tool.equal_text_assert(
        '/html/body/div/div/div/div/div/div/div/div[2]/div[1]/b',
        '设备连接历史列表显示区域',
        '设备连接历史列表'
    )
    tool.equal_text_assert(
        '/html/body/div/div/div/div/div/div/div/div[3]/div[1]/b',
        '位置信息显示区域',
        '位置信息'
    )
    tool.contained_text_assert(
        '/html/body/div/div/div/div/div/div/div/div[3]/div[2]/span[1]',
        '设备所在地址显示区域',
        ['中国', '北京']
    )
    tool.contained_text_assert(
        '/html/body/div/div/div/div/div/div/div/div[3]/div[2]/span[2]',
        'IP地址显示区域',
        ['1', '.'],
        '@结束@'
    )
    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    my_device_operation()
