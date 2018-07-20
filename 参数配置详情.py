# coding=utf-8
from gui_test_tool import *

tool = GUITestTool()


def para_config_verbose_info():
    # 参数配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[1]',
        '参数配置标签'
    )
    # 进入详情页面
    tool.click_action(
        '//a[@title="详情"]',
        '详情图标'
    )
    # 断言
    tool.contained_text_assert(
        'payChannelForm',
        '参数配置详情页显示区域',
        expected_text=[
            '配置名称', '服务商', '是否默认', '类型',
            '密钥', '订单查询链接', '订单退款链接', '订单撤销链接',
            '账单查询链接', '卡券核销链接', '刷卡支付(被扫)链接',
            '统一下单(主扫)链接', '请输入超时时间(s)'
        ],
        end='@结束@',
        locator=By.ID
    )
    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    para_config_verbose_info()