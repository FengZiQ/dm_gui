# coding=utf-8
from api_condition import *
from gui_test_tool import *


def unsold_device_query():
    # 测试数据
    test_data = get_unsold_device_info()
    tool = GUITestTool()

    tool.click_action(
        '/html/body/div/div/ul/li[3]/a',
        '设备管理标签'
    )
    tool.click_action(
        '/html/body/div/div/ul/li/ul/li[1]/a',
        '未销售列表标签'
    )
    tool.fill_action(
        '//*[@id="queryDeviceId"]',
        test_data[0]['serialNum'],
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

    tool.fill_action(
        '//*[@id="queryDeviceId"]',
        '',
        '设备编号输入框'
    )
    # 产品类型选择“Inspos系列”
    tool.click_action(
        '//div/div/select[1]/option[3]',
        '产品类型下拉列表'
    )
    # 断言
    tool.no_text_assert(
        '//*[@id="unboundDeviceTblId"]',
        '表格',
        ['条码扫描设备', '国际版', '专销产品', '配件']
    )

    # 设备类型选择“加强版”
    tool.click_action(
        '//div/div/select[2]/option[5]',
        '设备类型下拉列表'
    )
    # 断言
    tool.no_text_assert(
        '//*[@id="unboundDeviceTblId"]',
        '表格',
        ['RC', '基础版', '兼容版', '闪票小盒', '外设产品', '公交扫码设备'],
        '@结束@'
    )

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    unsold_device_query()
