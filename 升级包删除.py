# coding=utf-8
from gui_test_tool import *


def del_release():

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
    # 点击取消按钮
    tool.click_action(
        '//button[@class="cancel"]',
        '取消按钮'
    )
    # 点击删除图标
    tool.click_action(
        '//a[@title="删除"]',
        '删除图标'
    )
    # 点击确定按钮
    tool.click_action(
        '//button[@class="ok"]',
        '确定按钮',
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '删除成功'
    )
    tool.equal_text_assert(
        '//table/tbody/tr/td',
        '查询结果',
        '查询不到数据！',
        end='@结束@'
    )

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    del_release()
