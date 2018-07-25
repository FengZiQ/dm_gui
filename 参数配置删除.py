# coding=utf-8
from api_condition import *
from gui_test_tool import *

tool = GUITestTool()


def precondition():
    # 创建一个无开发能力服务商并销售15台设备
    new_customer('selenium_test')
    cus_info = customer_info('selenium_test')
    # 销售设备
    device_info = get_unsold_device_info()
    bind_device(
        cus_info['id'],
        cus_info['treeId'],
        [device_info[i]['id'] for i in range(len(device_info))]
    )

    return cus_info, device_info


c_info, d_info = precondition()


def del_is_default_para_config():
    # 创建一个默认的参数配置：selenium_test1
    add_para_config(c_info['id'], '1')
    # 参数配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[1]',
        '参数配置标签'
    )
    # 查询
    tool.fill_action(
        'channelName',
        'selenium_test1',
        '参数配置名称输入框',
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
    tool.click_action(
        'ok',
        '保存按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '删除参数配置成功',
        end='@结束@'
    )


def del_not_default_not_device():
    # 创建一个非默认的参数配置：selenium_test0
    add_para_config(c_info['id'], '0')
    try:
        tool.driver.find_element_by_id('channelName').clear()
    except Exception as e:
        print(e)
    # 查询
    tool.fill_action(
        'channelName',
        'selenium_test0',
        '参数配置名称输入框',
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
    tool.click_action(
        'ok',
        '保存按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '删除参数配置成功',
        end='@结束@'
    )


def del_not_default_have_device():
    # 创建一个非默认的参数配置：selenium_test0
    pay_channel_id = add_para_config(c_info['id'], '0')
    # 给上一步创建的非默认参数配置绑定一个设备
    bind_device_for_para_config(pay_channel_id, d_info[0]['id'], d_info[0]['serialNum'])
    try:
        tool.driver.find_element_by_id('channelName').clear()
    except Exception as e:
        print(e)
    # 查询
    tool.fill_action(
        'channelName',
        'selenium_test0',
        '参数配置名称输入框',
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
    tool.click_action(
        'ok',
        '保存按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '当前参数配置存在绑定设备，不可删除',
        end='@结束@'
    )


if __name__ == "__main__":
    del_is_default_para_config()
    del_not_default_not_device()
    del_not_default_have_device()
    tool.mark_status()
    tool.finished()
    # 清理环境
    unbind_device([d_info[i]['id'] for i in range(len(d_info))])
    delete_customer(c_info['id'])
