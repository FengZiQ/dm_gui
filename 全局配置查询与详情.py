# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()

# 前置条件：增加一个名为“全局配置查询测试”的全局配置
config_id = add_global_config('全局配置查询测试')


def query_by_config_name():
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
        '全局配置查询测试',
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


def verbose_info():
    # 点击查看全局配置详情图标，进入详情页面
    tool.click_action(
        '//a[@title="查看全局配置详情"]',
        '查看全局配置详情图标'
    )
    # 断言
    tool.contained_text_assert(
        'globalConfigForm',
        '全局配置详情显示区域',
        expected_text=['配置名称', '日志上传地址', '票据上传地址', 'ping地址'],
        end='@结束@',
        locator=By.ID
    )


if __name__ == "__main__":
    query_by_config_name()
    verbose_info()
    tool.mark_status()
    tool.finished()
    # 清理环境
    del_global_config(config_id)
