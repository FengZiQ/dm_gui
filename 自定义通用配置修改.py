# coding=utf-8
from gui_test_tool import *
from api_condition import *

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


def return_button():
    # 进入自定义通用配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[5]',
        '自定义通用配置标签'
    )
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
    # 点击修改图标，进入修改页面
    tool.click_action(
        '//a[@title="修改"]',
        '修改图标'
    )
    # 点击返回按钮
    tool.click_action(
        'return',
        '返回按钮',
        locator=By.CLASS_NAME
    )
    # 断言
    tool.equal_text_assert(
        'addbtn',
        '添加按钮',
        '添加',
        locator=By.ID,
        end='@结束@'
    )


def delete_mark():
    # 点击修改图标，进入修改页面
    tool.click_action(
        '//a[@title="修改"]',
        '修改图标'
    )
    # 点击删除图标
    tool.click_action(
        '//tbody[@id="tbodyContent"]/tr[1]/td[5]/i',
        '删除图标'
    )
    # 断言
    tool.element_not_exist_assert(
        '//tbody[@id="tbodyContent"]/tr[2]/td[5]/i',
        '删除图标',
        end='@结束@'
    )


def self_common_config_modify():
    # 在修改自定义配置页配置名称输入框输入：test_modify
    tool.fill_action(
        'name',
        'test_modify',
        '配置名称输入框',
        locator=By.ID
    )
    # 第一行参数值输入框输入：修改值1
    tool.fill_action(
        '//tbody[@id="tbodyContent"]/tr/td[2]/input',
        '修改值1',
        '参数值输入框'
    )
    # 点击增加字段图标
    tool.click_action(
        'keyAdd',
        '增加字段图标',
        locator=By.CLASS_NAME
    )
    # 第二行参数简称下拉框：选择测试1
    tool.click_action(
        '//tbody[@id="tbodyContent"]/tr[2]/td[1]/select/option[1]',
        '参数简称下拉框'
    )
    # 第二行参数值输入框输入：修改值2
    tool.fill_action(
        '//tbody[@id="tbodyContent"]/tr[2]/td[2]/input',
        '修改值2',
        '参数值输入框'
    )
    # 点击保存按钮
    tool.click_action(
        'saveBtn',
        '保存按钮',
        locator=By.CLASS_NAME,
        response_time=3
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改自定义配置信息成功',
        end='@结束@'
    )


if __name__ == "__main__":
    return_button()
    delete_mark()
    self_common_config_modify()
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
