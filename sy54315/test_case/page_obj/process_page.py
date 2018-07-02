from selenium.webdriver.common.by import By
from .base import Base


class ProcessPage(Base):
    # 进入初加工任务按钮
    to_process_page_loc = (By.XPATH, '/html/body/section/menu/ul/li/ul/li[2]/a/span')
    # 新增初加工计划
    add_process_button_loc = (By.XPATH, '/html/body/section/section/div[2]/a[1]')
    # 添加初加工任务
    add_process_task_button_loc = (By.XPATH, '//*[@id="allocatTask"]')
    # 搜索品种名输入框
    breedName_search_text_loc = (By.NAME, 'breedName')
    # 药材来源选择框0全部1溯源2非溯源
    choose_medSource_select_loc = (By.XPATH, '//*[@id="queryForm"]/ul/li[3]/select')
    # 搜索查询按钮
    search_button_loc = (By.XPATH, '//*[@id="queryForm"]/ul/li[6]/input')
    # checkbox1
    checkbox1_click_loc = (By.XPATH, '/html/body/section/section/table/tbody/tr[2]/td[1]/input')
    # 第一行药材名
    frist_line_breedName_loc = (By.XPATH,'/html/body/section/section/table/tbody/tr[2]/td[3]')

    def to_process_page(self):
        self.find_element(*self.to_process_page_loc).click()

    def add_process_button(self):
        self.find_element(*self.add_process_button_loc).click()

    def add_process_task_button(self):
        self.find_element(*self.add_process_task_button_loc).click()

    def breedName_search_text(self, text="三七"):
        self.find_element(*self.breedName_search_text_loc).send_keys(text)

    # 选择搜索药材来源0全部1为溯源2非溯源
    def choose_medSource_select(self, text=2):
        if text > 2:
            text = 0
        text = str(text)
        self.select_element(*self.choose_medSource_select_loc).select_by_index(text)

    def search_button_click(self):
        self.find_element(*self.search_button_loc).click()

    def frist_line_breedName(self):
        result = self.find_element(*self.frist_line_breedName_loc).text
        return result
