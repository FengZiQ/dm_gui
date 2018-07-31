# coding=utf-8
from gui_test_tool import *
from api_condition import *
from selenium.webdriver.common.keys import Keys

tool = GUITestTool()


def precondition():
    # 销售设备
    unsold_d = get_unsold_device_info()
    bind_device('44', '0010025', [unsold_d[i]['id'] for i in range(len(unsold_d))])
    return unsold_d


device_info = precondition()


def device_bind():
    # 进入票据解析页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[9]',
        '票据解析标签'
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
    # 模板名称输入框：测试_fengziqi
    tool.fill_action(
        'templateName',
        '测试_fengziqi',
        '模板名称输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'searchBtn',
        '查询按钮',
        locator=By.CLASS_NAME
    )
    # 点击设备列表图标进入绑定解绑页面
    tool.click_action(
        '//a[@title="设备列表"]',
        '设备列表图标'
    )
    # 点击添加设备按钮
    tool.click_action(
        'addbtn',
        '添加设备按钮',
        locator=By.ID
    )
    # 查询要绑定的设备
    for i in range(3):
        tool.fill_action(
            'queryDeviceId',
            device_info[i]['serialNum'],
            '设备编号输入框',
            locator=By.ID
        )
        tool.click_action(
            'searchBtn',
            '查询按钮',
            locator=By.CLASS_NAME
        )
        # 选定设备
        tool.click_action(
            '//table/tbody/tr/th[1]/div/ins',
            '选定设备复选框',
            response_time=1
        )
    # 点击确认添加按钮
    tool.click_action(
        'addDeviceBtn',
        '确认添加按钮',
        By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '设备添加成功',
        '@结束@'
    )


def device_unbind():
    time.sleep(5)
    # 在票据解析设备列表页选定要解绑的设备
    tool.click_action(
        '//table/tbody/tr/th[1]/div/ins',
        '选定设备复选框'
    )
    # 点击解绑设备按钮
    tool.click_action(
        'unwrap',
        '解绑设备按钮',
        By.ID
    )
    # 点击确定按钮
    tool.click_action(
        'ok',
        '提示框的确定按钮',
        By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '设备解绑成功'
    )
    time.sleep(3)
    tool.equal_text_assert(
        '//table[@id="devicesTable"]/tbody/tr/td',
        '查询结果列表',
        '该查询条件下暂时没有设备',
        '@结束@'
    )


if __name__ == "__main__":
    device_bind()
    device_unbind()
    tool.mark_status()
    tool.finished()
    # 清理环境
    unbind_device([device_info[i]['id'] for i in range(len(device_info))])