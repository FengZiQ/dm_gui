# coding=utf-8
from gui_test_tool import *


def page_turning():
    page_count = ''
    # 进入未销售列表页
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
    # 断言数据
    list_count = tool.wait_for_element(
        'fontbold',
        'list count',
        By.CLASS_NAME
    )
    first_page_data = tool.wait_for_element(
        '//table/tbody/tr[1]/td[4]',
        '第1行第4列的版本号'
    )
    try:
        page_count = str(int(list_count)//10 + 1)
    except Exception as e:
        print(e)

    tool.click_action(
        '//div/div[4]/select/option[1]',
        '选择每页10'
    )

    tool.contained_text_assert(
        '//div/div[4]/div/div',
        '页数统计标签',
        [page_count]
    )

    tool.click_action(
        '//div/div[4]/div/li[10]/a',
        '点击下一页'
    )
    next_page_data = tool.wait_for_element(
        '//table/tbody/tr[1]/td[4]',
        '第1行第4列的版本号'
    )
    print('期望第1行第4列的版本号：' + next_page_data)
    testlink('第1行第4列的版本号为：' + first_page_data + '；第1行第4列的版本号为：' + next_page_data)
    if first_page_data == next_page_data:
        tool.FailedFlag = True
        print('实际第1行第4列的版本号为：' + first_page_data)
    print('实际第1行第4列的版本号为：' + next_page_data)

    tool.fill_action(
        '//*[@id="pageNo"]',
        page_count,
        '翻页输入框'
    )
    tool.click_action(
        '//div/div[4]/div/div/button',
        '翻页确定按钮'
    )
    last_page_data = tool.wait_for_element(
        '//table/tbody/tr[1]/td[4]',
        '第1行服务商名称'
    )
    print('期望第1行第4列的版本号为：' + last_page_data)
    testlink('翻页前第1行第4列的版本号为：' + next_page_data + '；翻页后第1行第4列的版本号为：' + last_page_data)
    if next_page_data == last_page_data:
        tool.FailedFlag = True
        print('实际第1行第4列的版本号为：' + next_page_data)
    print('实际第1行第4列的版本号为：' + last_page_data)
    testlink('@结束@')

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    page_turning()
