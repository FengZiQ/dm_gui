# coding=utf-8
from gui_test_tool import *
from api_condition import *
from view_log import view_log

tool = GUITestTool()


def sum_common_config_issue():
    # 进入金额抓取通用配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[2]',
        '金额抓取通用配置标签'
    )
    # 配置名称输入框输入：测试_fengziqi
    tool.fill_action(
        'configName',
        '测试_fengziqi',
        '配置名称输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    #  点击下发图标, 进入下发页面
    tool.click_action(
        '//a[@title="下发"]',
        '下发图标'
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
        'searchBtn',
        '查询按钮',
        locator=By.CLASS_NAME
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
        '设备下发成功'
    )
    # 断言log是否触发
    cmd = 'tail -50f /data/log/inspos-dm-ppcp2.log | grep 4113180400130999'
    log_content = {'text': view_log(config_data['log_server1'], cmd)}
    if len(log_content['text']) <= len(cmd):
        log_content['text'] = view_log(config_data['log_server2'], cmd)
    tool.log_assert(
        log_content['text'],
        ['DeviceConfigHandler', 'msg=[{"deviceId":'],
        end='@结束@'
    )


def sum_common_config_batch_issue():
    # 点击下发图标, 进入下发页面
    tool.click_action(
        '//a[@title="下发"]',
        '下发图标'
    )
    # 点击批量下发按钮
    tool.click_action(
        'batchLssued',
        '批量下发按钮',
        By.ID
    )
    # 号段起始输入框: 4113180400130997
    tool.fill_action(
        'startNum',
        '4113180400130997',
        '号段起始输入框',
        locator=By.ID
    )
    # 号段起始输入框: 4113180400130999
    tool.fill_action(
        'endNum',
        '4113180400130999',
        '号段起始输入框',
        locator=By.ID
    )
    # 点击导入按钮
    tool.click_action(
        '//form[@id="myupload"]/div[1]/div[2]/input[4]',
        '导入按钮'
    )
    # 断言
    import_count = tool.wait_for_element(
        '//span[@class="prosperity"]',
        '成功导入的设备数量'
    )
    all_logs('期望结果：成功导入的设备数量应大于0小于等于3')
    all_logs('实际结果：成功导入的设备数量为：' + import_count)
    testlink('成功导入的设备数量为：' + import_count)
    try:
        if int(import_count) == 0 or int(import_count) > 3:
            tool.FailedFlag = True
            testlink('设备导入失败，成功导入设备数量为：' + import_count)
    except Exception as e:
        print(e)
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
        '设备下发成功'
    )
    # 断言log是否触发
    cmd = 'tail -50f /data/log/inspos-dm-ppcp2.log | grep 4113180400130999'
    log_content = {'text': view_log(config_data['log_server1'], cmd)}
    if len(log_content['text']) <= len(cmd):
        log_content['text'] = view_log(config_data['log_server2'], cmd)
    tool.log_assert(
        log_content['text'],
        ['DeviceConfigHandler', 'msg=[{"deviceId":'],
        end='@结束@'
    )


def sum_common_config_file_issue():
    # 前置条件：Excel表中A2/A3/A4单元格内容分别为 test/4113180400130999/124434235123153432212123/4113180400130999
    upload_excel_file(
        [
            'test', '4113180400130999',
            '124434235123153432212123', '4113180400130999'
        ],
        config_data['file_path'] + '金额抓取通用配置批量下发.xls'
    )
    # 点击下发图标，进入下发页面
    tool.click_action(
        '//a[@title="下发"]',
        '下发图标'
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
        config_data['file_path'] + '金额抓取通用配置批量下发.xls',
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
        '设备下发成功'
    )
    # 断言log是否触发
    cmd = 'tail -50f /data/log/inspos-dm-ppcp2.log | grep 4113180400130999'
    log_content = {'text': view_log(config_data['log_server1'], cmd)}
    if len(log_content['text']) <= len(cmd):
        log_content['text'] = view_log(config_data['log_server2'], cmd)
    tool.log_assert(
        log_content['text'],
        ['DeviceConfigHandler', 'msg=[{"deviceId":'],
        end='@结束@'
    )


if __name__ == "__main__":
    sum_common_config_issue()
    sum_common_config_batch_issue()
    sum_common_config_file_issue()
    tool.mark_status()
    tool.finished()

