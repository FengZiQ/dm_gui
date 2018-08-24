# coding=utf-8
from gui_test_tool import *


def upgrade_patch_query():

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
    tool.click_action(
        '//select[@id="type"]/option[2]',
        '软件类型选择“客户端”'
    )
    tool.click_action(
        '//select[@id="subType"]/option[3]',
        '版本类型选择“闪票小盒”'
    )
    # 断言
    tool.no_text_assert(
        '//tbody[@class="trStyle"]',
        '查询结果',
        ['固件', '键盘', 'BasePay', 'A5-System']
    )
    # 查询
    tool.click_action(
        '//select[@id="type"]/option[3]',
        '软件类型选择“固件”'
    )
    tool.click_action(
        '//select[@id="subType"]/option[2]',
        '版本类型选择“A5-System”'
    )
    tool.click_action(
        '//select[@id="upgradeStatus"]/option[2]',
        '更新类型选择“自然更新”'
    )
    tool.click_action(
        '//select[@id="status"]/option[3]',
        '状态选择“已发布”'
    )
    # 断言
    tool.no_text_assert(
        '//tbody[@class="trStyle"]',
        '查询结果',
        [
            '客户端', '键盘', 'BasePay',
            '闪票小盒', 'A5 kernel', 'A5 立扫6210',
            '强制更新', '循环升级', '未发布'
        ]
    )
    tool.driver.refresh()
    # 查询
    tool.fill_action(
        'softName',
        'A5公版',
        '升级包名称输入框',
        locator=By.ID
    )
    tool.fill_action(
        'version',
        '4.0.35.1',
        '版本号输入框',
        locator=By.ID
    )
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
        locator=By.CLASS_NAME
    )
    tool.contained_text_assert(
        'softwareUpgradTable',
        '查询结果列表',
        ['固件', 'A5-System', '4.0.35.1'],
        end="@结束@",
        locator=By.ID
    )

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    upgrade_patch_query()
