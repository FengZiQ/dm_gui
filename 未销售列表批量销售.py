# coding=utf-8
from gui_test_tool import *
from api_condition import *


def sell_device():
    tool = GUITestTool()
    # 测试数据
    test_data = get_unsold_device_info()
    upload_excel_file(test_data, config_data['file_path'] + '批量销售测试.xls')
    # 进入未销售列表页
    tool.click_action(
        '/html/body/div/div/ul/li[3]/a',
        '设备管理标签'
    )
    tool.click_action(
        '/html/body/div/div/ul/li/ul/li[1]/a',
        '未销售列表标签'
    )
    # 点击批量销售按钮
    tool.click_action(
        '//*[@id="bulkSales"]',
        '批量销售按钮'
    )
    # 选择批量文件
    tool.driver.find_element(By.ID, 'file').send_keys(config_data['file_path'] + '批量销售测试.xls')

    # 选择服务商
    tool.click_action(
        '/html/body/div/div/div/div/div/div/div/form/div/div/div/button',
        '点击服务商下拉列表'
    )
    tool.click_action(
        '/html/body/div/div/div/div/div/div/div/form/div/div/div/div/ul/li[21]/a/span[1]',
        '选择测试账户服务商'
    )
    tool.click_action(
        '/html/body/div/div/div/div/div/div/div/form/div[2]/input',
        '销售按钮',
        By.XPATH
    )
    # 断言
    tool.equal_text_assert(
        '/html/body/div[2]/div[2]/div[2]/div/div[6]/div/div/div[2]/p[1]/span',
        '成功销售数量',
        '15'
    )
    tool.equal_text_assert(
        '/html/body/div[2]/div[2]/div[2]/div/div[6]/div/div/div[2]/p[2]/span',
        '未销售成功数量',
        '0',
        '@结束@'
    )
    tool.mark_status()
    tool.finished()
    # 清理环境
    unbind_device([test_data[i]['id'] for i in range(len(test_data))])
    # del_excel_file()


if __name__ == "__main__":
    sell_device()
