# coding=utf-8
from gui_test_tool import *


def package_verbose_info():

    tool = GUITestTool()

    # 进入升级包管理页
    tool.click_action(
        '//*[@id="leftNav"]/li[3]',
        '设备管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[3]/ul/li[3]',
        '升级包管理标签'
    )
    # 查询
    tool.fill_action(
        'softName',
        '测试_固件_test1',
        '升级包名称输入框',
        locator=By.ID
    )
    tool.fill_action(
        'version',
        '200.36.36.33',
        '版本号输入框',
        locator=By.ID
    )
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
        'softwareUpgradForm',
        '升级包详情页显示区域',
        expected_text=[
            '升级包类型', '升级包名称',
            '版本类型', '版本号',
            '更新类型', '所属服务商',
            '发布状态', '升级包下载',
            '更新日志'
        ],
        end='@结束@',
        locator=By.ID
    )

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    package_verbose_info()
