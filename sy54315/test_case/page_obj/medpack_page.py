from selenium.webdriver.common.by import By
from .base import Base
from time import sleep
import os


class MedPackPage(Base):
    # 进入分包页面
    to_medpack_page_loc = (By.XPATH, '/html/body/section/menu/ul/li/ul/li[3]/a')
    # 药材来源
    choose_medSource_select_loc = (By.XPATH, '//*[@id="queryForm"]/ul/li[2]/select')
    # 查询按钮
    search_button_loc = (By.XPATH, '//*[@id="queryForm"]/ul/li[5]/input')
    # 质检数据上传
    quality_data_button_loc = (By.NAME, 'file')
    # 质检人员
    qualityer_text_loc = (By.XPATH, '//*[@id="reportForm"]/ul/li[1]/input')
    # 质检日期
    quality_date_text_loc = (By.XPATH, '//*[@id="time"]')
    # 储藏条件
    storage_condition_text_loc = (By.XPATH, '//*[@id="reportForm"]/ul/li[4]/input')
    # 质检报告
    quality_report_file_loc = (By.XPATH, '//*[@id="file"]')
    # 上传质检
    uploading_report_button_loc = (By.CLASS_NAME, 'btn-green')
    # 查看报告
    check_report_button_loc = (By.NAME, 'seeReport')
    # 分包按钮
    subpackage_button_loc = (By.NAME, 'subpackage')
    # 分包数
    subpackage_quantity_text_loc = (By.XPATH, '//*[@id="subPackage"]/ul/li[1]/input')
    # 每包重量
    package_weight_text_loc = (By.XPATH, '//*[@id="subPackage"]/ul/li[2]/input')
    # 确定分包按钮
    subpackage_confirm_button_loc = (By.XPATH, '// *[ @ id = "btn_0"]')
    #分包成功输出
    subpackage_successful_text_loc = (By.XPATH,'/html/body/div[1]/div[2]/p')
    #下一页
    next_page_button_loc = (By.XPATH,'//*[@id="_next_page_already"]')

    def to_medpack_page(self):
        self.find_element(*self.to_medpack_page_loc).click()

    def choose_medSource_select(self, text=2):
        if text > 2:
            text = 0
        text = str(text)
        self.select_element(*self.choose_medSource_select_loc).select_by_index(text)

    def search_button_click(self):
        self.find_element(self.search_button_loc).click()

    def quality_data_button_click(self):
        self.find_element(*self.quality_data_button_loc).click()

    def qualityer_text_sendkeys(self, key='马铃薯'):
        self.find_element(*self.qualityer_text_loc).send_keys(key)

    def quality_date_text_sendkeys(self):
        self.find_element(*self.quality_date_text_loc).send_keys(self.date_today())

    def storage_condition_text_sendkeys(self):
        self.find_element(*self.storage_condition_text_loc).send_keys('干燥冷藏保存')

    def quality_report_file_upload(self):
        file_path = os.path.abspath('图片上传.jpg')
        print(file_path)
        self.find_element(*self.quality_report_file_loc).send_keys(file_path)

    def uploading_report_button_click(self):
        self.find_element(*self.uploading_report_button_loc).click()

    def check_report_button_click(self):
        self.find_element(*self.check_report_button_loc).click()

    def subpackage_button_click(self):
        self.find_element(*self.subpackage_button_loc).click()

    def subpackage_quantity_text_sendkeys(self, key='1'):
        self.find_element(*self.subpackage_quantity_text_loc).send_keys(key)

    def package_weight_text_sendkeys(self):
        self.find_element(*self.package_weight_text_loc).send_keys('100')

    def subpackage_confirm_button_click(self):
        self.find_element(*self.subpackage_confirm_button_loc).click()

    def subpackage_successful_text(self):
        reresult  = self.find_element(*self.subpackage_successful_text_loc).text
        return reresult

    def quality_data_upload(self):
        for i in range(100):
            if self.is_element_exist('file'):
                self.quality_data_button_click()
                sleep(1)
                self.qualityer_text_sendkeys()
                self.quality_date_text_sendkeys()
                self.storage_condition_text_sendkeys()
                self.quality_report_file_upload()
                sleep(3)
                self.uploading_report_button_click()
                break
            else:
                self.find_element(*self.next_page_button_loc).click()