# coding=utf-8
from gui_test_tool import *
from api_condition import *


def add_upgrade_patch():
    tool = GUITestTool()

    # 进入升级包管理页
    tool.click_action(
        '//*[@id="leftNav"]/li[3]',
        '设备管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[3]/ul/li[3]',
        '升级包管理标签'
    )
    # 查询
    tool.fill_action(
        'softName',
        '测试_固件_test1',
        '升级包名称输入框',
        locator=By.ID
    )
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 进入修改页面
    tool.click_action(
        '//a[@title="修改"]',
        '修改图标'
    )
    # 点击返回按钮
    tool.click_action(
        'return',
        '返回按钮',
        By.CLASS_NAME
    )
    # 断言
    tool.equal_text_assert(
        'addbtn',
        '新建升级按钮',
        '新建升级',
        locator=By.ID
    )
    # 进入修改页面
    tool.click_action(
        '//a[@title="修改"]',
        '修改图标'
    )
    time.sleep(3)
    # 填写升级包名称
    tool.fill_action(
        'softName',
        '测试_固件_test1_111',
        '升级包名称输入框',
        By.ID
    )
    # 选择版本类型
    tool.click_action(
        '//select[@id="subType"]/option[4]',
        '选择A1 公交'
    )
    # 填写版本号
    tool.fill_action(
        'version',
        '200.36.36.352',
        '版本号输入框',
        By.ID
    )
    # 选择更新类型
    tool.click_action(
        '//form/div[6]/div/span/label',
        '更新类型选循环升级'
    )
    # 选择所属服务商：北京意锐新创科技有限公司
    tool.click_action(
        '//form/div[8]/div/div/button',
        '服务商下拉列表'
    )
    tool.click_action(
        '//div[@id="multipleChoice"]/div/div/div/ul/li[2]',
        '北京汇元网科技股份有限公司'
    )
    tool.click_action(
        'markSure',
        '确定按钮',
        By.ID
    )
    # 修改发布状态
    tool.click_action(
        '//form/div[10]/div/label[2]',
        '发布状态选择已发布'
    )
    # 填写更新日志
    tool.fill_action(
        'updateLog',
        '测试_modify',
        '更新日志输入框',
        locator=By.ID
    )
    tool.click_action(
        'saveBtn',
        '保存按钮',
        By.CLASS_NAME,
        response_time=1
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '修改升级包信息成功'
    )
    # 查询上传升级包
    try:
        tool.driver.find_element_by_id('softName').clear()
    except Exception as e:
        print(e)
    tool.fill_action(
        'softName',
        '测试_固件_test1',
        '升级包名称输入框',
        locator=By.ID
    )
    tool.click_action(
        'querybtn',
        '查询按钮',
        locator=By.ID
    )
    # 断言
    tool.equal_text_assert(
        '//table/tbody/tr/td[7]',
        '发布状态',
        '已发布',
    )
    tool.equal_text_assert(
        '//table/tbody/tr/td[6]',
        '更新类型',
        '循环升级',
        end='@结束@'
    )

    tool.mark_status()
    tool.finished()
    # 清理环境
    del_upgrade_package('测试_固件_test1_111', '200.36.36.352')


if __name__ == "__main__":
    add_upgrade_patch()
