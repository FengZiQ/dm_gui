# coding=utf-8
from gui_test_tool import *
from api_condition import *
from view_log import view_log

tool = GUITestTool()


# 通过配置信息获取配置id
def get_wallpaper_config_id(wallpaper='脚本用勿动__自定义壁纸'):
    try:
        res = session.get(
            server + 'scanConfig/pageList?name=' + wallpaper
        )
        temp = json.loads(res.text)
        return temp['data']['list'][0]['id']
    except Exception as e:
        print(e)


# 将设备"4113180400130999"绑定在“脚本用勿动__自定义壁纸”配置中
def wallpaper_config_bind_device(config_id):
    try:
        res = session.post(
            server + 'deviceIsBindScanConfig/add',
            json={
                "images": [{}],
                "scanconfigid": int(config_id),
                "deviceList": [{
                    "serialNum": "4113180400130999",
                    "baseModelType": "168"
                }],
                "customerId": 44
            }
        )
        temp = json.loads(res.text)
        return temp['data']
    except Exception as e:
        print(e)


def scene_issue():
    cfg_id = get_wallpaper_config_id()
    bind_id = wallpaper_config_bind_device(cfg_id)
    # 进入自定义壁纸页
    tool.click_action(
        '//*[@id="leftNav"]/li[5]',
        '系统定制标签'
    )
    # 点击自定义壁纸标签
    tool.click_action(
        '//*[@id="leftNav"]/li[5]/ul/li[4]',
        '自定义壁纸标签'
    )
    # 查询“脚本用勿动__自定义壁纸”配置
    tool.fill_action(
        'name',
        '脚本用勿动__自定义壁纸',
        '语音名称输入框',
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
        ['DeviceScanConfigHandler', 'msg={"deviceNoList":', '"scanConfigId"'],
        end='@结束@'
    )

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    scene_issue()
