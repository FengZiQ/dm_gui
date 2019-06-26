# coding=utf-8
# 2018.03.17

import testlink
import time
import os

# 登录凭证
url = "http://192.168.20.94:80/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
tester_key = {"admin": "68f26f458e8b1d537043f76d78f815d9"}
tlc = testlink.TestlinkAPIClient(url, tester_key["admin"])

# 执行测试的项目
project_name = '设备管理平台'
# 执行测试测测试计划
test_plan_name = '20190315'
# testlink中测试例第一层，一般为模块名
first_menu = ['设备首页', '服务商管理', '设备管理', '配置管理', '用户管理', '系统管理', '数据统计']


def to_execute_cases():
    """
    遍历项目、测试计划、测试用例集以获得要执行测试计划下的测试cases
    :return: None
    """
    # 获取执行测试的项目
    projects = tlc.getProjects()
    target_project = [project for project in projects if project['name'] == project_name]

    # 获取执行测试测测试计划
    test_plan = tlc.getProjectTestPlans(target_project[0]['id'])
    target_test_plan = [plan for plan in test_plan if plan['active'] == '1' and test_plan_name in plan['name']]
    target_test_plan_id = target_test_plan[0]['id']

    # 获取本次测试要执行的所有测试用例
    target_test_cases = tlc.getTestCasesForTestPlan(target_test_plan[0]['id']).values()

    # 获取每条用例的所有信息
    case_info = [case.values() for case in target_test_cases]

    # 遍历并执行每一条测试用例
    for case_body in case_info:
        # 如果测试用例未执行过或者执行失败，就执行测试用例
        if not case_body['exec_on_build'] or case_body['exec_status'] == 'f':
            # 获取用例结果更新所需参数execduration与timestamp的值
            start_time = time.time()
            time_stamp = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            duration_min = str((time.time() - start_time) / 60)

            # 获取用例结果更新所需其他参数
            case_id = case_body["tcase_id"]
            build_information = tlc.getBuildsForTestPlan(target_test_plan[0]['id'])
            build_name = build_information[0]["name"]
            test_case_external_id = case_body['external_id']
            case_platform_name = case_body['platform_name']

            # 获取登录者身份信息
            login_name = tlc.getTestCaseAssignedTester(
                target_test_plan[0]['id'],
                case_body['full_external_id'],
                buildname=build_name,
                platformname=case_platform_name
            )
            try:
                # 判断登录者信息与用例执行者身份是否一致，一致就执行用例
                if list(tester_key.keys())[0] == login_name[0]['login']:

                    case_name = case_body['tcase_name']
                    print(case_name)

                    # 执行测试用例
                    os.system('python ' + case_name + '.py')
                    case_steps = tlc.getTestCase(case_body['tcase_id'])[0]['steps']

                    # 在testLink.notes文件中收集用例执行结果：
                    # 'result': 'p' 用例执行通过
                    # 'result': 'f' 用例执行失败
                    notes = open('testLink.notes', 'r', encoding='UTF-8')
                    temp = notes.read().split("'result': ")
                    test_case_result = temp[-1][1]
                    temp3 = temp[-2].replace("'p'", '').replace("'f'", '')
                    steps_notes = temp3.split('@结束@')[:-1]
                    notes.close()

                    # 此处需要优化
                    # 如果一条用例的测试结果与步骤长度相等，并且用例执行结果为通过，就认为用例整个通过，否则所有步骤都认为是失败的
                    if len(steps_notes) == len(case_steps) and test_case_result == 'p':

                        test_case_step_results = [{
                            'step_number': str(j + 1),
                            'result': 'p',
                            'notes': steps_notes[j]
                        } for j in range(len(steps_notes))]

                        tlc.reportTCResult(
                            case_id, target_test_plan_id,
                            build_name,
                            test_case_result,
                            'automated test cases',
                            guess=True,
                            testcaseexternalid=test_case_external_id,
                            platformname=case_platform_name,
                            execduration=duration_min,
                            timestamp=time_stamp,
                            steps=test_case_step_results
                        )
                    elif len(steps_notes) == len(case_steps) and test_case_result == 'f':

                        test_case_step_results = [{
                            'step_number': str(j + 1),
                            'result': 'f',
                            'notes': steps_notes[j]
                        } for j in range(len(steps_notes))]

                        tlc.reportTCResult(
                            case_id, target_test_plan_id,
                            build_name,
                            test_case_result,
                            'automated test cases',
                            guess=True,
                            testcaseexternalid=test_case_external_id,
                            platformname=case_platform_name,
                            execduration=duration_min,
                            timestamp=time_stamp,
                            steps=test_case_step_results
                        )
                    # 如果一条用例的测试结果与步骤长度不相等，不更新执行结果
                    else:
                        print('\nFailed updates!\n')
            except Exception as e:
                print(e)


if __name__ == "__main__":

    to_execute_cases()
