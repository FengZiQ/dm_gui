# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()

# 前置条件：创建一个名为“测试全局配置下发服务商”无开发能力服务商并销售15台设备
new_customer('测试全局配置下发服务商')
cus_info = customer_info('测试全局配置下发服务商')
# 销售设备
device_info = get_unsold_device_info()
bind_device(
    cus_info['id'],
    cus_info['treeId'],
    [device_info[i]['id'] for i in range(len(device_info))]
)
# 生产一个批量下发的Excel表
upload_excel_file(
    [device_info[i]['serialNum'] for i in range(len(device_info))],
    config_data['file_path'] + '全局配置批量下发.xls'
)
# 增加一个名为“全局配置查询测试”的全局配置
config_id = add_global_config('全局配置下发测试')


def device_no_issue():
    # 进入全局配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[10]',
        '全局配置标签'
    )
    # 配置名称输入框：全局配置查询测试
    tool.fill_action(
        'configName',
        '全局配置下发测试',
        '配置名称输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 点击配置下发选择设备图标，进入下发页面
    tool.click_action(
        '//a[@title="配置下发选择设备"]',
        '配置下发选择设备图标'
    )
    # 查询要绑定的设备
    tool.fill_action(
        'queryDeviceId',
        device_info[0]['serialNum'],
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
    # 点击确认下发按钮
    tool.click_action(
        'addDeviceBtn',
        '确认下发按钮',
        By.CLASS_NAME,
        response_time=2
    )
    # 点击确定按钮
    tool.click_action(
        'ok',
        '确定按钮',
        By.CLASS_NAME,
        response_time=2
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '配置下发成功',
        end='@结束@'
    )


def file_batch_issue():
    time.sleep(5)
    # 点击配置下发选择设备图标，进入下发页面
    tool.click_action(
        '//a[@title="配置下发选择设备"]',
        '配置下发选择设备图标'
    )
    # 点击批量下发按钮
    tool.click_action(
        'batchLssued',
        '批量下发按钮',
        locator=By.ID
    )
    # 上传批量文件
    tool.fill_action(
        'file',
        config_data['file_path'] + '全局配置批量下发.xls',
        '浏览图标',
        locator=By.ID
    )
    # 点击导入按钮
    tool.click_action(
        '//form[@id="myupload"]/div[1]/div[2]/input[3]',
        '导入按钮',
        response_time=30
    )
    # 断言
    tool.contained_text_assert(
        '//div[@id="bulk"]/div/div/div[2]',
        '导入结果显示区域',
        ['成功导入：15台', '未成功导入：0台']
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
        '配置下发成功',
        end='@结束@'
    )


if __name__ == "__main__":
    device_no_issue()
    file_batch_issue()
    tool.mark_status()
    tool.finished()
    # 清理环境
    del_global_config(config_id)
    delete_customer(cus_info['id'])
