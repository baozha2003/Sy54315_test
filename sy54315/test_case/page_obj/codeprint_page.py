from selenium.webdriver.common.by import By
from .base import Base
from time import sleep
import os


class CodPrintPage(Base):
    #跳转到赋码打印页
    to_codprint_link_loc =(By.XPATH,'/html/body/section/menu/ul/li/ul/li[4]/a/span')
    # 药材名输入框
    breedName_search_text_loc = (By.NAME, 'breedName')
    # 选择药材来源
    choose_medSource_select_loc = (By.XPATH, '//*[@id="queryForm"]/ul/li[2]/select')
    # 批次号输入
    batch_text_loc = (By.NAME, 'batch')
    # 搜索按钮
    search_button_loc = (By.XPATH, '//*[@id="queryForm"]/ul/li[5]/input')
    # 赋码打印
    frist_codprint_button_loc = (By.XPATH, '//*[@id="Fixed"]/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td/a')
    #搜索结果批次号
    result_batch_no_loc = (By.XPATH,'//*[@id="Fixed"]/table/tbody/tr/td[1]/div/table/tbody/tr[2]/td[2]')

    def to_codprint_link(self):
        self.find_element(*self.to_codprint_link_loc).click()

    def breedName_search_text(self, key="三七"):
        self.find_element(*self.breedName_search_text_loc).send_keys(key)

    def choose_medSource_select(self, text=1):
        if text > 2:
            text = 0
        text = str(text)
        self.select_element(*self.choose_medSource_select_loc).select_by_index(text)

    def batch_text(self, key='ZZ2018053100006'):
        self.find_element(*self.batch_text_loc).send_keys(key)

    def search_button(self):
        self.find_element(*self.search_button_loc).click()

    def frist_codprint_button(self):
        self.find_element(*self.frist_codprint_button_loc).click()

    def result_batch_no(self):
        return self.find_element(*self.result_batch_no_loc).text
    #搜索操作
    def breedname_search_case(self):
        self.breedName_search_text()
        self.choose_medSource_select()
        self.batch_text()
        self.search_button()
