# coding=utf-8
from gui_test_tool import *
from api_condition import *
from selenium.webdriver.common.keys import Keys

tool = GUITestTool()

cus_id = new_customer('test_测试语音模板服务商')


def add_self_scene_mode():
    # 进入系统定制页
    tool.click_action(
        '//*[@id="leftNav"]/li[5]',
        '系统定制标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[5]/ul/li[2]',
        '自定义语音模板标签'
    )
    # 点击添加语音模板按钮
    tool.click_action(
        'addbtn',
        '添加语音模板按钮',
        locator=By.ID,
        response_time=5
    )
    # 语音模板名称输入框：test_语音模板添加
    tool.fill_action(
        'name',
        'test_语音模板添加',
        '语音模板名称输入框',
        locator=By.ID
    )
    # 选择服务商
    tool.click_action(
        '//button[@data-id="customerId"]',
        '服务商选择下拉按钮'
    )
    # 搜索服务商: test_测试语音模板服务商
    tool.fill_action(
        '//input[@aria-label="Search"]',
        'test_测试语音模板服务商',
        '服务商搜索框'
    )
    # 回车选定
    tool.fill_action(
        '//input[@aria-label="Search"]',
        Keys.ENTER,
        '服务商搜索框'
    )
    # 选择两条语音场景，分别选择上传的语音文件
    tool.click_action(
        '//tbody[@id="speechTemplateTbody"]/tr[1]/td[1]/div/ins',
        '第一条语音场景复选框'
    )
    # 选择语音文件
    tool.fill_action(
        '//tbody[@id="speechTemplateTbody"]/tr[1]/td[3]/input',
        config_data['file_path'] + 'voice.wav',
        '浏览图标'
    )
    tool.click_action(
        '//tbody[@id="speechTemplateTbody"]/tr[2]/td[1]/div/ins',
        '第二条语音场景复选框'
    )
    # 选择语音文件
    tool.fill_action(
        '//tbody[@id="speechTemplateTbody"]/tr[2]/td[3]/input',
        config_data['file_path'] + 'voice.wav',
        '浏览图标'
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
        '新增自定义语音模板成功',
        end='@结束@'
    )


def query_mode():
    time.sleep(3)
    # 自定义语音模板输入框: test_语音模板添加
    tool.fill_action(
        'name',
        'test_语音模板添加',
        '自定义语音模板输入框',
        locator=By.ID
    )
    # 点击查询按钮
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 断言
    tool.equal_text_assert(
        'fontbold',
        'list count',
        '1',
        end='@结束@',
        locator=By.CLASS_NAME
    )
    # 点击详情图标，进入详情页面
    tool.click_action(
        '//a[@title="详情"]',
        '详情图标'
    )
    # 断言
    tool.contained_text_assert(
        'speechTemplateForm',
        '自定义语音模板详情显示区域',
        [
            '语音模板名称', '定制化语音文件上传',
            '请选择可定制的语音场景', '服务商'
        ],
        end='@结束@',
        locator=By.ID
    )


def modify_mode():
    tool.driver.back()
    time.sleep(5)
    # 点击修改图标，进入修改页面
    tool.click_action(
        '//a[@title="修改"]',
        '修改图标'
    )
    # 语音模板名称输入框：test_语音模板添加_modify
    tool.fill_action(
        'name',
        'test_语音模板添加_modify',
        '语音模板名称输入框',
        locator=By.ID
    )
    # 去掉一个场景
    tool.click_action(
        '//tbody[@id="speechTemplateTbody"]/tr[2]/td[1]/div/ins',
        '第二条语音场景复选框'
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
        '修改自定义语音模板成功',
        end='@结束@'
    )
    time.sleep(3)
    # 点击修改图标，进入修改页面
    tool.click_action(
        '//a[@title="修改"]',
        '修改图标'
    )
    # 新增一条场景
    tool.click_action(
        '//tbody[@id="speechTemplateTbody"]/tr[2]/td[1]/div/ins',
        '第二条语音场景复选框'
    )
    # 选择语音文件
    tool.fill_action(
        '//tbody[@id="speechTemplateTbody"]/tr[2]/td[3]/input',
        config_data['file_path'] + 'voice.wav',
        '浏览图标'
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
        '修改自定义语音模板成功',
        end='@结束@'
    )


def del_scene_mode():
    time.sleep(5)
    # 点击删除图标
    tool.click_action(
        '//a[@title="删除"]',
        '删除图标'
    )
    # 点击确定按钮
    tool.click_action(
        'ok',
        '确定按钮',
        locator=By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '删除自定义语音模板板成功'
    )
    time.sleep(3)
    tool.equal_text_assert(
        '//table[@id="speechTemplateTable"]/tbody/tr/td',
        '查询结果列表',
        '查询不到数据！',
        '@结束@'
    )


if __name__ == "__main__":
    add_self_scene_mode()
    query_mode()
    modify_mode()
    del_scene_mode()
    tool.mark_status()
    tool.finished()
    # 清理环境
    delete_customer(cus_id)