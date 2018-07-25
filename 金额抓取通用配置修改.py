# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()

# 前置条件：给测试账户服务商创建一个名为“selenium_测试_sum”的金额抓取通用配置
sum_config_id = add_sum_catch_common_config('44', 'selenium_测试_sum')


def sum_common_config_modify():
    # 进入金额抓取通用配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[2]',
        '金额抓取通用配置标签'
    )
    # 配置名称输入框输入：selenium_测试_sum
    tool.fill_action(
        'configName',
        'selenium_测试_sum',
        '配置名称输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 点击修改图标，进入修改页面
    tool.click_action(
        '//a[@title="修改"]',
        '修改图标'
    )
    # 配置名称输入框: selenium_测试_sum
    tool.fill_action(
        'configName',
        'selenium_测试_sum',
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
    # 日志上传开关: 关
    tool.click_action(
        '//form[@id="customerConfigForm"]/div[5]/div/div[2]/ins',
        '日志上传开关radio'
    )
    # 票据上传开关: 关
    tool.click_action(
        '//form[@id="customerConfigForm"]/div[6]/div/div[2]/ins',
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
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改金额抓取通用配置信息成功',
        end='@结束@'
    )


def modify_by_another_config_name():
    # 点击修改图标，进入修改页面
    tool.click_action(
        '//a[@title="修改"]',
        '修改图标'
    )
    # 配置名称输入框: 测试_fengziqi
    tool.fill_action(
        'configName',
        '测试_fengziqi',
        '配置名称输入框',
        locator=By.ID
    )
    # 点击保存按钮
    tool.click_action(
        'saveBtn',
        '保存按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '配置名称已经存在',
        end='@结束@'
    )


if __name__ == "__main__":
    sum_common_config_modify()
    modify_by_another_config_name()
    tool.mark_status()
    tool.finished()
    # 清理环境
    del_sum_catch_common_config(sum_config_id)
