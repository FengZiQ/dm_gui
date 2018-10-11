# coding=utf-8
from gui_test_tool import *
from selenium.webdriver.common.keys import Keys


def device_batch_upgrade():
    tool = GUITestTool()

    # 进入设备升级页
    tool.click_action(
        '//*[@id="leftNav"]/li[3]',
        '设备管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[3]/ul/li[4]',
        '设备升级标签',
        response_time=5
    )
    # 查询：选择测试账户服务商
    tool.click_action(
        '//button[@data-id="customerId"]',
        '服务商下拉列表'
    )
    # 搜索服务商测试账户
    tool.fill_action(
        '//input[@aria-label="Search"]',
        '测试账户',
        '服务商搜索输入框'
    )
    tool.fill_action(
        '//input[@aria-label="Search"]',
        Keys.ENTER,
        '服务商搜索输入框',
        response_time=5
    )
    # 点击设备升级按钮
    tool.click_action(
        'addbtn',
        '设备升级按钮',
        locator=By.ID
    )
    # 上传文件
    tool.fill_action(
        'file',
        config_data['file_path'] + 'A2设备升级批量文件.xls',
        '浏览上传文件框',
        locator=By.ID,
        response_time=3
    )
    # 点击设备导入按钮
    tool.click_action(
        'affirm',
        '设备导入按钮',
        locator=By.CLASS_NAME
    )
    time.sleep(3)
    # 断言
    tool.contained_text_assert(
        '//div[@id="batchUpdate"]/div/div/div[2]',
        '导入结果显示区域',
        ['成功导入：1台', '未成功导入：1台', '以下均为未成功设备号：']
    )
    # 点击下一步按钮
    tool.click_action(
        'affirm',
        '下一步按钮',
        locator=By.CLASS_NAME,
        response_time=5
    )
    # 选择软件
    tool.click_action(
        '//table[@id="upgradeTbl"]/tbody/tr[1]/td[1]/div/ins',
        '选择BasePayDDB'
    )
    # 选择升级版本
    tool.click_action(
        '//table[@id="upgradeTbl"]/tbody/tr[1]/td[3]/select/option[1]',
        '选择版本1.4.13'
    )
    # 点击确认升级按钮
    tool.click_action(
        'saveButton',
        '确认升级按钮',
        locator=By.CLASS_NAME
    )
    # 点击确定按钮
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
        '升级指令已下发到您指定的1台设备。',
        end='@结束@'
    )

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    device_batch_upgrade()
