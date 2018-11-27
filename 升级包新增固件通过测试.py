# coding=utf-8
from gui_test_tool import *
from api_condition import *
from selenium.webdriver.common.keys import Keys


def add_upgrade_patch():
    # 测试数据
    test_data = {
        'upgrade_type': ['自然更新', '强制更新', '循环升级'],
        'package_type': ['ppm', 'exe', 'bin']
    }

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
    # 新增升级包
    tool.click_action(
        'addbtn',
        '新建升级按钮',
        By.ID
    )
    # 返回按钮
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
    for i in range(len(test_data['package_type'])):
        # 新增升级包
        tool.click_action(
            'addbtn',
            '新建升级按钮',
            By.ID
        )
        time.sleep(3)
        # 选择升级包类型：固件升级包
        tool.click_action(
            '//form/div[1]/div/label[1]',
            '固件升级包radio'
        )
        time.sleep(3)
        # 填写升级包名称
        tool.fill_action(
            'softName',
            '测试_固件_test' + str(i+1),
            '升级包名称输入框',
            By.ID
        )
        # 选择版本类型
        tool.click_action(
            '//select[@id="subType"]/option[2]',
            '选择A5-System'
        )
        time.sleep(3)
        # 填写版本号
        tool.fill_action(
            'version',
            '200.36.36.3' + str(i + 3),
            '版本号输入框',
            By.ID
        )
        time.sleep(3)
        # 选择更新类型
        if i < 2:
            tool.click_action(
                '//form/div[6]/div/label[' + str(i+1) + ']',
                test_data['upgrade_type'][i] + 'radio'
            )
        else:
            tool.click_action(
                '//form/div[6]/div/span/label',
                test_data['upgrade_type'][i] + 'radio'
            )
        time.sleep(3)
        # 服务商选择：测试账户
        tool.click_action(
            '//form/div[8]/div/div/button',
            '服务商下拉列表'
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
        tool.click_action(
            'markSure',
            '确定按钮',
            By.ID
        )
        time.sleep(3)
        # 选择上传文件
        tool.fill_action(
            'file',
            config_data['file_path'] + 'test.' + test_data['package_type'][i],
            '选择文件输入框',
            By.ID
        )
        time.sleep(3)
        # 填写更新日志
        tool.fill_action(
            'updateLog',
            '测试 -*- 0.0',
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
            '新增升级包成功'
        )
        # 查询上传升级包
        try:
            tool.driver.find_element_by_id('softName').clear()
        except Exception as e:
            print(e)
        tool.fill_action(
            'softName',
            '测试_固件_test' + str(i+1),
            '升级包名称输入框',
            locator=By.ID
        )
        try:
            tool.driver.find_element_by_id('version').clear()
        except Exception as e:
            print(e)
        tool.fill_action(
            'version',
            '200.36.36.3' + str(i+3),
            '版本号输入框',
            locator=By.ID
        )
        tool.click_action(
            'querybtn',
            '查询按钮',
            locator=By.ID
        )
        time.sleep(3)
        # 断言
        tool.equal_text_assert(
            'fontbold',
            'list count',
            '1',
            locator=By.CLASS_NAME
        )
        tool.equal_text_assert(
            '//table/tbody/tr/td[6]',
            '更新类型',
            test_data['upgrade_type'][i],
            end='@结束@'
        )
        del_upgrade_package(
            '测试_固件_test' + str(i+1),
            '200.36.36.3' + str(i+3)
        )

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    add_upgrade_patch()
