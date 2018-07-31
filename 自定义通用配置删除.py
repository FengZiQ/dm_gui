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
add_self_common_config('test_通用配置', cus_info['id'], mode_id)


def del_self_common_config():
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
    # 点击删除图标
    tool.click_action(
        '//a[@title="删除"]',
        '删除图标'
    )
    # 点击提示框中的确定按钮
    tool.click_action(
        'ok',
        '确定按钮',
        locator=By.CLASS_NAME,
        response_time=2
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '删除自定义配置成功',
        end='@结束@'
    )


if __name__ == "__main__":
    del_self_common_config()
    tool.mark_status()
    tool.finished()
    # 清理环境
    del_self_config_mode(mode_id, cus_info['id'])
    delete_customer(cus_info['id'])
