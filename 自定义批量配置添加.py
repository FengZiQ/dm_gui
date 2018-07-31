# coding=utf-8
from gui_test_tool import *
from api_condition import *
from selenium.webdriver.common.keys import Keys

tool = GUITestTool()


def add_by_one_device_no():
    # 进入自定义批量配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[7]',
        '自定义批量配置标签'
    )
    # 服务商选择：测试账户
    tool.click_action(
        '//button[@data-id="customerId"]',
        '服务商选择下拉按钮'
    )
    # 搜索服务商
    tool.fill_action(
        '//input[@aria-label="Search"]',
        '测试账户',
        '服务商搜索框'
    )
    # 回车选定
    tool.fill_action(
        '//input[@aria-label="Search"]',
        Keys.ENTER,
        '服务商搜索框',
        response_time=3
    )
    # 点击添加按钮
    tool.click_action(
        'addbtn',
        '添加按钮',
        locator=By.ID
    )
    # 商户号输入框：测试_add
    tool.fill_action(
        'merchantNumInput',
        '测试_add',
        '商户号输入框',
        locator=By.NAME
    )
    # 设备编号输入框：4113180400130999
    tool.fill_action(
        'serialNumInput',
        '4113180400130999',
        '设备编号输入框',
        locator=By.NAME
    )
    # 点击导入按钮
    tool.click_action(
        '//form[@id="myupload"]/div[1]/div[2]/button',
        '导入按钮'
    )
    # 断言
    tool.contained_text_assert(
        '//div[@id="addBatchConfig"]/div/div/div[2]',
        '导入结果显示区域',
        ['成功导入：1台', '未成功导入：0台']
    )
    # 点击保存并下发按钮
    tool.click_action(
        'saveButton',
        '保存并下发按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '文件保存并下发成功',
        end='@结束@'
    )


def file_issue():
    # 前置条件：Excel表中A2/A3/A4单元格内容分别为 test/4113180400130999/124434235123153432212123/4113180400130999
    try:
        device_no = [
            'test', '4113180400130999',
            '124434235123153432212123', '4113180400130999'
        ]
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('Sheet1')
        for i in range(len(device_no)):
            worksheet.write(i + 1, 0, device_no[i])
            worksheet.write(i + 1, 1, '通过文件_add')
        workbook.save(config_data['file_path'] + '自定义批量配置批量下发.xls')
    except:
        pass

    time.sleep(5)
    # 点击添加按钮
    tool.click_action(
        'addbtn',
        '添加按钮',
        locator=By.ID
    )
    # 上传批量文件
    tool.fill_action(
        'file',
        config_data['file_path'] + '自定义批量配置批量下发.xls',
        '浏览图标',
        locator=By.ID
    )
    # 点击导入按钮
    tool.click_action(
        '//form[@id="myupload"]/div[1]/div[2]/button',
        '导入按钮'
    )
    # 断言
    tool.contained_text_assert(
        '//div[@id="addBatchConfig"]/div/div/div[2]',
        '导入结果显示区域',
        ['成功导入：1台', '未成功导入：2台', 'test', '124434235123153432212123']
    )
    # 点击保存并下发按钮
    tool.click_action(
        'saveButton',
        '保存并下发按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '文件保存并下发成功',
        end='@结束@'
    )


if __name__ == "__main__":
    add_by_one_device_no()
    file_issue()
    tool.mark_status()
    tool.finished()
    # 清理环境
    config_id = get_self_batch_config_id('4113180400130999')
    del_self_batch_config(config_id)
