# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()

# 前置条件：增加一个名为“日志配置查询测试服务商”的服务商，并为该服务商添加一个日志配置
cus_id = new_customer('日志配置查询测试服务商')
add_log_config(cus_id)
log_config_id = get_log_config_id('日志配置查询测试服务商')


def query_by_cus_name():
    # 进入日志配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[11]',
        '日志配置标签'
    )
    # 服务商名称输入框：日志配置查询测试服务商
    tool.fill_action(
        'customer_input',
        '日志配置查询测试服务商',
        '服务商名称输入框',
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


def verbose_info():
    # 点击详情图标，进入详情页面
    tool.click_action(
        '//a[@title="详情"]',
        '详情图标'
    )
    # 断言
    tool.contained_text_assert(
        'editLogConfigForm',
        '日志配置详情显示区域',
        expected_text=['服务商名称', '类型', '推送地址', '密钥', '描述'],
        end='@结束@',
        locator=By.ID
    )


if __name__ == "__main__":
    query_by_cus_name()
    verbose_info()
    tool.mark_status()
    tool.finished()
    # 清理环境
    del_log_config(log_config_id)
    delete_customer(cus_id)