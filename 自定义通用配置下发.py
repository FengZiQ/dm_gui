# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()


def one_device_issue():
    # 进入自定义通用配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[5]',
        '自定义通用配置标签'
    )
    # 设备编号输入框输入绑定的设备号
    tool.fill_action(
        'serialNum',
        '4113180400130999',
        '设备编号输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 点击下发设备列表图标，进入下发页面
    tool.click_action(
        '//a[@title="下发设备列表"]',
        '下发设备列表图标'
    )
    # 设备编号输入框输入：4113180400130999
    tool.fill_action(
        'queryDeviceId',
        '4113180400130999',
        '设备编号输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 选择设备
    tool.click_action(
        '//table/tbody/tr/th[1]/div/ins',
        '选择复选框'
    )
    # 点击确认下发按钮
    tool.click_action(
        'addDeviceBtn',
        '确认下发按钮',
        locator=By.CLASS_NAME
    )
    # 点击提示框中的确定按钮
    tool.click_action(
        'ok',
        '确定按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '设备下发成功',
        end='@结束@'
    )


def file_issue():
    # 前置条件：Excel表中A2/A3/A4单元格内容分别为 test/4113180400130999/124434235123153432212123/4113180400130999
    upload_excel_file(
        [
            'test', '4113180400130999',
            '124434235123153432212123', '4113180400130999'
        ],
        config_data['file_path'] + '自定义通用配置批量下发.xls'
    )
    time.sleep(5)
    # 点击下发设备列表图标，进入下发页面
    tool.click_action(
        '//a[@title="下发设备列表"]',
        '下发设备列表图标'
    )
    # 点击批量下发按钮
    tool.click_action(
        'batchLssued',
        '批量下发按钮',
        By.ID
    )
    # 上传批量文件
    tool.fill_action(
        'file',
        config_data['file_path'] + '自定义通用配置批量下发.xls',
        '浏览图标',
        locator=By.ID
    )
    # 点击导入按钮
    tool.click_action(
        '//form[@id="myupload"]/div[1]/div[2]/input[4]',
        '导入按钮'
    )
    # 断言
    tool.contained_text_assert(
        '//div[@id="bulk"]/div/div/div[2]',
        '导入结果显示区域',
        ['成功导入：1台', '未成功导入：2台', 'test', '124434235123153432212123']
    )
    # 点击设备下发按钮
    tool.click_action(
        '//form[@id="myupload"]/div[2]/input',
        '设备下发按钮'
    )
    # 点击保存按钮
    tool.click_action(
        'ok',
        '确定按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '设备下发成功',
        end='@结束@'
    )


if __name__ == "__main__":
    one_device_issue()
    file_issue()
    tool.mark_status()
    tool.finished()

