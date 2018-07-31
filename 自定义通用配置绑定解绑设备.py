# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()


def precondition():
    # 销售设备
    unsold_d = get_unsold_device_info()
    bind_device('44', '0010025', [unsold_d[i]['id'] for i in range(len(unsold_d))])
    upload_excel_file(
        [unsold_d[i]['serialNum'] for i in range(len(unsold_d))],
        config_data['file_path'] + '自定义通用配置批量绑定解绑测试.xls'
    )
    return unsold_d


device_info = precondition()


def one_device_bind():
    # 进入自定义通用配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[5]',
        '自定义通用配置标签'
    )
    # 查询
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
    # 进入解绑设备列表页面
    tool.click_action(
        '//a[@title="解绑设备列表"]',
        '解绑设备列表图标'
    )
    # 点击设备绑定按钮
    tool.click_action(
        'definedBind',
        '设备绑定按钮',
        locator=By.ID
    )
    # 查询要绑定的设备
    tool.fill_action(
        'queryDeviceId',
        device_info[0]['serialNum'],
        '设备编号输入框',
        locator=By.ID
    )
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 选定设备
    tool.click_action(
        '//table/tbody/tr/th[1]/div/ins',
        '选定设备复选框'
    )
    # 点击确认绑定按钮
    tool.click_action(
        'addDeviceBtn',
        '确认绑定按钮',
        By.CLASS_NAME
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
        '设备绑定成功',
        '@结束@'
    )


def one_device_unbind():
    time.sleep(5)
    # 在自定义通用配置设备解绑列表查询要解绑的设备
    tool.fill_action(
        'queryDeviceId',
        device_info[0]['serialNum'],
        '设备编号输入框',
        locator=By.ID
    )
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 选定设备
    tool.click_action(
        '//table/tbody/tr/th[1]/div/ins',
        '选定设备复选框'
    )
    # 点击确认解绑按钮
    tool.click_action(
        'addDeviceBtn',
        '确认解绑按钮',
        By.CLASS_NAME
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
        '设备解绑成功',
        '@结束@'
    )


def batch_bind():
    time.sleep(5)
    # 进入自定义通用配置设备解绑列表
    tool.click_action(
        '//a[@title="解绑设备列表"]',
        '解绑设备列表图标'
    )
    # 点击设备绑定按钮
    tool.click_action(
        'definedBind',
        '设备绑定按钮',
        locator=By.ID
    )
    # 点击批量绑定按钮
    tool.click_action(
        'definedBind',
        '批量绑定按钮',
        locator=By.ID
    )
    # 上传批量绑定文件
    tool.fill_action(
        'file',
        config_data['file_path'] + '自定义通用配置批量绑定解绑测试.xls',
        '批量文件图标',
        locator=By.ID
    )
    # 点击导入文件图标
    tool.click_action(
        '//form[@id="myupload"]/div[1]/div/input[7]',
        '导入文件图标'
    )
    # 断言
    tool.contained_text_assert(
        '//div[@id="definedBatchBind"]/div/div/div[2]',
        '导入结果显示区域',
        ['成功导入：15台', '未成功导入：0台']
    )
    # 点击确认绑定图标
    tool.click_action(
        '//form[@id="myupload"]/div[2]/input',
        '确认绑定图标'
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
        '设备绑定成功',
        '@结束@'
    )


def batch_unbind():
    time.sleep(5)
    # 在自定义通用配置设备解绑列表点击批量解绑按钮
    tool.click_action(
        'definedUnbind',
        '批量解绑按钮',
        locator=By.ID
    )
    # 上传批量绑定文件
    tool.fill_action(
        'file',
        config_data['file_path'] + '自定义通用配置批量绑定解绑测试.xls',
        '批量文件图标',
        locator=By.ID
    )
    # 点击导入文件图标
    tool.click_action(
        '//form[@id="myupload"]/div[1]/div/input[7]',
        '导入文件图标'
    )
    # 断言
    tool.contained_text_assert(
        '//div[@id="definedBatchUnbind"]/div/div/div[2]',
        '导入结果显示区域',
        ['成功导入：15台', '未成功导入：0台']
    )
    # 点击确解绑定图标
    tool.click_action(
        '//form[@id="myupload"]/div[2]/input',
        '确认解绑图标'
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
        '设备解绑成功',
        '@结束@'
    )


if __name__ == "__main__":
    one_device_bind()
    one_device_unbind()
    batch_bind()
    batch_unbind()
    tool.mark_status()
    tool.finished()
    # 清理环境
    unbind_device([device_info[i]['id'] for i in range(len(device_info))])