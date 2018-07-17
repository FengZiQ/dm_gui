# coding=utf-8
from gui_test_tool import *
from api_condition import *


def add_keyboard_release():
    # 测试数据
    test_data = {
        'upgrade_type': ['自然更新', '强制更新'],
        'package_type': ['ppm', 'bin']
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
    for i in range(len(test_data['upgrade_type'])):
        # 新增升级包
        tool.click_action(
            'addbtn',
            '新建升级按钮',
            By.ID
        )
        time.sleep(3)
        # 选择升级包类型：键盘升级
        tool.click_action(
            '//form/div[1]/div/label[3]',
            '键盘升级包radio'
        )
        time.sleep(3)
        # 填写升级包名称
        tool.fill_action(
            'softName',
            '测试_键盘_test' + str(i+1),
            '升级包名称输入框',
            By.ID
        )
        # 选择所属服务商
        tool.click_action(
            '//button[@title="请选择服务商"]',
            '服务商下拉列表'
        )
        tool.click_action(
            '//div[@id="choice"]/div/div/div/ul/li[1]',
            '选择北京意锐新创科技有限公司'
        )
        # 选择版本类型
        tool.click_action(
            '//select[@id="subType"]/option[2]',
            '选择KBL-P04类型'
        )
        # 填写版本号
        tool.fill_action(
            'version',
            '300.36.36.1' + str(i+3),
            '版本号输入框',
            By.ID
        )
        # 选择更新类型
        tool.click_action(
            '//form/div[6]/div/label[' + str(i+1) + ']',
            test_data['upgrade_type'][i] + 'radio'
        )
        # 发布状态
        tool.click_action(
            '//form/div[10]/div/label[1]',
            '发布状态选择未发布'
        )
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
            '测试键盘升级，上传升级包类型为.' + test_data['package_type'][i],
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
            '测试_键盘_test' + str(i+1),
            '升级包名称输入框',
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
        # 清理环境
        del_upgrade_package('测试_键盘_test' + str(i+1), '')

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    add_keyboard_release()
