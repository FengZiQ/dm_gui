# coding=utf-8
from api_condition import *
from gui_test_tool import *


def precondition():
    # 销售设备
    unsold_d = get_unsold_device_info()
    bind_device(
        '44',
        '0010025',
        [unsold_d[i]['id'] for i in range(len(unsold_d))]
    )
    return unsold_d


def device_query():
    # 测试数据
    device_info = precondition()
    tool = GUITestTool()
    # 进入我的设备页
    tool.click_action(
        '//*[@id="leftNav"]/li[3]',
        '设备管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[3]/ul/li[2]',
        '我的设备标签',
    )

    tool.fill_action(
        '//*[@id="queryDeviceId"]',
        device_info[0]['serialNum'],
        '设备编号输入框'
    )
    tool.click_action(
        '//*[@class="searchBtn"]',
        '查询按钮'
    )
    # 断言
    tool.equal_text_assert(
        'fontbold',
        'list count',
        '1',
        '',
        By.CLASS_NAME
    )
    tool.equal_text_assert(
        '//table/tbody/tr/td[2]/a',
        '查询得到的设备号',
        device_info[0]['serialNum']
    )

    tool.fill_action(
        '//*[@id="queryDeviceId"]',
        '',
        '设备编号输入框'
    )
    # 服务商选择测试账户
    tool.click_action(
        '/html/body/div/div/div/div/div[1]/div/button',
        '服务商名称下拉列表'
    )
    tool.click_action(
        '/html/body/div/div/div/div/div/div/div/ul/li[22]/a',
        '选择测试账户'
    )
    # 断言
    tool.no_text_assert(
        '/html/body/div/div/div/div/div[4]',
        '表格',
        ['北京意锐新创科技有限公司', '测试设备专用账户'],
    )

    # 产品类型选择“国际版”
    tool.click_action(
        '/html/body/div/div/div/div/div/select[1]/option[4]',
        '产品类型下拉列表'
    )
    # 断言
    tool.no_text_assert(
        '/html/body/div/div/div/div/div[4]',
        '表格',
        ['条码扫描设备', 'Inspos系列', '专销产品', '配件']
    )

    # 设备类型选择“RC”
    tool.click_action(
        '/html/body/div/div/div/div/div/select[2]/option[2]',
        '设备类型下拉列表'
    )
    # 断言
    tool.no_text_assert(
        '/html/body/div/div/div/div/div[4]',
        '表格',
        ['加强版', '基础版', '兼容版', '闪票小盒', '外设产品', '公交扫码设备'],
    )
    # 连接状态选择“已连接”
    tool.click_action(
        '/html/body/div/div/div/div/div/select[3]/option[2]',
        '连接状态下拉框'
    )
    # 断言
    tool.contained_text_assert(
        '/html/body/div/div/div/div/div/div/span',
        'list count',
        ['0'],
        '@结束@'
    )
    tool.mark_status()
    tool.finished()
    # 清理环境
    unbind_device([device_info[i]['id'] for i in range(len(device_info))])


if __name__ == "__main__":
    device_query()
