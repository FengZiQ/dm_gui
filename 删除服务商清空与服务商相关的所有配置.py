# coding=utf-8
import time
from api_condition import *
from business_assert import BusinessAssert

businessAssert = BusinessAssert()
# 测试数据
cus_id = new_customer('t删除服务商清空所有配置')

# 新增参数配置
para_config_id0 = add_para_config(cus_id, '1')

# 新增自定义金额抓取通用配置
sum_catch_comm_c_id0 = add_sum_catch_common_config(cus_id, 't清空金额抓取通用配置')

# 新增自定义配置模板
self_config_mode_id0 = add_self_config_mode(cus_id, 't清空自定义配置模板')

# 新增票据解析
receipt_config_id0 = add_receipt_config_mode('t清空票据解析', cus_id)

# 新增日志配置
log_config_id0 = add_log_config(cus_id)

# 新增自定义语音模板
self_voice_template_id0 = add_self_voice_template('voice.wav', 't清空自定义语音模板', cus_id)

# 新增自定义壁纸
self_wallpaper_id0 = add_self_wallpaper('test.bmp', 't清空自定义壁纸', cus_id)

# 删除服务商
delete_customer(cus_id)
time.sleep(10)

# 断言：删除服务商后参数配置要被清空
para_config_info = get_para_config('selenium_test1', cus_id)
businessAssert.no_data_assert(
    para_config_info,
    state='删除服务商后参数配置要被清空'
)

# 断言：删除服务商后金额抓取通用配置要被清空
sum_catch_config_info = get_sum_catch_common_config_info('t清空金额抓取通用配置')
businessAssert.no_data_assert(
    sum_catch_config_info,
    state='删除服务商后金额抓取通用配置要被清空'
)

# 断言：删除服务商后自定义配置模板被清空
self_config_info = get_self_config_mode_info('t清空自定义配置模板')
businessAssert.no_data_assert(
    self_config_info,
    state='删除服务商后自定义配置模板被清空'
)

# 断言：删除服务商后票据解析被清空
receipt_config_info = get_receipt_config_id('t清空票据解析', cus_id)
businessAssert.no_data_assert(
    receipt_config_info,
    state='删除服务商后票据解析被清空'
)

# 断言：删除服务商后日志配置被清空
log_config_info = get_log_config_id(cus_id)
businessAssert.no_data_assert(
    log_config_info,
    state='删除服务商后日志配置被清空'
)

# 断言：删除服务商后自定义语音模板被清空
self_voice_template_info = get_self_voice_template_id('t清空自定义语音模板')
businessAssert.no_data_assert(
    self_voice_template_info,
    state='删除服务商后自定义语音模板被清空'
)

# 断言：删除服务商后自定义壁纸被清空
self_wallpaper_info = get_self_wallpaper_id('t清空自定义壁纸')
businessAssert.no_data_assert(
    self_wallpaper_info,
    end='@结束@',
    state='删除服务商后自定义壁纸被清空'
)

# 标记cases执行状态
businessAssert.mark_status()

# 清理环境
del_para_config(para_config_id0)
del_sum_catch_common_config(sum_catch_comm_c_id0)
del_self_config_mode(self_config_mode_id0, cus_id)
del_receipt_config_mode(receipt_config_id0)
del_log_config(log_config_id0)
del_self_voice_template(self_voice_template_id0)
del_self_wallpaper(self_wallpaper_id0)
