from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
import datetime
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 基本层
class Base(object):

    def __init__(self, driver, base_url='http://sytest.54315.com'):
        self.driver = driver
        self.base_url = 'http://sytest.54315.com'
        self.timeout = 30

    def _open(self, url):
        url_ = self.base_url + url
        # print(url_)
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        # assert self.driver.current_url == url_, 'Did ont land on %s' % url_

    def open(self):
        self._open(self.url)

    # *参数个数不是固定的（By.ID, 'kw'）
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    # 下拉框选择
    def select_element(self, *loc):
        return Select(self.find_element(*loc))

    # 当天的日期
    def date_today(self):
        return str(datetime.date.today())

    # 七天后的日期
    def date_endday(self):
        return str(datetime.date.today() + datetime.timedelta(days=7))

    def iframe(self, iframeid):
        return self.driver.switch_to.frame(iframeid)

    def iframe_out(self):
        return self.driver.switch_to.default_content()

    # 获取cookies值
    def get_cookies(self):
        return self.driver.get_cookies()

    # 判断元素是否存在返回True or False
    def is_element_exist(self, name):
        s = self.driver.find_elements_by_name(name)
        if len(s) == 0:
            print("元素未找到:%s" % name)
            return False
        else:
            return True

    # 鼠标悬停操作
    def mouse_hover(self, xpath):
        above = self.driver.find_element_by_xpath(xpath)
        ActionChains(self.driver).move_to_element(above).perform()

    # 元素显性等待
    def WaitElem(_driver, xpath, timeout=5):
        WebDriverWait(_driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
