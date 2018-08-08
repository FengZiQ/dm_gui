# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()


def open_voice_scene_page():
    # 进入系统定制页
    tool.click_action(
        '//*[@id="leftNav"]/li[5]',
        '系统定制标签'
    )
    tool.click_action(
        '//*[@id="leftNav"]/li[5]/ul/li[1]',
        '语音场景设置标签'
    )
    # 断言
    tool.contained_text_assert(
        'voiceSceneTable',
        '语音场景列表',
        ['序号', '场景名称', '操作'],
        end='@结束@',
        locator=By.ID
    )


def add_scene():
    all_logs('期望结果：新增语音场景成功')
    try:
        res = session.post(
                server + 'sceneConfig/add',
                json={
                    "sequenceId": "100",
                    "sceneName": "test"
                }
            )

        temp = json.loads(res.text)
    except Exception as e:
        tool.FailedFlag = True
        all_logs('实际结果：新增语音场景失败')
        testlink('新增语音场景失败')
        testlink('@结束@')
        print(e)
    else:
        all_logs('实际结果：新增语音场景成功')
        testlink('新增语音场景成功')
        testlink('@结束@')
        return temp['data']


def modify_scene():
    all_logs('期望结果：修改语音场景成功')
    try:
        session.post(
                server + 'sceneConfig/modify',
                json={
                    "id": int(scene_config_id),
                    "sequenceId": "101",
                    "sceneName": "modify"
                }
            )
    except Exception as e:
        tool.FailedFlag = True
        all_logs('实际结果：修改语音场景失败')
        testlink('修改语音场景失败')
        testlink('@结束@')
        print(e)
    else:
        all_logs('实际结果：修改语音场景成功')
        testlink('修改语音场景成功')
        testlink('@结束@')


def delete_scene():
    all_logs('期望结果：删除语音场景成功')
    try:
        session.post(
                server + 'sceneConfig/deletes',
                json={"id": int(scene_config_id)}
            )
    except Exception as e:
        tool.FailedFlag = True
        all_logs('实际结果：删除语音场景失败')
        testlink('删除语音场景失败')
        testlink('@结束@')
        print(e)
    else:
        all_logs('实际结果：删除语音场景成功')
        testlink('删除语音场景成功')
        testlink('@结束@')


if __name__ == "__main__":
    open_voice_scene_page()
    scene_config_id = add_scene()
    modify_scene()
    delete_scene()
    tool.mark_status()
    tool.finished()
