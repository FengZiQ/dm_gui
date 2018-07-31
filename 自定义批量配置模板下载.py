# coding=utf-8
from gui_test_tool import *

tool = GUITestTool()


def download_mode():
    # 进入自定义批量配置页
    tool.click_action(
        '//*[@id="leftNav"]/li[4]',
        '配置管理标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[4]/ul/li[7]',
        '自定义批量配置标签'
    )
    button_text = tool.wait_for_element('//button[@id="downloadBtn"]', '模板下载按钮')
    href = ''
    try:
        href += tool.driver.find_element_by_id('template').get_attribute('href')
    except:
        pass
    all_logs(
        '期望结果：自定义批量配置页有“模板下载按钮”并且有超链接“https://inspiry-product.oss-cn-beijing.aliyuncs.com/template/*.xlsx”'
    )
    if button_text != '模板下载' or 'https://inspiry-product.oss-cn-beijing.aliyuncs.com/template/' not in href:
        tool.FailedFlag = True
        all_logs('实际结果：页面中没有模板下载按钮或缺少超链接“https://inspiry-product.oss-cn-beijing.aliyuncs.com/template/*.xlsx”')
        testlink('页面中没有模板下载按钮或缺少超链接“https://inspiry-product.oss-cn-beijing.aliyuncs.com/template/*.xlsx”')
        testlink('@结束@')
    else:
        all_logs(
            '实际结果：页面中有' + button_text + '且有超链接：' + href
        )
        testlink('页面中有' + button_text + '且有超链接：' + href )
        testlink('@结束@')

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    download_mode()
