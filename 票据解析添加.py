# coding=utf-8
from gui_test_tool import *
from api_condition import *
from selenium.webdriver.common.keys import Keys

tool = GUITestTool()

# 前置条件：新增一个名为“测试票据解析服务商”的服务商
cus_id = new_customer('测试票据解析服务商')


def del_exception_word_button():
    # 进入票据解析页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[9]',
        '票据解析标签'
    )
    # 查询：测试票据解析服务商
    tool.click_action(
        '//button[@data-id="customerId"]',
        '服务商下拉列表'
    )
    # 搜索服务商测试账户
    tool.fill_action(
        '//input[@aria-label="Search"]',
        '测试票据解析服务商',
        '服务商搜索输入框'
    )
    tool.fill_action(
        '//input[@aria-label="Search"]',
        Keys.ENTER,
        '服务商搜索输入框'
    )
    # 点击新增模板按钮
    tool.click_action(
        'addbtn',
        '新增模板按钮',
        locator=By.ID
    )
    # 点击排除关键字删除按钮
    tool.click_action(
        'keyDelete',
        '排除关键字删除按钮',
        locator=By.CLASS_NAME
    )
    # 断言
    tool.element_not_exist_assert(
        'keyDelete',
        '排除关键字删除按钮',
        end='@结束@',
        locator=By.CLASS_NAME
    )


def del_action_icon():
    # 点击删除操作图标
    tool.click_action(
        '//table[@id="templateTable"]/tbody/tr/td[7]/i',
        '删除操作图标'
    )
    # 断言
    tool.element_not_exist_assert(
        '//table[@id="templateTable"]/tbody/tr/td[7]/i',
        '排除关键字删除按钮',
        end='@结束@'
    )


def add_receipt_config():
    # 模板名称输入框：add_测试
    tool.fill_action(
        'name',
        'add_测试',
        '模板名称输入框',
        locator=By.ID
    )
    # 服务商选择：测试票据解析服务商
    tool.click_action(
        '//button[@data-id="customerId"]',
        '服务商选择下拉按钮'
    )
    # 搜索服务商
    tool.fill_action(
        '//input[@aria-label="Search"]',
        '测试票据解析服务商',
        '服务商搜索框'
    )
    # 回车选定
    tool.fill_action(
        '//input[@aria-label="Search"]',
        Keys.ENTER,
        '服务商搜索框',
        response_time=3
    )
    # 模板描述输入框：这里是描述，description
    tool.fill_action(
        'description',
        '这里是描述，description',
        '模板描述称输入框',
        locator=By.ID
    )
    # 通知地址输入框：http://dm4.preo.2dupay.com:8080/customer/notify
    tool.fill_action(
        'notifyUrl',
        'http://dm4.preo.2dupay.com:8080/customer/notify',
        '通知地址输入框',
        locator=By.ID
    )
    # 密钥输入框：secret key
    tool.fill_action(
        'secretKey',
        'secret key',
        '密钥输入框',
        locator=By.ID
    )
    # 点击3次增加关键字按钮
    for i in range(3):
        tool.click_action(
            'keyAdd',
            '增加关键字按钮',
            locator=By.CLASS_NAME,
            response_time=1
        )
        # 分别填入排除关键字：排除_word0/1/2
        tool.fill_action(
            '//form[@id="resolveForm"]/div[6]/div[1]/input[' + str(i+1) + ']',
            '排除_word' + str(i),
            '排除关键字输入框'
        )
    # 点击10次增加字段按钮
    for i in range(10):
        tool.click_action(
            'keyAddTwo',
            '增加字段按钮',
            locator=By.CLASS_NAME,
            response_time=1
        )
    for i in range(10):
        if i % 2 == 0:
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
        # 关键字：关键字_word0~9
        tool.fill_action(
            '//table[@id="templateTable"]/tbody/tr[' + str(i + 1) + ']/td[' + str(3) + ']/textarea',
            '关键字_word' + str(i),
            '关键字'
        )
        # 候选字：候选字_word0~9
        tool.fill_action(
            '//table[@id="templateTable"]/tbody/tr[' + str(i + 1) + ']/td[' + str(4) + ']/textarea',
            '候选字_word' + str(i),
            '候选字'
        )
        # 参数名：参数名_word0~9
        tool.fill_action(
            '//table[@id="templateTable"]/tbody/tr[' + str(i + 1) + ']/td[' + str(5) + ']/textarea',
            '参数名_word' + str(i),
            '参数名'
        )
    # 启用安全推送：禁用
    tool.click_action(
        '//form[@id="resolveForm"]/div[9]/div/label[2]',
        '禁用安全推送radio',
        response_time=1
    )
    # 启用安全推送：启用
    tool.click_action(
        '//form[@id="resolveForm"]/div[9]/div/label[1]',
        '启用安全推送radio',
        response_time=1
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
        '添加模板成功'
    )
    time.sleep(3)
    tool.equal_text_assert(
        'fontbold',
        'list count',
        '1',
        end="@结束@",
        locator=By.CLASS_NAME
    )


if __name__ == "__main__":
    del_exception_word_button()
    del_action_icon()
    add_receipt_config()
    tool.mark_status()
    tool.finished()
    # 清理环境
    mode_id = get_receipt_config_id('add_测试', cus_id)
    del_receipt_config_mode(mode_id)
    delete_customer(cus_id)
