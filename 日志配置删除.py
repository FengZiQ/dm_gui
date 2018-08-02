# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()


def del_config():
    # 前置条件：增加一个名为“日志配置删除测试服务商”的服务商，并给该服务商添加一个日志配置
    cus_id = new_customer('日志配置删除测试服务商')
    add_log_config(cus_id)

    # 进入日志配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[11]',
        '日志配置标签'
    )
    # 服务商名称输入框：日志配置删除测试服务商
    tool.fill_action(
        'customer_input',
        '日志配置删除测试服务商',
        '服务商名称输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 点击删除图标，进入删除页面
    tool.click_action(
        '//a[@title="删除"]',
        '删除图标'
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
        '删除日志配置成功'
    )
    time.sleep(3)
    tool.equal_text_assert(
        '//table[@id="logConfigTable"]/tbody/tr/td',
        '查询结果列表',
        '查询不到数据！',
        '@结束@'
    )
    tool.mark_status()
    tool.finished()
    # 清理环境
    delete_customer(cus_id)


if __name__ == "__main__":
    del_config()
