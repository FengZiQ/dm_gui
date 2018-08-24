# coding=utf-8
from gui_test_tool import *
from api_condition import *
from selenium.webdriver.common.keys import Keys
from view_log import view_log


# 前置条件：服务商“测试账户”存在自定义语音模板，清空“测试账户”自定义语音
def clear_test_account_config():
    try:
        res0 = session.get(
            server + 'voiceConfig/pageList'
        )
        temp0 = json.loads(res0.text)
        all_config_info = temp0['data']['list']
        config_id = [int(d['id']) for d in all_config_info if d['customerName'] == '测试账户']
        if config_id:
            res1 = session.get(
                server + 'deviceVoice/pageList?voiceConfigId=' + str(config_id[0])
            )
            temp1 = json.loads(res1.text)
            device_info = temp1['data']['list']
            id_list = [int(d['id']) for d in device_info]
            session.post(
                server + 'deviceVoice/deletes',
                json=id_list
            )
            session.post(
                server + 'voiceConfig/deletes',
                json={'id': config_id[0]}
            )
    except Exception as e:
        print(e)
        print('清空“测试账户”自定义语音失败')


tool = GUITestTool()


def add_self_scene():
    # 进入自定义语音页
    tool.click_action(
        '//*[@id="leftNav"]/li[5]',
        '系统定制标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[5]/ul/li[3]',
        '自定义语音标签'
    )
    # 点击添加定制按钮
    tool.click_action(
        'addbtn',
        '添加定制按钮',
        locator=By.ID,
        response_time=5
    )
    # 自定义语音名称输入框：test_add自定义语音
    tool.fill_action(
        'name',
        'test_add自定义语音',
        '自定义语音名称输入框',
        locator=By.ID
    )
    # 选择服务商
    tool.click_action(
        '//button[@data-id="customerId"]',
        '服务商选择下拉按钮'
    )
    # 搜索服务商: 测试账户
    tool.fill_action(
        '//input[@aria-label="Search"]',
        '测试账户',
        '服务商搜索框'
    )
    # 回车选定
    tool.fill_action(
        '//input[@aria-label="Search"]',
        Keys.ENTER,
        '服务商搜索框'
    )
    # 选择一条语音场景
    tool.click_action(
        '//tbody[@id="tbodyContent"]/tr/td[1]/select/option[1]',
        '语音场景下拉框'
    )
    # 点击播放图标
    tool.click_action(
        '//tbody[@id="tbodyContent"]/tr/td[5]/i',
        '播放图标'
    )
    # 点击增加语音图标
    tool.click_action(
        'keyAdd',
        '增加语音图标',
        locator=By.CLASS_NAME
    )
    # 选择二条语音场景
    tool.click_action(
        '//tbody[@id="tbodyContent"]/tr[2]/td[1]/select/option[1]',
        '语音场景下拉框'
    )
    # 点击删除图标
    tool.click_action(
        '//tbody[@id="tbodyContent"]/tr[2]/td[6]/i',
        '删除图标'
    )
    # 点击增加语音图标
    tool.click_action(
        'keyAdd',
        '增加语音图标',
        locator=By.CLASS_NAME
    )
    # 选择二条语音场景
    tool.click_action(
        '//tbody[@id="tbodyContent"]/tr[2]/td[1]/select/option[1]',
        '语音场景下拉框'
    )
    # 点击保存按钮
    tool.click_action(
        'saveBtn',
        '保存按钮',
        locator=By.CLASS_NAME,
        response_time=2
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '新增自定义语音成功',
        end='@结束@'
    )


def query_scene():
    time.sleep(3)
    # 语音名称输入框: test_add自定义语音
    tool.fill_action(
        'name',
        'test_add自定义语音',
        '语音名称输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 断言
    tool.equal_text_assert(
        'fontbold',
        'list count',
        '1',
        end='@结束@',
        locator=By.CLASS_NAME
    )
    # 点击详情图标，进入详情页面
    tool.click_action(
        '//a[@title="详情"]',
        '详情图标'
    )
    # 断言
    tool.contained_text_assert(
        'definedConfigForm',
        '自定义语音详情显示区域',
        [
            '自定义语音名称', '服务商',
            '自定义语音模板', '情景语音位置',
            '语音文件', '播放', '操作'
        ],
        end='@结束@',
        locator=By.ID
    )


def modify_scene():
    tool.driver.back()
    time.sleep(5)
    # 点击修改图标，进入修改页面
    tool.click_action(
        '//a[@title="修改"]',
        '修改图标'
    )
    # 自定义语音名称输入框：test_add自定义语音modify
    tool.fill_action(
        'name',
        'test_add自定义语音modify',
        '自定义语音名称输入框',
        locator=By.ID
    )
    # 去掉一个场景
    tool.click_action(
        '//tbody[@id="tbodyContent"]/tr[2]/td[6]/i',
        '删除图标'
    )
    # 点击保存按钮
    tool.click_action(
        'saveBtn',
        '保存按钮',
        locator=By.CLASS_NAME,
        response_time=2
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改语音定制信息成功',
        end='@结束@'
    )
    time.sleep(3)
    # 点击修改图标，进入修改页面
    tool.click_action(
        '//a[@title="修改"]',
        '修改图标'
    )
    # 点击增加语音图标
    tool.click_action(
        'keyAdd',
        '增加语音图标',
        locator=By.CLASS_NAME
    )
    # 选择二条语音场景
    tool.click_action(
        '//tbody[@id="tbodyContent"]/tr[2]/td[1]/select/option[1]',
        '语音场景下拉框'
    )
    # 点击保存按钮
    tool.click_action(
        'saveBtn',
        '保存按钮',
        locator=By.CLASS_NAME,
        response_time=2
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改语音定制信息成功',
        end='@结束@'
    )


def bind_device():
    time.sleep(5)
    # 点击解绑设备列表图标，进入设备解绑列表页面
    tool.click_action(
        '//a[@title="解绑设备列表"]',
        '解绑设备列表图标'
    )
    # 点击设备绑定按钮
    tool.click_action(
        'soundBind',
        '设备绑定按钮',
        locator=By.ID
    )
    # 选择要绑定的设备
    for i in range(3):
        tool.click_action(
            '//table/tbody/tr[' + str(i+1) + ']/td[1]/div/ins',
            '选择设备复选框',
            response_time=1
        )
    # 点击确认绑定按钮
    tool.click_action(
        'addDeviceBtn',
        '确认绑定按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 点击提示窗中的确定按钮
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
        '设备绑定成功',
        end='@结束@'
    )
    # 前置条件：Excel表中A2/A3/A4单元格内容分别为 test/4113180400130999/124434235123153432212123/4113180400130999
    upload_excel_file(
        [
            'test', '4113180400130999',
            '124434235123153432212123', '4113180400130999'
        ],
        config_data['file_path'] + '自定义语音批量下发.xls'
    )
    # 点击设备绑定按钮
    tool.click_action(
        'soundBind',
        '设备绑定按钮',
        locator=By.ID
    )
    # 点击批量绑定按钮
    tool.click_action(
        'soundBind',
        '批量绑定按钮',
        locator=By.ID
    )
    # 上传文件
    tool.fill_action(
        'file',
        config_data['file_path'] + '自定义语音批量下发.xls',
        '浏览图标',
        locator=By.ID
    )
    # 点击导入按钮
    tool.click_action(
        '//form[@id="myupload"]/div[1]/div/input[6]',
        '导入按钮'
    )
    # 断言
    tool.contained_text_assert(
        '//div[@id="batchSoundBind"]/div/div/div[2]',
        '导入结果显示区域',
        ['成功导入：1台', '未成功导入：2台', 'test', '124434235123153432212123']
    )
    # 点击确认绑定按钮
    tool.click_action(
        'affirm',
        '确认绑定按钮',
        locator=By.CLASS_NAME
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
        '设备绑定成功',
        end='@结束@'
    )


def scene_issue():
    time.sleep(3)
    # 点击自定义语音标签
    tool.click_action(
        '//*[@id="leftNav"]/li[5]/ul/li[3]',
        '自定义语音标签'
    )
    # 点击下发设备列表图标，进入下发页面
    tool.click_action(
        '//a[@title="下发设备列表"]',
        '下发设备列表图标'
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
    # 断言提示消息
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '设备下发成功'
    )
    # 断言log是否触发
    cmd = 'tail -n 500 /data/log/inspos-dm-ppcp2.log | grep "4113180400130999"'
    log_content = {'text': view_log(config_data['log_server1'], cmd)}
    if len(log_content['text']) <= len(cmd):
        log_content['text'] = view_log(config_data['log_server2'], cmd)
    tool.log_assert(
        log_content['text'],
        ['DeviceVoiceConfigHandler', 'msg={"deviceNoList":', '"voiceConfigId"'],
        end='@结束@'
    )


def unbind_device():
    time.sleep(5)
    # 点击解绑设备列表图标，进入设备解绑列表页面
    tool.click_action(
        '//a[@title="解绑设备列表"]',
        '解绑设备列表图标'
    )
    # 选择要解绑的设备
    for i in range(3):
        tool.click_action(
            '//table/tbody/tr[' + str(i+1) + ']/td[1]/div/ins',
            '选择设备复选框',
            response_time=1
        )
    # 点击确认解绑按钮
    tool.click_action(
        'addDeviceBtn',
        '确认解绑按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 点击提示窗中的确定按钮
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
        '设备解绑成功',
        end='@结束@'
    )
    time.sleep(5)
    # 点击解绑设备列表图标，进入设备解绑列表页面
    tool.click_action(
        '//a[@title="解绑设备列表"]',
        '解绑设备列表图标'
    )
    # 点击批量解绑按钮
    tool.click_action(
        'soundUnbind',
        '批量解绑按钮',
        locator=By.ID,
        response_time=1
    )
    # 上传文件
    tool.fill_action(
        'file',
        config_data['file_path'] + '自定义语音批量下发.xls',
        '浏览图标',
        locator=By.ID
    )
    # 点击导入按钮
    tool.click_action(
        '//form[@id="myupload"]/div[1]/div/input[6]',
        '导入按钮'
    )
    # 断言
    tool.contained_text_assert(
        '//div[@id="soundBatchUnbind"]/div/div/div[2]',
        '导入结果显示区域',
        ['成功导入：1台', '未成功导入：2台', 'test', '124434235123153432212123']
    )
    # 点击确认绑定按钮
    tool.click_action(
        'affirm',
        '确认绑定按钮',
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
        '设备解绑成功',
        end='@结束@'
    )


def del_scene():
    time.sleep(5)
    # 点击删除图标
    tool.click_action(
        '//a[@title="删除"]',
        '删除图标'
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
        '删除自定义语音成功'
    )
    time.sleep(3)
    tool.equal_text_assert(
        '//table[@id="soundDiyTable"]/tbody/tr/td',
        '查询结果列表',
        '查询不到数据！',
        '@结束@'
    )


if __name__ == "__main__":
    clear_test_account_config()
    add_self_scene()
    query_scene()
    modify_scene()
    bind_device()
    scene_issue()
    unbind_device()
    del_scene()
    tool.mark_status()
    tool.finished()
