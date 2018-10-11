# coding=utf-8
from to_log import all_logs, testlink

Pass = "'result': 'p'"
Fail = "'result': 'f'"


class BusinessAssert(object):

    def __init__(self):
        self.flag = False

    # 查询结果中包含期望文本断言
    def contained_text_assert(self, actual_result, expected_text=list(), end='', state=''):
        try:
            all_logs(state)
            all_logs('期望结果: 结果中包含：' + str(expected_text))
            all_logs('实际结果: ' + str(actual_result))
            testlink(str(actual_result))
            testlink(end)
            for t in expected_text:
                if t not in str(actual_result):
                    self.flag = True
        except Exception as e:
            print(e)

    # 查询结果为空断言
    def no_data_assert(self, result, end='', state=''):
        all_logs(state)
        all_logs('期望结果：值为空')
        all_logs('实际结果：' + str(result))
        testlink(str(result))
        testlink(end)
        if result:
            self.flag = True

    # 标记case状态
    def mark_status(self):

        if self.flag:
            all_logs(Fail + '\n')
            testlink(Fail + '\n')
        else:
            all_logs(Pass + '\n')
            testlink(Pass + '\n')

