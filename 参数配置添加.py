# coding=utf-8
from gui_test_tool import *
from api_condition import *
from selenium.webdriver.common.keys import Keys

tool = GUITestTool()


def precondition():
    # 创建一个无开发能力服务商并销售15台设备
    new_customer('selenium_test')
    c_info = customer_info('selenium_test')
    # 销售设备
    d_info = get_unsold_device_info()
    bind_device(
        c_info['id'],
        c_info['treeId'],
        [d_info[i]['id'] for i in range(len(d_info))]
    )
    return c_info, d_info


cus_info, device_info = precondition()


def add_para_config():
    # 参数配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[1]',
        '参数配置标签'
    )
    # 点击添加按钮
    tool.click_action(
        'addbtn',
        '添加按钮',
        locator=By.ID
    )
    # 点击返回按钮
    tool.click_action(
        '//div[@id="saveDiv"]/div',
        '返回按钮'
    )
    # 断言
    tool.equal_text_assert(
        'addbtn',
        '添加按钮',
        '添加',
        end='@结束@',
        locator=By.ID
    )
    for i in range(3):
        # 点击添加按钮
        tool.click_action(
            'addbtn',
            '添加按钮',
            locator=By.ID
        )
        # 填写配置名称
        tool.fill_action(
            'description',
            'selenium_测试' + str(i),
            '配置名称输入框',
            locator=By.ID
        )
        # 选择服务商
        tool.click_action(
            '//button[@data-id="customerId"]',
            '服务商选择下拉按钮'
        )
        # 搜索服务商
        tool.fill_action(
            '//input[@aria-label="Search"]',
            'selenium_test',
            '服务商搜索框'
        )
        # 回车选定
        tool.fill_action(
            '//input[@aria-label="Search"]',
            Keys.ENTER,
            '服务商搜索框'
        )
        # 是否默认
        if i == 0:
            tool.click_action(
                '//form[@id="payChannelForm"]/div[3]/div/div[2]/ins',
                '否radio'
            )
        # 输入密钥
        tool.fill_action(
            'sign_key',
            '123456',
            '密钥输入框',
            locator=By.ID
        )
        if i == 0 or i == 2:
            # 类型选择
            tool.click_action(
                '//div[@id="passage"]/div/div[2]/ins',
                '定额通道radio'
            )
            # 定额金额输入
            tool.fill_action(
                'fixationMoney',
                '0.01',
                '金额输入框',
                locator=By.ID
            )
            # 订单查询链接输入
            tool.fill_action(
                'query_order_url',
                'http://testing.testing.com/testing',
                '订单查询链接输入框',
                locator=By.ID
            )
            # 订单退款链接输入
            tool.fill_action(
                'refundUrl',
                'https://testing.testing.com/testing',
                '订单退款链接输入框',
                locator=By.ID
            )
            # 订单撤销链接输入
            tool.fill_action(
                'cancelUrl',
                'https://testing.testing.com/testing',
                '订单撤销链接输入框',
                locator=By.ID
            )
            # 账单查询链接输入
            tool.fill_action(
                'queryBillUrl',
                'http://testing.testing.com/testing',
                '账单查询链接输入框',
                locator=By.ID
            )
            # 卡券核销链接输入
            tool.fill_action(
                'couponUrl',
                'https://testing.testing.com/testing',
                '卡券核销链接输入框',
                locator=By.ID
            )
            # 被扫链接输入
            tool.fill_action(
                'scanned_pay_url',
                'https://testing.testing.com/testing',
                '被扫链接输入框',
                locator=By.ID
            )
            # 主扫链接输入
            tool.fill_action(
                'generate_order_url',
                'http://testing.testing.com/testing',
                '主扫链接输入框',
                locator=By.ID
            )
            # 请输入超时时间输入
            tool.fill_action(
                'time_out',
                '30',
                '请输入超时时间输入框',
                locator=By.ID
            )
        tool.click_action(
            '//div[@id="saveDiv"]/button',
            '保存按钮',
            response_time=1
        )
        # 断言
        tool.equal_text_assert(
            '/html/body/div/div/span/p',
            '提示消息',
            '新增参数配置信息成功'
        )
        # 查询
        tool.fill_action(
            'channelName',
            'selenium_测试' + str(i),
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
            ['selenium_测试' + str(i), 'selenium_test'],
            end='@结束@',
            locator=By.ID
        )


if __name__ == "__main__":
    add_para_config()

    tool.mark_status()
    tool.finished()
    # 清理环境
    unbind_device([device_info[i]['id'] for i in range(len(device_info))])
    delete_customer(cus_info['id'])
