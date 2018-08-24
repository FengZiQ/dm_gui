# coding=utf-8
from gui_test_tool import *
from api_condition import *

tool = GUITestTool()


def add_service_provider():

    tool.click_action(
        '/html/body/div[1]/div[2]/ul/li[2]/a',
        '服务商管理'
    )

    before_list_count = tool.wait_for_element(
        'fontbold',
        'list count',
        By.CLASS_NAME
    )

    tool.click_action(
        'addbtn',
        '添加服务商',
        By.ID
    )
    tool.fill_action(
        'name',
        '壹',
        '服务商名称',
        By.ID
    )
    tool.fill_action(
        'abb',
        't',
        '服务商简称',
        By.ID
    )
    tool.fill_action(
        'userName',
        't',
        '服务商用户名',
        By.ID
    )
    tool.click_action(
        '//span[@id="roleChooseResult"]/i',
        '删除默认系统管理员角色'
    )
    tool.click_action(
        '//form/div/div/div/div/ul/li/span',
        '展开角色下拉框'
    )
    tool.click_action(
        '//form/div/div/div/div/ul/li/ul/li/a',
        '选择服务商(无开发)'
    )
    tool.click_action(
        '//span[@id="roleChooseResult"]/i',
        '删除默认系统管理员角色'
    )
    tool.fill_action(
        'password',
        '123456',
        '登录密码',
        By.ID
    )
    tool.fill_action(
        'contact',
        '1',
        '联系人',
        By.ID
    )
    tool.fill_action(
        'mobile',
        '00000000',
        '电话',
        By.ID
    )
    tool.fill_action(
        'mail',
        '1@100.cn',
        '邮箱',
        By.ID
    )
    tool.fill_action(
        'address',
        '1',
        '地址',
        By.ID
    )
    tool.click_action(
        'sell',
        '销售员列表',
        By.ID
    )
    tool.click_action(
        '//option[@value="1087"]',
        '销售员sadmin'
    )
    # click_action('//form/div[@class="form-group"]/div/label[@class="radioLeft"]', '服务商类型')
    # click_action('//form/div[@id="platformCount"]/div/label[@class="radioRight"]', '平台类型--SP平台')
    # click_action('//form/div[@id="platformCount"]/div/div/label[@class="radioRight"]', '平台类型--SP国际版平台')
    # click_action('//form/div[@class="form-group"]/div[@class="col-sm-3"]/label[@class="radioLeft"]', '状态')

    # 点击保存后，如果睡眠时间过长将导致提示信息丢失
    tool.click_action(
        '//form/div/button[@class="saveBtn"]',
        '保存按钮',
        response_time=1
    )

    # 断言
    tool.equal_text_assert(
        '/html/body/div/div/span/p',
        '提示消息',
        '新增服务商信息成功'
    )
    try:
        tool.equal_text_assert(
            'fontbold',
            'list count',
            str(int(before_list_count) + 1),
            end='@结束@',
            locator=By.CLASS_NAME
        )
    except:
        pass

    # cases执行结果
    tool.mark_status()

    tool.finished()
    # 清理环境，删除测试服务商 壹
    try:
        cus_info = customer_info('壹')
        delete_customer(cus_info['id'])
    except Exception as e:
        print(e)
        print('删除新增服务商信息失败')


if __name__ == "__main__":
    add_service_provider()