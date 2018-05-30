#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import unittest
from time import sleep
import datetime
# from .models import function, myunit
from selenium.webdriver.support import expected_conditions as EC


class MyTest(unittest.TestCase):
    """药材分包模块"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://sytest.54315.com"
        self.today = str(datetime.date.today())
        self.endday = str(datetime.date.today() + datetime.timedelta(days=7))

    def test_login(self):
        """测试13727086330账号登陆"""
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_class_name("user").clear()
        driver.find_element_by_class_name("user").send_keys("13727086330")
        driver.find_element_by_class_name("password").clear()
        driver.find_element_by_class_name("password").send_keys("qwe123")
        driver.find_element_by_class_name("password").submit()
        sleep(1)

    # def test_origin_subpackage(self):
    #     """溯源药材分包测试"""
    #
    #     driver = self.driver
    #     self.login()
    #     driver.find_element_by_xpath('/html/body/section/menu/ul/li/ul/li[3]/a/span').click()
    #     sleep(1)
    #     Select(driver.find_element_by_name("medSource")).select_by_visible_text('溯源药材')
    #     driver.find_element_by_class_name('btn-gray').click()
    #     sleep(1)
    #     driver.find_element_by_xpath('/html/body/section/section/table/tbody/tr[2]/td[7]/a').click()
    #     sleep(1)
    #     driver.find_element_by_name('packNum').send_keys('2')
    #     driver.find_element_by_name('packWeight').send_keys('100')
    #     driver.find_element_by_id('btn_0').click()
    #     sleep(15)
    #     result = driver.find_element_by_css_selector('body > div.dialog > div.dialog-body > p').text
    #     self.assertEqual(result, '分包成功！')

    # def test_no_subpackage(self):
    #     """非溯源药材分包测试"""
    #
    #     driver = self.driver
    #     self.login()
    #     driver.find_element_by_xpath('/html/body/section/menu/ul/li/ul/li[3]/a/span').click()
    #     sleep(1)
    #     Select(driver.find_element_by_name("medSource")).select_by_visible_text('非溯源药材')
    #     driver.find_element_by_class_name('btn-gray').click()
    #     sleep(1)
    #     driver.find_element_by_xpath('/html/body/section/section/table/tbody/tr[2]/td[7]/a').click()
    #     sleep(1)
    #     driver.find_element_by_name('packNum').send_keys('2')
    #     driver.find_element_by_name('packWeight').send_keys('100')
    #     driver.find_element_by_id('btn_0').click()
    #     sleep(15)
    #     result = driver.find_element_by_css_selector('body > div.dialog > div.dialog-body > p').text
    #     self.assertEqual(result, '分包成功！')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
