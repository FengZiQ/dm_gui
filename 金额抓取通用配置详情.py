# coding=utf-8
from gui_test_tool import *

tool = GUITestTool()


def sum_common_config_verbose_info():
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
    # 进入详情页面
    tool.click_action(
        '//a[@title="详情"]',
        '详情图标'
    )
    # 断言
    tool.contained_text_assert(
        'customerConfigForm',
        '金额抓取通用配置详情显示区域',
        expected_text=[
            '服务商名称', '配置名称', '金额识别关键字',
            '排除关键字', '日志上传开关', '票据上传开关'
        ],
        end='@结束@',
        locator=By.ID
    )
    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    sum_common_config_verbose_info()