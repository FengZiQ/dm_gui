# coding=utf-8
from gui_test_tool import *
from api_condition import *
from selenium.webdriver.common.keys import Keys

tool = GUITestTool()

# 前置条件
unsold_d = get_unsold_device_info()
# 创建一个服务商“test_自定义通用配置”
new_customer('test_自定义通用配置')
cus_info = customer_info('test_自定义通用配置')
# 销售2台设备给服务商“test_自定义通用配置”
bind_device(cus_info['id'], cus_info['treeId'], [unsold_d[0]['id'], unsold_d[1]['id']])
# 给服务商“测试自定义通用配置”新增一个自定义配置模板“test_通用配置模板”
mode_id = add_self_config_mode(cus_info['id'], 'test_通用配置模板')
# 创建一个自定义通用配置“test_通用配置”
common_config_id = add_self_common_config('test_通用配置', cus_info['id'], mode_id)
# 绑定2台设备到自定义通用配置“test_通用配置”
device_and_self_common_config(
    common_config_id,
    1,
    [unsold_d[0]['id'], unsold_d[1]['id']],
    [unsold_d[0]['serialNum'], unsold_d[1]['serialNum']]
)


def query_by_config_name():
    # 进入自定义通用配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[5]',
        '自定义通用配置标签'
    )
    # 配置名称输入框输入：test_通用配置
    tool.fill_action(
        'name',
        'test_通用配置',
        '配置名称输入框',
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


def query_by_device_no():
    try:
        tool.driver.find_element_by_id('name').clear()
    except:
        pass
    # 设备编号输入框输入绑定的设备号
    tool.fill_action(
        'serialNum',
        unsold_d[0]['serialNum'],
        '设备编号输入框',
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


def query_by_service_name():
    try:
        tool.driver.find_element_by_id('serialNum').clear()
    except:
        pass
    # 服务商选择：test_自定义通用配置
    tool.click_action(
        '//button[@data-id="customerId"]',
        '服务商选择下拉按钮'
    )
    # 搜索服务商
    tool.fill_action(
        '//input[@aria-label="Search"]',
        'test_自定义通用配置',
        '服务商搜索框'
    )
    # 回车选定
    tool.fill_action(
        '//input[@aria-label="Search"]',
        Keys.ENTER,
        '服务商搜索框',
        response_time=3
    )
    # 断言
    tool.equal_text_assert(
        'fontbold',
        'list count',
        '1',
        end='@结束@',
        locator=By.CLASS_NAME
    )


def verbose_info():
    # 点击详情图标，进入详情页面
    tool.click_action(
        '//a[@title="详情"]',
        '详情图标'
    )
    # 断言
    tool.contained_text_assert(
        'definedConfigForm',
        '自定义通用配置详情显示区域',
        expected_text=[
            '配置名称', '服务商',
            '参数简称', '参数值', '模板名称'
        ],
        end='@结束@',
        locator=By.ID
    )


if __name__ == "__main__":
    query_by_config_name()
    query_by_device_no()
    query_by_service_name()
    verbose_info()
    tool.mark_status()
    tool.finished()
    # 清理环境
    device_and_self_common_config(
        common_config_id,
        0,
        [unsold_d[0]['id'], unsold_d[1]['id']],
        [unsold_d[0]['serialNum'], unsold_d[1]['serialNum']]
    )
    del_self_common_config(common_config_id)
    del_self_config_mode(mode_id, cus_info['id'])
    delete_customer(cus_info['id'])
