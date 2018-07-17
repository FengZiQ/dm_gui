# coding=utf-8
from gui_test_tool import *


def release_load():

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
    # 断言
    link = tool.driver.find_element_by_xpath('//a[@title="下载升级包"]').get_attribute('href')
    print('期望结果：下载图标对应的超链接为“http://inspiry-product.oss-cn-beijing.aliyuncs.com/firmware/包名”')
    print('实际结果：' + str(link))
    testlink('下载图标对应的超链接为：' + str(link))
    if 'http://inspiry-product.oss-cn-beijing.aliyuncs.com/firmware/' not in str(link):
        tool.FailedFlag = True

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    release_load()
