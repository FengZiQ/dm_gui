# coding=utf-8
from selenium import webdriver
from reuseBrowser import ReuseFirefox

driver0 = webdriver.Firefox()
driver0.maximize_window()
executor_url = driver0.command_executor
session_id = driver0.session_id
driver0.get('https://www.baidu.com')
del driver0

driver = ReuseFirefox(command_executor=executor_url, session_id=session_id)
