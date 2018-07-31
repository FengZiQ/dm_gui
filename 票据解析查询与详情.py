# coding=utf-8
from gui_test_tool import *
from api_condition import *
from selenium.webdriver.common.keys import Keys

tool = GUITestTool()

# 前置条件：将设备“4113180400130999”绑定在票据解析模板“测试_fengziqi”下
device_info = get_device_info('4113180400130999')
mode_id = get_receipt_config_id('测试_fengziqi')
try:
    receipt_config_bind_device(device_info['id'], device_info['serialNum'], mode_id)
except:
    pass


def query_by_provider_name():
    # 进入票据解析页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[9]',
        '票据解析标签'
    )
    # 服务商选择：测试账户
    tool.click_action(
        '//button[@data-id="customerId"]',
        '服务商选择下拉按钮'
    )
    # 搜索服务商
    tool.fill_action(
        '//input[@aria-label="Search"]',
        '测试账户',
        '服务商搜索框'
    )
    # 回车选定
    tool.fill_action(
        '//input[@aria-label="Search"]',
        Keys.ENTER,
        '服务商搜索框',
        response_time=3
    )
    # 断言
    tool.no_text_assert(
        'templateTable',
        '查询结果列表',
        ['北京意锐新创科技有限公司'],
        end='@结束@',
        locator=By.ID
    )


def query_mode_name():
    # 模板名称输入框：测试_fengziqi
    tool.fill_action(
        'templateName',
        '测试_fengziqi',
        '模板名称输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'searchBtn',
        '查询按钮',
        locator=By.CLASS_NAME
    )
    # 断言
    tool.equal_text_assert(
        'fontbold',
        'list count',
        '1',
        end='@结束@',
        locator=By.CLASS_NAME
    )


def query_device_no():
    try:
        tool.driver.find_element_by_id('templateName').clear()
    except:
        pass
    # 设备编号输入框：4113180400130999
    tool.fill_action(
        'deviceNo',
        '4113180400130999',
        '服务商搜索框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'searchBtn',
        '查询按钮',
        locator=By.CLASS_NAME
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
        'resolveForm',
        '票据模版详情显示区域',
        expected_text=[
            '模板名称', '模板描述', '排除关键字',
            '服务商名称', '通知地址', '密钥',
            '结束类型', '抓取类型', '关键字',
            '候选字(逗号分隔)', '参数名', '提取下一行',
            '删除操作', '是否使用', '启用安全推送',
            '是否存储', '启用', '禁用',
        ],
        end='@结束@',
        locator=By.ID
    )


if __name__ == "__main__":
    query_by_provider_name()
    query_mode_name()
    query_device_no()
    verbose_info()
    tool.mark_status()
    tool.finished()
