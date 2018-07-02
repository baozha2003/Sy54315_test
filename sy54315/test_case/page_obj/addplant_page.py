from selenium.webdriver.common.by import By
from .base import Base
from time import sleep
from selenium.webdriver.support.select import Select


class AddPlantPage(Base):
    # 药材名称输入
    breedName_text_loc = (By.ID, 'breedName')
    # 种子来源自购
    radio_seedSource_buy_loc = (By.XPATH, '//*[@id="dataForm"]/ul/li[2]/input[1]')
    # 种子来源栽培
    radio_seedSource_foster_loc = (By.XPATH, '//*[@id="dataForm"]/ul/li[2]/input[2]')
    # 种子来源野生
    radio_seedSource_wild_loc = (By.XPATH, '//*[@id="dataForm"]/ul/li[2]/input[3]')
    # 种子重量
    seedWeight_text_loc = (By.NAME, 'seedWeight')
    # 选择地块按钮
    choose_massif_button_loc = (By.NAME, 'Choose')
    #选择第一个地块
    choose_frist_massif_radio = (By.XPATH,'/html/body/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[1]/input')
    #选择负责人
    choose_manager_select_loc = (By.NAME, "manager")
    # 添加按钮
    add_plant_button_loc = (By.ID, 'Add')
    alter_tishi_loc = (By.XPATH, '/html/body/div[2]/div[2]/p')

    def addplant_breedname(self, text='金银花'):
        self.find_element(*self.breedName_text_loc).send_keys(text)

    def seedsource_buy(self):
        self.find_element(*self.radio_seedSource_buy_loc).click()

    def seedsource_foster(self):
        self.find_element(*self.radio_seedSource_foster_loc).click()

    def seedsource_wild(self):
        self.find_element(*self.radio_seedSource_wild_loc).click()

    def seedWeight(self, text='100'):
        self.find_element(*self.seedWeight_text_loc).send_keys(text)

    def choose_massif(self):
        self.find_element(*self.choose_massif_button_loc).click()
        sleep(1)
        self.find_element(*self.choose_frist_massif_radio).click()
        sleep(1)

    def choose_manager(self):
        self.select_element(*self.choose_manager_select_loc).select_by_index(5)

    def addplant_button(self):
        self.find_element(*self.add_plant_button_loc).click()

    def tishi_text(self):
        return self.find_element(*self.alter_tishi_loc).text

    def add_plant(self, text):
        self.addplant_breedname(text)
        self.seedsource_buy()
        self.seedWeight(150)
        self.choose_massif()
        self.choose_manager()
        self.addplant_button()
        sleep(1)
