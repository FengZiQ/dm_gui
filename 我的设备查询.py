# coding=utf-8
from api_condition import *
from gui_test_tool import *
from selenium.webdriver.common.keys import Keys

tool = GUITestTool()
# 测试数据
test_data = get_unsold_device_info()
c_id = new_customer('test_设备管理查询')
c_info = customer_info('test_设备管理查询')
bind_device(
    c_id,
    c_info.get('treeId', ''),
    [test_data[0].get('id', ''),
     test_data[1].get('id', '')]
)


# 设备号查询
def device_no_query():
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
        test_data[0].get('serialNum', ''),
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
        end='@结束@',
        locator=By.CLASS_NAME
    )


def provider_device_no_query():
    tool.driver.refresh()
    time.sleep(3)
    # 服务商选择：test_设备管理查询
    tool.click_action(
        '//button[@data-id="customerId"]',
        '服务商选择下拉按钮'
    )
    # 搜索服务商
    tool.fill_action(
        '//input[@aria-label="Search"]',
        'test_设备管理查询',
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
    tool.equal_text_assert(
        'fontbold',
        'list count',
        '2',
        locator=By.CLASS_NAME
    )
    tool.fill_action(
        '//*[@id="queryDeviceId"]',
        test_data[0].get('serialNum', ''),
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
        end='@结束@',
        locator=By.CLASS_NAME
    )


def product_type_query():
    tool.driver.refresh()
    time.sleep(3)
    # 产品类型选择“国际版”
    tool.click_action(
        '/html/body/div/div/div/div/div/select[1]/option[4]',
        '产品类型下拉列表'
    )
    # 断言：查询结果列表中不包括['条码扫描设备', 'Inspos系列', '专销产品', '配件']
    tool.no_text_assert(
        'devicesTable',
        '查询结果列表',
        ['条码扫描设备', 'Inspos系列', '专销产品', '配件'],
        end='@结束@',
        locator=By.ID
    )


def device_type_query():
    tool.driver.refresh()
    time.sleep(3)
    # 设备类型选择“RC”
    tool.click_action(
        '/html/body/div/div/div/div/div/select[2]/option[2]',
        '设备类型下拉列表'
    )
    # 断言：查询结果列表中不包括['加强版', '基础版', '兼容版', '闪票小盒', '外设产品', '公交扫码设备']
    tool.no_text_assert(
        'devicesTable',
        '查询结果列表',
        ['加强版', '基础版', '兼容版', '闪票小盒', '外设产品', '公交扫码设备'],
        end='@结束@',
        locator=By.ID
    )


def connect_status_query():
    tool.driver.refresh()
    time.sleep(3)
    # 连接状态选择“已连接”
    tool.click_action(
        '/html/body/div/div/div/div/div/select[3]/option[2]',
        '连接状态下拉框',
        response_time=30
    )
    # 断言：查询结果列表中不包括['未连接']
    tool.no_text_assert(
        'devicesTable',
        '查询结果列表',
        ['未连接'],
        end='@结束@',
        locator=By.ID
    )


if __name__ == "__main__":
    device_no_query()
    provider_device_no_query()
    product_type_query()
    device_type_query()
    connect_status_query()
    tool.mark_status()
    tool.finished()
    # 清理环境
    delete_customer(c_id)
