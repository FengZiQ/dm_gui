# coding=utf-8
from to_log import all_logs, testlink

Pass = "'result': 'p'"
Fail = "'result': 'f'"


# 查询结果中包含期望文本断言
def contained_text_assert(actual_result, expected_text=list(), end='', state=''):
    flag = False
    try:
        all_logs(state)
        all_logs('期望结果: 结果中包含：' + str(expected_text))
        all_logs('实际结果: ' + str(actual_result))
        testlink(str(actual_result) + end)
        for t in expected_text:
            if t not in str(actual_result):
                flag = True
    except Exception as e:
        print(e)

    if flag:
        all_logs(Fail + '\n')
        testlink(Fail + '\n')
    else:
        all_logs(Pass + '\n')
        testlink(Pass + '\n')


# 查询结果为空断言
def no_data_assert(result, end='', state=''):
    all_logs(state)
    if result:
        all_logs(str(result))
        all_logs(Fail + '\n')
        testlink(Fail + '\n' + end)
    else:
        all_logs(Pass + '\n')
        testlink(Pass + '\n' + end)
