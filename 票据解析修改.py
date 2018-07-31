# coding=utf-8
from gui_test_tool import *
from api_condition import *
from selenium.webdriver.common.keys import Keys

tool = GUITestTool()

# 前置条件：给测试账户添加一个票据解析模板“用于修改测试”，并将设备“4113180400130999”绑定在票据解析模板下
add_receipt_config_mode('用于修改测试', '44')
mode_id = get_receipt_config_id('用于修改测试')
device_info = get_device_info('4113180400130999')


def modify_del_key_word_handle():
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
    # 模板名称输入框：用于修改测试
    tool.fill_action(
        'templateName',
        '用于修改测试',
        '模板名称输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'searchBtn',
        '查询按钮',
        locator=By.CLASS_NAME
    )
    # 点击修改图标，进入修改页面
    tool.click_action(
        '//a[@title="修改"]',
        '修改图标'
    )
    # 点击排除关键字删除按钮
    tool.click_action(
        'keyDelete',
        '排除关键字删除按钮',
        locator=By.CLASS_NAME
    )
    # 点击删除操作图标
    tool.click_action(
        '//table[@id="templateTable"]/tbody/tr/td[7]/i',
        '删除操作图标'
    )
    # 点击保存按钮
    tool.click_action(
        'saveBtn',
        '保存按钮',
        locator=By.CLASS_NAME,
        response_time=2
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改模板成功',
        end='@结束@'
    )


def modify_add_key_word_handle():
    time.sleep(3)
    # 给票据解析模板“用于修改测试”绑定设备
    try:
        receipt_config_bind_device(device_info['id'], device_info['serialNum'], mode_id)
    except:
        pass
    # 点击修改图标，进入修改页面
    tool.click_action(
        '//a[@title="修改"]',
        '修改图标'
    )
    # 模板名称输入框：modify_测试
    tool.fill_action(
        'name',
        'modify_测试',
        '模板名称输入框',
        locator=By.ID
    )
    # 点击增加关键字按钮
    tool.click_action(
        'keyAdd',
        '增加关键字按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 填入排除关键字：排除_word0
    tool.fill_action(
        '//form[@id="resolveForm"]/div[6]/div[1]/input[1]',
        '排除_word0',
        '排除关键字输入框'
    )
    # 点击3次增加字段按钮
    for i in range(3):
        tool.click_action(
            'keyAddTwo',
            '增加字段按钮',
            locator=By.CLASS_NAME,
            response_time=1
        )
    for i in range(3):
        if i % 2 != 0:
            # 结束类型：换行
            tool.click_action(
                '//table[@id="templateTable"]/tbody/tr[' + str(i+1) + ']/td[' + str(1) + ']/select/option[2]',
                '结束类型',
                response_time=1
            )
            # 抓取类型：候选字
            tool.click_action(
                '//table[@id="templateTable"]/tbody/tr[' + str(i+1) + ']/td[' + str(2) + ']/select/option[2]',
                '抓取类型',
                response_time=1
            )
            # 提取下一行：是
            tool.click_action(
                '//table[@id="templateTable"]/tbody/tr[' + str(i+1) + ']/td[' + str(6) + ']/select/option[2]',
                '提取下一行',
                response_time=1
            )
        # 关键字：关键字_word0~2
        tool.fill_action(
            '//table[@id="templateTable"]/tbody/tr[' + str(i + 1) + ']/td[' + str(3) + ']/textarea',
            '关键字_word' + str(i),
            '关键字'
        )
        # 候选字：候选字_word0~2
        tool.fill_action(
            '//table[@id="templateTable"]/tbody/tr[' + str(i + 1) + ']/td[' + str(4) + ']/textarea',
            '候选字_word' + str(i),
            '候选字'
        )
        # 参数名：参数名_word0~2
        tool.fill_action(
            '//table[@id="templateTable"]/tbody/tr[' + str(i + 1) + ']/td[' + str(5) + ']/textarea',
            '参数名_word' + str(i),
            '参数名'
        )
    # 点击保存按钮
    tool.click_action(
        'saveBtn',
        '保存按钮',
        locator=By.CLASS_NAME,
        response_time=2
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改模板成功',
        end='@结束@'
    )


if __name__ == "__main__":
    modify_del_key_word_handle()
    modify_add_key_word_handle()
    tool.mark_status()
    tool.finished()
    # 清理环境
    receipt_config_unbind_device(mode_id, ['4113180400130999'])
    del_receipt_config_mode(mode_id)