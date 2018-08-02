# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()


def del_global_config():
    # 前置条件：增加一个名为“全局配置删除测试”的全局配置
    add_global_config('全局配置删除测试')

    # 进入全局配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[10]',
        '全局配置标签'
    )
    # 配置名称输入框：全局配置删除测试
    tool.fill_action(
        'configName',
        '全局配置删除测试',
        '配置名称输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 点击删除全局配置图标，进入删除页面
    tool.click_action(
        '//a[@title="删除全局配置"]',
        '删除全局配置图标'
    )
    # 点击确定按钮
    tool.click_action(
        'ok',
        '确定按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '删除全局配置信息成功！'
    )
    time.sleep(3)
    tool.equal_text_assert(
        '//table[@id="globalConfigTable"]/tbody/tr/td',
        '查询结果列表',
        '查询不到数据！',
        '@结束@'
    )
    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    del_global_config()

