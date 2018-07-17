# coding=utf-8
from gui_test_tool import *

tool = GUITestTool()


def page_turning():
    page_count = ''

    tool.click_action(
        '/html/body/div[1]/div[2]/ul/li[2]/a',
        '服务商管理'
    )
    # 断言数据
    list_count = tool.wait_for_element(
        'fontbold',
        'list count',
        By.CLASS_NAME
    )
    first_page_data = tool.wait_for_element(
        '//table/tbody/tr/td[1]',
        '第一行服务商名称'
    )
    try:
        page_count = str(int(list_count)//100 + 1)
    except Exception as e:
        print(e)

    tool.click_action(
        '//div/div[4]/select/option[5]',
        '选择每页100'
    )

    tool.contained_text_assert(
        '//div/div[4]/div/div',
        '页数统计标签',
        [page_count]
    )

    tool.click_action(
        '//div/div[4]/div/li[6]/a',
        '点击下一页'
    )
    next_page_data = tool.wait_for_element(
        '//table/tbody/tr/td[1]',
        '第一行服务商名称'
    )
    print('期望第一行服务商数据为：' + next_page_data)
    testlink('第一页第一行服务商为：' + first_page_data + '；下一页第一行服务商数据为：' + next_page_data)
    if first_page_data == next_page_data:
        tool.FailedFlag = True
        print('实际第一行服务商数据为：' + first_page_data)
    print('实际第一行服务商数据为：' + next_page_data)

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
        '//table/tbody/tr/td[1]',
        '第一行服务商名称'
    )
    print('期望第一行服务商数据为：' + last_page_data)
    testlink('翻页前第一行服务商为：' + next_page_data + '；翻页后第一行服务商数据为：' + last_page_data)
    if next_page_data == last_page_data:
        tool.FailedFlag = True
        print('实际第一行服务商数据为：' + next_page_data)
    print('实际第一行服务商数据为：' + last_page_data)
    testlink('@结束@')

    tool.mark_status()
    tool.finished()


if __name__ == "__main__":
    page_turning()
