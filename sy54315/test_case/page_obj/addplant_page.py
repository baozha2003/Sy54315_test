from selenium.webdriver.common.by import By
from .base import Base
from time import sleep
from selenium.webdriver.support.select import Select


class AddPlantPage(Base):
    breedName_text_loc = (By.ID, 'breedName')
    radio_seedSource_buy_loc = (By.XPATH, '//*[@id="dataForm"]/ul/li[2]/input[1]')
    radio_seedSource_foster_loc = (By.XPATH, '//*[@id="dataForm"]/ul/li[2]/input[2]')
    radio_seedSource_wild_loc = (By.XPATH, '//*[@id="dataForm"]/ul/li[2]/input[3]')
    seedWeight_text_loc = (By.NAME, 'seedWeight')
    choose_massif_button_loc = (By.NAME, 'Choose')
    choose_manager_select_loc = (By.NAME, "manager")
    add_plant_button_loc = (By.ID, 'Add')
    alter_tishi_loc = (By.XPATH,'/html/body/div[2]/div[2]/p')

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
        self.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[1]/input').click()
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
