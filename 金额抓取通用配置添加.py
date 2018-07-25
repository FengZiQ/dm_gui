# coding=utf-8
from gui_test_tool import *
from api_condition import *
from selenium.webdriver.common.keys import Keys

tool = GUITestTool()


def add_sum_common_config_return():
    # 进入金额抓取通用配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[2]',
        '金额抓取通用配置标签'
    )
    # 点击添加按钮
    tool.click_action(
        'addbtn',
        '添加按钮',
        locator=By.ID
    )
    # 点击添加按钮
    tool.click_action(
        'return',
        '添加按钮',
        locator=By.CLASS_NAME
    )
    # 断言
    tool.equal_text_assert(
        'querybtn',
        '查询按钮',
        '查询',
        end='@结束@',
        locator=By.ID
    )


def add_sum_common_config():
    for i in range(2):
        # 点击添加按钮
        tool.click_action(
            'addbtn',
            '添加按钮',
            locator=By.ID
        )
        # 选择服务商：测试账户
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
            '服务商搜索框'
        )
        # 配置名称输入框: selenium_test_sum
        tool.fill_action(
            'configName',
            'selenium_test_sum',
            '配置名称输入框',
            locator=By.ID
        )
        # 金额识别关键字输入框: 总金额,total
        tool.fill_action(
            'feeKeyword',
            '总金额,total',
            '金额识别关键字输入框',
            locator=By.ID
        )
        # 排除关键字输入框: 退款, refund
        tool.fill_action(
            'exclusionKeyword',
            '退款, refund',
            '排除关键字输入框',
            locator=By.ID
        )
        if i == 0:
            # 日志上传开关: 开
            tool.click_action(
                '//form[@id="customerConfigForm"]/div[5]/div/div[1]/ins',
                '日志上传开关radio'
            )
            # 票据上传开关: 开
            tool.click_action(
                '//form[@id="customerConfigForm"]/div[6]/div/div[1]/ins',
                '票据上传开关radio'
            )
        # 点击保存按钮
        tool.click_action(
            'saveBtn',
            '保存按钮',
            locator=By.CLASS_NAME,
            response_time=1
        )
        # 断言
        if i == 0:
            tool.equal_text_assert(
                '/html/body/div/div/span/p',
                '提示消息',
                '新增金额抓取通用配置信息成功',
                end='@结束@'
            )
        else:
            tool.equal_text_assert(
                '/html/body/div/div/span/p',
                '提示消息',
                '配置名称已经存在',
                end='@结束@'
            )
    # 清理环境
    config_info = get_sum_catch_common_config_info('selenium_test_sum')
    del_sum_catch_common_config(config_info['id'])


if __name__ == "__main__":
    add_sum_common_config_return()
    add_sum_common_config()
    tool.mark_status()
    tool.finished()

