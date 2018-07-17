# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from to_log import *
import time
from configuration_file import config

config_data = config()

Pass = "'result': 'p'"
Fail = "'result': 'f'"


class GUITestTool(object):

    server = config_data['server']

    def __init__(self, base_url=server):
        # login user and username
        self.user = 'admin'
        self.password = config_data['pwd']

        # mark test cases execution status
        self.FailedFlag = False

        # execution login
        # IE 浏览器测试
        # self.driver = webdriver.Ie()
        # 谷歌浏览器测试
        # self.driver = webdriver.Chrome()
        # 火狐狸浏览器测试
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(base_url)
        self.driver.find_element_by_id('username').send_keys(self.user)
        self.driver.find_element_by_id("password").send_keys(self.password)
        # self.driver.find_element_by_id("captcha").send_keys('123456')
        self.driver.find_element_by_id("loginSubmit").click()
        time.sleep(5)

    """
    locator type: 
    By.ID,By.NAME,By.CLASS_NAME,By.TAG_NAME,By.LINK_TEXT,By.PARTIAL_LINK_TEXT,By.XPATH,By.CSS_SELECTOR
    """
    def click_action(self, path, location, locator=By.XPATH, response_time=3):
        try:
            self.driver.find_element(locator, path).click()
            time.sleep(response_time)
        except Exception as e:
            print(e)
            self.FailedFlag = True
            all_logs(location + ' is not found')
            testlink(location + ' is not found')

    def fill_action(self, path, value, location, locator=By.XPATH, response_time=1):

        try:
            self.driver.find_element(locator, path).clear()
            self.driver.find_element(locator, path).send_keys(value)
            time.sleep(response_time)
        except Exception as e:
            print(e)
            self.FailedFlag = True
            all_logs(location + ' is not found')
            testlink(location + ' is not found')

    # 每条case的最后一个断言end = '@结束@'
    def equal_text_assert(self, path, location, expected_text, end='', locator=By.XPATH):
        try:
            all_logs('期望结果: ' + location + ': ' + expected_text)
            actual_text = self.driver.find_element(locator, path).text
            all_logs('实际结果: ' + location + ': ' + actual_text)
            testlink(location + ': ' + actual_text)
            testlink(end)
            if actual_text != expected_text:
                self.FailedFlag = True
        except Exception as e:
            self.FailedFlag = True
            all_logs('实际结果: ' + str(e))
            testlink(str(e))
            testlink(end)
            all_logs(location + ' is not found\n')

    # 每条case的最后一个断言end = '@结束@'
    def contained_text_assert(self, path, location, expected_text=list(), end='', locator=By.XPATH):
        try:
            all_logs('期望结果: ' + location + ': ' + str(expected_text))
            actual_text = self.driver.find_element(locator, path).text
            all_logs('实际结果: ' + location + ': ' + actual_text)
            testlink(location + ': ' + actual_text)
            testlink(end)
            for t in expected_text:
                if t not in actual_text:
                    self.FailedFlag = True
        except Exception as e:
            self.FailedFlag = True
            all_logs('实际结果: ' + str(e))
            testlink(str(e))
            testlink(end)
            all_logs(location + ' is not found\n')

    # 每条case的最后一个断言end = '@结束@'
    def no_text_assert(self, path, location, expected_text=list(), end='', locator=By.XPATH):
        try:
            all_logs('期望结果: ' + location + '中不包括' + str(expected_text))
            page_text = self.driver.find_element(locator, path).text
            all_logs('实际结果: ' + location + '中内容为”\n' + page_text + '"')
            testlink(location + '中内容为”\n' + page_text + '"')
            testlink(end)
            for t in expected_text:
                if t in page_text:
                    self.FailedFlag = True
        except Exception as e:
            self.FailedFlag = True
            all_logs('实际结果: ' + str(e))
            testlink(str(e))
            testlink(end)
            all_logs(location + ' is not found\n')

    def wait_for_element(self, path, location, locator=By.XPATH):
        text = ''
        for i in range(10):
            try:
                if self.driver.find_element(locator, path):
                    text += self.driver.find_element(locator, path).text
                    break
            except Exception as e:
                print(e)
                all_logs(location + ' is not found\n')
                break
            time.sleep(1)
        else:
            all_logs('time out')

        return text

    def mark_status(self):

        if self.FailedFlag:
            all_logs('-*- The case is executed -*-\n')
            all_logs(Fail)
            testlink(Fail + '\n')
        else:
            all_logs('-*- The case is executed -*-\n')
            all_logs(Pass)
            testlink(Pass + '\n')

    def finished(self):
        self.driver.close()