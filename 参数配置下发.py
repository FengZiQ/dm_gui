# coding=utf-8
from gui_test_tool import *
from api_condition import *
from view_log import view_log

tool = GUITestTool()


def precondition():
    # 销售设备
    unsold_d = get_unsold_device_info()
    bind_device('44', '0010025', [unsold_d[i]['id'] for i in range(len(unsold_d))])
    upload_excel_file(
        [unsold_d[i]['serialNum'] for i in range(len(unsold_d))],
        config_data['file_path'] + '参数配置批量下发测试.xls'
    )
    return unsold_d


device_info = precondition()


def one_device_issue():
    # 参数配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[1]',
        '参数配置标签'
    )
    # 查询
    tool.fill_action(
        'serialNum',
        device_info[0]['serialNum'],
        '设备编号输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 进入下发页面
    tool.click_action(
        '//a[@title="下发设备列表"]',
        '下发设备列表图标'
    )
    # 查询要下发的设备
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
    # 点击确认下发
    tool.click_action(
        'addDeviceBtn',
        '确认下发按钮',
        By.CLASS_NAME
    )
    # 点击确定按钮
    tool.click_action(
        'ok',
        '提示框的确定按钮',
        By.CLASS_NAME,
        response_time=1
    )
    # 断言提示消息
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '设备下发成功'
    )
    # 断言log是否触发
    cmd = 'tail -n 100 /data/log/inspos-dm-ppcp2.log | grep ' + device_info[0]['serialNum']
    log_content = {'text': view_log(config_data['log_server1'], cmd)}
    if len(log_content['text']) <= len(cmd):
        log_content['text'] = view_log(config_data['log_server2'], cmd)
    tool.log_assert(
        log_content['text'],
        ['PayChannelHandler', 'msg={"channelId":'],
        end='@结束@'
    )


def file_issue():
    # 查询
    tool.fill_action(
        'serialNum',
        device_info[0]['serialNum'],
        '设备编号输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 进入下发页面
    tool.click_action(
        '//a[@title="下发设备列表"]',
        '下发设备列表图标'
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
        config_data['file_path'] + '参数配置批量下发测试.xls',
        '批量文件图标',
        locator=By.ID
    )
    # 点击导入
    tool.click_action(
        '//form[@id="myupload"]/div[1]/div[2]/input[6]',
        '导入按钮'
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
        '设备下发成功'
    )
    # 断言log是否触发
    cmd = 'tail -n 100 /data/log/inspos-dm-ppcp2.log | grep ' + device_info[0]['serialNum']
    log_content = {'text': view_log(config_data['log_server1'], cmd)}
    if len(log_content['text']) <= len(cmd):
        log_content['text'] = view_log(config_data['log_server2'], cmd)
    tool.log_assert(
        log_content['text'],
        ['PayChannelHandler', 'msg={"channelId":'],
        end='@结束@'
    )


def batch_issue():
    # 参数配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[1]',
        '参数配置标签'
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
    # 进入下发页面
    tool.click_action(
        '//a[@title="下发设备列表"]',
        '下发设备列表图标'
    )
    # 点击批量下发按钮
    tool.click_action(
        'batchLssued',
        '批量下发按钮',
        locator=By.ID
    )
    # 输入号段
    tool.fill_action(
        'startNum',
        '4113180400130999',
        '起始号段输入框',
        locator=By.ID
    )
    tool.fill_action(
        'endNum',
        '4113180400131001',
        '起始号段输入框',
        locator=By.ID
    )
    # 点击导入
    tool.click_action(
        '//form[@id="myupload"]/div[1]/div[2]/input[6]',
        '导入按钮'
    )
    # 断言
    tool.contained_text_assert(
        '//div[@id="bulk"]/div/div/div[2]',
        '导入结果显示区域',
        ['成功导入：1台', '未成功导入：2台']
    )
    # 点击设备下发按钮
    tool.click_action(
        '//form[@id="myupload"]/div[2]/input',
        '设备下发按钮'
    )
    # 点击确定按钮
    tool.click_action(
        'ok',
        '提示框的确定按钮',
        By.CLASS_NAME,
        response_time=2
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '设备下发成功'
    )
    # 断言log是否触发
    cmd = 'tail -n 500 /data/log/inspos-dm-ppcp2.log | grep 4113180400130999'
    log_content = {'text': view_log(config_data['log_server1'], cmd)}
    if len(log_content['text']) <= len(cmd):
        log_content['text'] = view_log(config_data['log_server2'], cmd)
    tool.log_assert(
        log_content['text'],
        ['PayChannelHandler', 'msg={"channelId":'],
        end='@结束@'
    )


if __name__ == "__main__":
    one_device_issue()
    file_issue()
    batch_issue()
    tool.mark_status()
    tool.finished()
    # 清理环境
    unbind_device([device_info[i]['id'] for i in range(len(device_info))])
