# coding=utf-8
from gui_test_tool import *

tool = GUITestTool()


def provider_name_query():
    # 参数配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[1]',
        '参数配置标签'
    )
    # 查询：选择测试账户服务商
    tool.fill_action(
        'customer_input',
        '测试账户',
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
    list_count = tool.wait_for_element(
        'fontbold',
        'list count',
        locator=By.CLASS_NAME
    )
    testlink('包含“测试账户”字符服务商的参数配置共有：' + list_count + '\n')
    print('期望结果：包含“测试账户”字符服务商的参数配置应大于20小于40')
    print('实际结果：包含“测试账户”字符服务商的参数配置共有' + list_count)
    if int(list_count) > 40 or int(list_count) < 20:
        tool.FailedFlag = True
    testlink('@结束@')


def para_name_query():
    try:
        tool.driver.find_element_by_id('customer_input').clear()
    except:
        pass
    tool.fill_action(
        'channelName',
        'fengziqi',
        '参数配置名称输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 断言
    tool.contained_text_assert(
        'payChannelTable',
        '查询结果列表',
        ['fengziqi', '测试账户'],
        end='@结束@',
        locator=By.ID
    )


def device_no_query():
    # 刷新当前页面
    tool.driver.refresh()
    time.sleep(3)
    tool.fill_action(
        'serialNum',
        '4113180400130999',
        '设备编号输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 断言
    tool.contained_text_assert(
        'payChannelTable',
        '查询结果列表',
        ['测试账户'],
        locator=By.ID
    )
    tool.equal_text_assert(
        'fontbold',
        'list count',
        '1',
        end='@结束@',
        locator=By.CLASS_NAME
    )


def type_query():
    # 刷新当前页面
    tool.driver.refresh()
    time.sleep(3)
    # 类型选择定额通道
    tool.click_action(
        '//select[@id="channelType"]/option[3]',
        '类型选择定额通道'
    )
    # 断言
    tool.no_text_assert(
        'payChannelTable',
        '查询结果列表',
        ['普通通道'],
        end='@结束@',
        locator=By.ID
    )


def if_default_query():
    # 是否默认：是
    tool.click_action(
        '//select[@id="isDefault"]/option[2]',
        '是否默认下拉列表，选择是'
    )
    # 断言
    tool.no_text_assert(
        'payChannelTable',
        '查询结果列表',
        ['普通通道', '否'],
        end='@结束@',
        locator=By.ID
    )


if __name__ == "__main__":
    provider_name_query()
    para_name_query()
    device_no_query()
    type_query()
    if_default_query()
    tool.mark_status()
    tool.finished()
