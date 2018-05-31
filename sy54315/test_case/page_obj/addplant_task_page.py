from selenium.webdriver.common.by import By
from .base import Base


class AddPlantTaskPage(Base):
    # 田间操作
    field_operation_radio_loc = (By.XPATH, '//*[@id="Current1"]')
    # 生长周期
    growth_cycle_radio_loc = (By.XPATH, '//*[@id="Current2"]')
    # 播种
    sow_radio_loc = (By.XPATH, '//*[@id="currentCont1"]/input[1]')
    # 除草
    weeding_radio_loc = (By.XPATH, '//*[@id="currentCont1"]/input[4]')
    # 种苗期
    germchit_radio_loc = (By.XPATH, '//*[@id="currentCont2"]/input[1]')
    # 花期
    florescence_radio_loc = (By.XPATH, '//*[@id="currentCont2"]/input[3]')
    # 成熟期
    ripe_radio_loc = (By.XPATH, '//*[@id="currentCont2"]/input[5]')
    # 任务描述
    task_describe_text_loc = (By.XPATH, '//*[@id="dataForm"]/ul/li[7]/textarea')
    # 开始日期
    startTime_text_loc = (By.ID, 'start')
    # 结束日期
    endTime_text_loc = (By.ID, 'end')
    # 提交任务按钮
    task_submit_button_loc = (By.ID, 'Confirm')
    # 任务完成提示
    tishi_text_loc = (By.CLASS_NAME, 'tishi')

    # 把每一个元素封装成一个方法
    def field_operation_click(self):
        self.find_element(*self.field_operation_radio_loc).click()

    def growth_cycle_click(self):
        self.find_element(*self.growth_cycle_radio_loc).click()

    def sow_radio_click(self):
        self.find_element(*self.sow_radio_loc).click()

    def weeding_radio_click(self):
        self.find_element(*self.weeding_radio_loc).click()

    def germchit_radio_click(self):
        self.find_element(*self.germchit_radio_loc).click()

    def florescence_radio_click(self):
        self.find_element(*self.florescence_radio_loc).click()

    def ripe_radio_click(self):
        self.find_element(*self.ripe_radio_loc).click()

    def task_describe_text(self):
        self.find_element(*self.task_describe_text_loc).send_keys("用铲子或锄子将垄间杂草铲除，行内杂草用手拔出，不伤苗，不带苗。")

    def startTime_text(self):
        self.find_element(*self.startTime_text_loc).send_keys(self.date_endday())

    def endTime_text(self):
        self.find_element(*self.endTime_text_loc).send_keys(self.date_endday())

    def task_submit(self):
        self.find_element(*self.task_submit_button_loc).click()

    def tishi_text(self):
        return self.find_element(*self.tishi_text_loc).text

    def add_Plant_Task(self):
        self.field_operation_click()
        self.sow_radio_click()
        self.task_describe_text()
        self.startTime_text()
        self.endTime_text()
        self.task_submit()

