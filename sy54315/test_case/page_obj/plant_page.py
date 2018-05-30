from selenium.webdriver.common.by import By
from .base import Base


class PlantPage(Base):
    plant_page_button_loc = (By.XPATH,'/html/body/section/menu/ul/li/ul/li[1]/a/span')
    add_plant_button_loc = (By.XPATH, '/html/body/section/section/div[2]/a[1]')
    add_task_button_loc = (By.ID, 'allocatTask')
    checkbox1_click_loc = (By.XPATH, '//*[@id="Fixed"]/table/tbody/tr/td[1]/div/table/tbody/tr[2]/td[1]/input')
    breedName_search_text_loc = (By.NAME,'breedName')
    search_button_loc = (By.XPATH, '//*[@id="queryForm"]/ul/li[6]/input')

    # 把每一个元素封装成一个方法
    def to_plant_page(self):
        self.find_element(*self.plant_page_button_loc).click()

    def add_plant_click(self):
        self.find_element(*self.add_plant_button_loc).click()

    def add_task_click(self):
        self.find_element(*self.add_task_button_loc).click()

    def checkbox1(self):
        self.find_element(*self.checkbox1_click_loc).click()

    def breedname_search(self,text='金银花'):
        self.find_element(*self.breedName_search_text_loc).send_keys(text)

    def search_click(self):
        self.find_element(*self.search_button_loc).click()


