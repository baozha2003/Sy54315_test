from selenium.webdriver.common.by import By
from .base import Base
from time import sleep


class PlantPage(Base):
    #种植管理页面
    to_plant_page_loc = (By.XPATH, '/html/body/section/menu/ul/li/ul/li[1]/a/span')
    #新增计划按钮
    add_plant_button_loc = (By.XPATH, '/html/body/section/section/div[2]/a[1]')
    #下达任务按钮
    add_task_button_loc = (By.ID, 'allocatTask')
    #第一条计划的checkbox
    checkbox1_click_loc = (By.XPATH, '//*[@id="Fixed"]/table/tbody/tr/td[1]/div/table/tbody/tr[2]/td[1]/input')
    #药材名输入框
    breedName_search_text_loc = (By.NAME,'breedName')
    #搜索按钮
    search_button_loc = (By.XPATH, '//*[@id="queryForm"]/ul/li[6]/input')
    #完成计划按钮
    finish_plant_button_loc = (By.XPATH,'//*[@id="Fixed"]/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td/a[2]')
    finish_plant_confirm_button_loc = (By.XPATH,'//*[@id="btn_0"]')
    finish_successful_reresult_lof = (By.CLASS_NAME,'tishi')
    

    # 把每一个元素封装成一个方法
    def to_plant_page(self):
        self.find_element(*self.to_plant_page_loc).click()

    def add_plant_click(self):
        self.find_element(*self.add_plant_button_loc).click()

    def add_task_click(self):
        self.find_element(*self.add_task_button_loc).click()

    def checkbox1_click(self):
        self.find_element(*self.checkbox1_click_loc).click()

    def breedname_search(self,text='金银花'):
        self.find_element(*self.breedName_search_text_loc).send_keys(text)

    def search_click(self):
        self.find_element(*self.search_button_loc).click()

    def finish_plant(self):
        self.find_element(*self.finish_plant_button_loc).click()
        sleep(1)
        self.find_element(*self.finish_plant_confirm_button_loc).click()
        sleep(1)

    def finish_successful_reresult(self):
        reresult = self.find_element(*self.finish_successful_reresult_lof).text
        return reresult


